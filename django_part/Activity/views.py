from datetime import date, datetime, timedelta
from typing import Any
import math

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from HealthOverview.views import get_or_create_facade

import core


def get_facade_for_request(request: HttpRequest):
    return get_or_create_facade(request)


def get_period_dates(period: str) -> tuple[str, str]:
    today = date.today()

    if period == "1w":
        start_date = today - timedelta(days=6)
        return str(start_date), str(today)

    if period == "1m":
        start_date = today - timedelta(days=30)
        return str(start_date), str(today)

    start_date = today - timedelta(days=6)
    return str(start_date), str(today)


def parse_date(date_value: str):
    try:
        return datetime.strptime(date_value, "%Y-%m-%d").date()
    except (TypeError, ValueError):
        return None


def get_text_value(request, field_name):
    value = request.POST.get(field_name)

    if value is None:
        return ""

    return value.strip()


def get_float_value(request, field_name):
    value = request.POST.get(field_name)

    if value is None or value == "":
        return None

    try:
        return float(value)
    except ValueError:
        return None


def get_activity_date_from_request(request):
    activity_date = get_text_value(request, "activity_date")

    if activity_date == "":
        activity_date = get_text_value(request, "date_of_activity")

    if activity_date == "":
        return date.today().isoformat()

    parsed_date = parse_date(activity_date)

    if parsed_date is None:
        return date.today().isoformat()

    return parsed_date.isoformat()


def get_activity_calories_from_request(request):
    burned_calories = get_float_value(request, "burned_calories")

    if burned_calories is None:
        return 0

    if burned_calories < 0:
        return 0

    return burned_calories


def create_activity_from_request(request, burned_calories):
    activity_name = get_text_value(request, "activity_name")
    start_time = get_text_value(request, "start_time")
    end_time = get_text_value(request, "end_time")

    if activity_name == "":
        activity_name = "Workout"

    if start_time == "":
        start_time = "00:00"

    if end_time == "":
        end_time = "00:00"

    activity_obj = core.facade_logic.facade_api.SpecificActivityType(
        "Workout",
        activity_name,
        burned_calories,
        start_time,
        end_time,
    )

    return activity_obj


def handle_add_activity_form(request, facade):
    activity_date = get_activity_date_from_request(request)
    burned_calories = get_activity_calories_from_request(request)

    activity_obj = create_activity_from_request(
        request,
        burned_calories,
    )

    facade.add_activity(
        activity_obj,
        activity_date,
    )

    facade.add_burned_calories(
        burned_calories,
        activity_date,
    )


def prepare_activity_chart(
    raw_activity_data: dict[str, Any],
    period: str,
) -> tuple[list[dict[str, Any]], list[int]]:
    days_from_api = raw_activity_data.get("days", [])

    if not days_from_api:
        return [], [600, 480, 360, 240, 120, 0]

    prepared_source_days = []

    for day_item in days_from_api:
        day_date = parse_date(day_item.get("date"))

        if day_date is None:
            continue

        prepared_source_days.append(
            {
                "date": day_date,
                "day": day_item.get("day", ""),
                "burned_calories": day_item.get("burned_calories", 0),
            }
        )

    prepared_source_days.sort(key=lambda item: item["date"])

    if period == "1w":
        chart_items = prepare_week_chart_items(prepared_source_days)

    elif period == "1m":
        chart_items = prepare_month_chart_items(prepared_source_days)

    else:
        chart_items = prepare_week_chart_items(prepared_source_days)

    return prepare_chart_heights(chart_items)


def prepare_week_chart_items(
    prepared_source_days: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    chart_items = []

    for day_item in prepared_source_days:
        chart_items.append(
            {
                "label": day_item["day"],
                "burned_calories": day_item["burned_calories"],
            }
        )

    return chart_items


def prepare_month_chart_items(
    prepared_source_days: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    calories_by_week = {}

    for day_item in prepared_source_days:
        week_number = day_item["date"].isocalendar().week
        label = f"W{week_number}"

        if week_number not in calories_by_week:
            calories_by_week[week_number] = {
                "label": label,
                "burned_calories": 0,
            }

        calories_by_week[week_number]["burned_calories"] += day_item[
            "burned_calories"
        ]

    chart_items = []

    for week_number in sorted(calories_by_week.keys()):
        chart_items.append(calories_by_week[week_number])

    return chart_items


def get_nice_axis_max(max_calories: float) -> int:
    if max_calories <= 0:
        return 600

    if max_calories <= 600:
        return 600

    raw_step = max_calories / 5
    magnitude = 10 ** math.floor(math.log10(raw_step))
    normalized_step = raw_step / magnitude

    if normalized_step <= 1:
        nice_step = 1 * magnitude
    elif normalized_step <= 2:
        nice_step = 2 * magnitude
    elif normalized_step <= 5:
        nice_step = 5 * magnitude
    else:
        nice_step = 10 * magnitude

    return int(nice_step * 5)


def build_y_axis_labels(axis_max: int) -> list[int]:
    step = axis_max / 5

    return [
        round(axis_max - step * index)
        for index in range(6)
    ]


def prepare_chart_heights(
    chart_items: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[int]]:
    if not chart_items:
        return [], [600, 480, 360, 240, 120, 0]

    max_bar_height_px = 185

    max_calories = max(
        item.get("burned_calories", 0)
        for item in chart_items
    )

    axis_max = get_nice_axis_max(max_calories)
    y_axis_labels = build_y_axis_labels(axis_max)

    prepared_chart = []

    for item in chart_items:
        burned_calories = item.get("burned_calories", 0)

        height_px = round(
            (burned_calories / axis_max) * max_bar_height_px
        )

        prepared_chart.append(
            {
                "day": item["label"],
                "burned_calories": round(burned_calories, 2),
                "height_px": height_px,
            }
        )

    return prepared_chart, y_axis_labels

def activity_overview(request: HttpRequest) -> HttpResponse:
    facade = get_facade_for_request(request)

    if request.method == "POST":
        form_type = request.POST.get("form_type")

        if form_type == "add_activity":
            handle_add_activity_form(request, facade)

    period = request.GET.get("period", "1w")

    if period not in ["1w", "1m"]:
        period = "1w"

    start_period, end_period = get_period_dates(period)

    raw_activity_data = facade.get_result_of_activity_analysis(
        start_period,
        end_period,
    )

    if raw_activity_data is None:
        raw_activity_data = {}

    week_chart, y_axis_labels = prepare_activity_chart(
        raw_activity_data,
        period,
    )

    context = {
        "current_date": date.today().strftime("%d.%m.%Y"),
        "active_period": period,

        "week_chart": week_chart,
        "y_axis_labels": y_axis_labels,

        "best_calories_day": raw_activity_data.get("best_calories_day", "No data"),
        "best_calories_date": raw_activity_data.get("best_calories_date", ""),
        "best_calories_value": raw_activity_data.get("best_calories_value", 0),

        "lowest_calories_day": raw_activity_data.get("lowest_calories_day", "No data"),
        "lowest_calories_date": raw_activity_data.get("lowest_calories_date", ""),
        "lowest_calories_value": raw_activity_data.get("lowest_calories_value", 0),

        "top_activity": raw_activity_data.get("top_activity", "No data"),
        "top_activity_calories": raw_activity_data.get("top_activity_calories", 0),

        "average_calories": raw_activity_data.get("average_calories", 0),
        "total_steps": raw_activity_data.get("total_steps", 0),
        "total_calories": raw_activity_data.get("total_calories", 0),

        "activity_summary": raw_activity_data.get("activity_summary", []),
        "donut_gradient": raw_activity_data.get(
            "donut_gradient",
            "conic-gradient(#D9D9D9 0deg 360deg)",
        ),
    }

    return render(request, "activity/activity_overview.html", context)