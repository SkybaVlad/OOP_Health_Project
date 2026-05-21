from datetime import date, datetime, timedelta
from typing import Any
import math

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

import core
from core.facade_logic.facade_api import create_and_configure_facade_for_start
from core.activity.activity_type import SpecificActivityType


def load_demo_activity_data(facade):
    today = date.today()

    demo_data = [
        {
            "days_ago": 0,
            "category": "Sport",
            "name": "Running",
            "calories": 540,
            "start": "08:00",
            "end": "09:00",
            "steps": 8500,
        },
        {
            "days_ago": 1,
            "category": "Fitness",
            "name": "Gym workout",
            "calories": 430,
            "start": "18:00",
            "end": "19:10",
            "steps": 6200,
        },
        {
            "days_ago": 2,
            "category": "Sport",
            "name": "Swimming",
            "calories": 300,
            "start": "17:30",
            "end": "18:20",
            "steps": 4000,
        },
        {
            "days_ago": 3,
            "category": "Sport",
            "name": "Football",
            "calories": 500,
            "start": "16:00",
            "end": "17:30",
            "steps": 9200,
        },
        {
            "days_ago": 4,
            "category": "Health",
            "name": "Walking",
            "calories": 220,
            "start": "19:00",
            "end": "19:45",
            "steps": 7000,
        },
        {
            "days_ago": 5,
            "category": "Relaxation",
            "name": "Yoga",
            "calories": 180,
            "start": "07:30",
            "end": "08:20",
            "steps": 2500,
        },
        {
            "days_ago": 6,
            "category": "Sport",
            "name": "Basketball",
            "calories": 410,
            "start": "15:00",
            "end": "16:15",
            "steps": 8100,
        },
        {
            "days_ago": 10,
            "category": "Sport",
            "name": "Cycling",
            "calories": 700,
            "start": "10:00",
            "end": "12:00",
            "steps": 3500,
        },
        {
            "days_ago": 20,
            "category": "Fitness",
            "name": "Boxing",
            "calories": 620,
            "start": "17:00",
            "end": "18:30",
            "steps": 2800,
        },
        {
            "days_ago": 45,
            "category": "Sport",
            "name": "Tennis",
            "calories": 760,
            "start": "11:00",
            "end": "13:00",
            "steps": 5200,
        },
        {
            "days_ago": 120,
            "category": "Fitness",
            "name": "Crossfit",
            "calories": 900,
            "start": "09:00",
            "end": "11:00",
            "steps": 4300,
        },
    ]

    for item in demo_data:
        activity_date = str(today - timedelta(days=item["days_ago"]))

        activity = SpecificActivityType(
            activity_category=item["category"],
            activity_name=item["name"],
            burned_calories=item["calories"],
            start_time_of_activity=item["start"],
            end_time_of_activity=item["end"],
        )

        facade.add_activity(activity, activity_date)
        facade.add_count_of_steps(item["steps"], activity_date)


def create_user_obj() -> core.User:
    name = "Maks"
    surname = "Skyba"
    age = 18
    sex = "Male"

    user = core.User(
        name=name,
        surname=surname,
        age=age,
        sex=sex,
    )

    return user


def get_facade_for_request(request: HttpRequest):
    user_obj = create_user_obj()
    facade = create_and_configure_facade_for_start(user_obj)

    load_demo_activity_data(facade)

    return facade


def get_period_dates(period: str) -> tuple[str | None, str | None]:
    today = date.today()

    if period == "1w":
        start_date = today - timedelta(days=6)
        return str(start_date), str(today)

    if period == "1m":
        start_date = today - timedelta(days=30)
        return str(start_date), str(today)

    if period == "1y":
        start_date = today - timedelta(days=365)
        return str(start_date), str(today)

    start_date = today - timedelta(days=6)
    return str(start_date), str(today)


def parse_date(date_value: str):
    try:
        return datetime.strptime(date_value, "%Y-%m-%d").date()
    except (TypeError, ValueError):
        return None


def prepare_activity_chart(
        raw_activity_data: dict[str, Any],
        period: str,
) -> tuple[list[dict[str, Any]], list[int]]:
    days_from_api = raw_activity_data.get("days", [])

    if not days_from_api:
        return [], [600, 480, 360, 240, 120, 0]

    prepared_source_days = []

    for day in days_from_api:
        day_date = parse_date(day.get("date"))

        if day_date is None:
            continue

        prepared_source_days.append(
            {
                "date": day_date,
                "day": day.get("day", ""),
                "burned_calories": day.get("burned_calories", 0),
            }
        )

    prepared_source_days.sort(key=lambda item: item["date"])

    if period == "1w":
        chart_items = prepare_week_chart_items(prepared_source_days)

    elif period == "1m":
        chart_items = prepare_month_chart_items(prepared_source_days)

    elif period == "1y":
        chart_items = prepare_year_chart_items(prepared_source_days)

    else:
        chart_items = prepare_week_chart_items(prepared_source_days)

    return prepare_chart_heights(chart_items)


def prepare_week_chart_items(
        prepared_source_days: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    chart_items = []

    for day in prepared_source_days:
        chart_items.append(
            {
                "label": day["day"],
                "burned_calories": day["burned_calories"],
            }
        )

    return chart_items


def prepare_month_chart_items(
        prepared_source_days: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    calories_by_week = {}

    for day in prepared_source_days:
        week_number = day["date"].isocalendar().week
        label = f"W{week_number}"

        if week_number not in calories_by_week:
            calories_by_week[week_number] = {
                "label": label,
                "burned_calories": 0,
            }

        calories_by_week[week_number]["burned_calories"] += day["burned_calories"]

    chart_items = []

    for week_number in sorted(calories_by_week.keys()):
        chart_items.append(calories_by_week[week_number])

    return chart_items


def prepare_year_chart_items(
        prepared_source_days: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    month_names = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec",
    }

    calories_by_month = {}

    for day in prepared_source_days:
        month_number = day["date"].month

        if month_number not in calories_by_month:
            calories_by_month[month_number] = {
                "label": month_names[month_number],
                "burned_calories": 0,
            }

        calories_by_month[month_number]["burned_calories"] += day["burned_calories"]

    chart_items = []

    for month_number in sorted(calories_by_month.keys()):
        chart_items.append(calories_by_month[month_number])

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
    period = request.GET.get("period", "1w")

    start_period, end_period = get_period_dates(period)

    facade = get_facade_for_request(request)

    raw_activity_data = facade.get_result_of_activity_analysis(
        start_period,
        end_period,
    )

    if raw_activity_data is None:
        raw_activity_data = {}

    week_chart, y_axis_labels = prepare_activity_chart(raw_activity_data, period)

    context = {
        "current_date": date.today().strftime("%d.%m.%Y"),
        "active_period": period,

        "week_chart": week_chart,
        "y_axis_labels": y_axis_labels,

        "best_calories_day": raw_activity_data.get("best_calories_day", "No data"),
        "best_calories_value": raw_activity_data.get("best_calories_value", 0),

        "lowest_calories_day": raw_activity_data.get("lowest_calories_day", "No data"),
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