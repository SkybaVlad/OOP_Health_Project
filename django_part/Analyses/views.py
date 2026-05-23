import datetime
from typing import Any

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

import core
from core import MainFacade

from HealthOverview.views import get_or_create_facade


def get_y_axis_labels(values: list[float | int], count: int = 4) -> list[float | int]:
    if not values:
        return [0]

    max_value = max(values)

    if max_value == 0:
        return [0 for _ in range(count)]

    step = max_value / (count - 1)

    labels = []

    for index in range(count):
        value = max_value - step * index

        if max_value >= 100:
            labels.append(round(value))
        else:
            labels.append(round(value, 2))

    return labels


def get_default_analysis_period() -> tuple[str, str]:
    today_date = datetime.date.today()
    date_of_monday = today_date - datetime.timedelta(days=today_date.weekday())

    return date_of_monday.isoformat(), today_date.isoformat()


def get_analysis_period_from_request(request: HttpRequest) -> tuple[str, str]:
    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")

    if start_date and end_date:
        return start_date, end_date

    return get_default_analysis_period()

def normalize_values_for_bars(values: list[float | int]) -> list[float]:
    if not values:
        return []

    max_value = max(values)

    if max_value == 0:
        return [1 for _ in values]

    return [round(value / max_value * 100, 2) if value != 0 else 1 for value in values]


def reduce_chart_labels(labels: list[str], max_labels: int = 7) -> list[str]:
    if not labels:
        return []

    if len(labels) <= max_labels:
        return labels

    result = []

    step = (len(labels) - 1) / (max_labels - 1)

    for index in range(max_labels):
        label_index = round(index * step)
        result.append(labels[label_index])

    return result


def normalize_values_for_svg(values: list[float | int]) -> str:
    if not values:
        return ""

    min_value = min(values)
    max_value = max(values)

    chart_width = 300
    chart_height = 150
    padding_x = 10
    padding_y = 15

    if len(values) == 1:
        x = chart_width / 2
        y = chart_height / 2
        return f"{x},{y}"

    points = []

    for index, value in enumerate(values):
        x = padding_x + index * ((chart_width - 2 * padding_x) / (len(values) - 1))

        if max_value == min_value:
            y = chart_height / 2
        else:
            normalized = (value - min_value) / (max_value - min_value)
            y = chart_height - padding_y - normalized * (chart_height - 2 * padding_y)

        points.append(f"{round(x, 2)},{round(y, 2)}")

    return " ".join(points)


def normalize_values_for_large_svg(values: list[float | int]) -> str:
    if not values:
        return ""

    min_value = min(values)
    max_value = max(values)

    chart_width = 600
    chart_height = 150
    padding_x = 10
    padding_y = 15

    if len(values) == 1:
        x = chart_width / 2
        y = chart_height / 2
        return f"{x},{y}"

    points = []

    for index, value in enumerate(values):
        x = padding_x + index * ((chart_width - 2 * padding_x) / (len(values) - 1))

        if max_value == min_value:
            y = chart_height / 2
        else:
            normalized = (value - min_value) / (max_value - min_value)
            y = chart_height - padding_y - normalized * (chart_height - 2 * padding_y)

        points.append(f"{round(x, 2)},{round(y, 2)}")

    return " ".join(points)


def get_last_values(values: list[float | int], count: int = 7) -> list[float | int]:
    if not values:
        return []

    return values[-count:]


def build_analyses_context(
    analysis_result: dict[str, Any],
    start_period: str,
    end_period: str,
) -> dict[str, Any]:

    days_labels = analysis_result["days_labels"]
    short_days_labels = reduce_chart_labels(days_labels, 7)

    last_burned_values = get_last_values(
        analysis_result["burned_calories_value_for_each_day"],
        7,
    )

    last_burned_days = get_last_values(days_labels, 7)

    calories_values_for_axis = (
        analysis_result["consumed_calories_value_for_each_day"]
        + analysis_result["burned_calories_value_for_each_day"]
    )

    weight_values_for_axis = analysis_result["weight_value_for_each_day"]

    bmi_values_for_axis = analysis_result["bmi_value_for_each_day"]

    return {
        "start_period": start_period,
        "end_period": end_period,
        "calories_chart": {
            "days": short_days_labels,
            "intake_values": normalize_values_for_svg(
                analysis_result["consumed_calories_value_for_each_day"]
            ),
            "burned_values": normalize_values_for_svg(
                analysis_result["burned_calories_value_for_each_day"]
            ),
            "y_labels": get_y_axis_labels(calories_values_for_axis),
        },
        "weight_chart": {
            "days": short_days_labels,
            "values": normalize_values_for_svg(
                analysis_result["weight_value_for_each_day"]
            ),
            "y_labels": get_y_axis_labels(weight_values_for_axis),
        },
        "burned_calories_summary": {
            "avg_burned_percent": round(
                analysis_result["avg_burned_calories_percent"],
                2,
            ),
            "total_burned_percent": round(
                analysis_result["total_burned_calories_percent"],
                2,
            ),
            "daily_values_percent": normalize_values_for_bars(last_burned_values),
            "days": last_burned_days,
        },
        "small_statistics": [
            {
                "title": "Total Steps",
                "value": round(analysis_result["total_steps"]),
                "unit": "",
                "change": round(analysis_result["steps_change_percent"], 2),
            },
            {
                "title": "Active Minutes",
                "value": round(analysis_result["total_activity_time"], 2),
                "unit": "min",
                "change": round(analysis_result["activity_time_change_percent"], 2),
            },
            {
                "title": "Burned Calories",
                "value": round(analysis_result["total_burned_calories"], 2),
                "unit": "kcal",
                "change": round(analysis_result["burned_calories_change_percent"], 2),
            },
            {
                "title": "Consumed Calories",
                "value": round(analysis_result["total_consumed_calories"], 2),
                "unit": "kcal",
                "change": round(analysis_result["consumed_calories_change_percent"], 2),
            },
            {
                "title": "Water",
                "value": round(analysis_result["total_drunk_water"], 2),
                "unit": "L",
                "change": round(analysis_result["water_change_percent"], 2),
            },
            {
                "title": "Sleep",
                "value": round(analysis_result["total_sleep_hours"], 2),
                "unit": "h",
                "change": round(analysis_result["sleep_change_percent"], 2),
            },
        ],
        "summary": {
            "day_streak": analysis_result["day_streak"],
            "avg_fat": round(analysis_result["avg_fat_percentage"], 2),
            "avg_bmr": round(analysis_result["avg_bmr"], 2),
            "avg_bmi": round(analysis_result["avg_bmi"], 2),
        },
        "body_metric_chart": {
            "days": short_days_labels,
            "values": normalize_values_for_large_svg(
                analysis_result["bmi_value_for_each_day"]
            ),
            "y_labels": get_y_axis_labels(bmi_values_for_axis),
        },
    }


@login_required
def analyses(request: HttpRequest) -> HttpResponse:
    facade = get_or_create_facade(request)

    start_period, end_period = get_analysis_period_from_request(request)

    analysis_result = facade.get_result_of_analyze_some_period(
        start_period,
        end_period,
    )

    context = build_analyses_context(
        analysis_result=analysis_result,
        start_period=start_period,
        end_period=end_period,
    )

    return render(
        request,
        "analyses/analyses.html",
        context,
    )