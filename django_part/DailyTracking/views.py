import datetime

from django.shortcuts import render

from HealthOverview.views import get_or_create_facade

from core.medication.medication_objects import (
    Medication,
    MedicationReceipt,
    MedicationCharacteristicBuilder,
    Frequency,
    Interval,
)


def get_facade_for_request(request):
    return get_or_create_facade(request)


def get_float_value(request, field_name):
    value = request.POST.get(field_name)

    if value is None or value == "":
        return None

    try:
        return float(value)
    except ValueError:
        return None


def get_text_value(request, field_name):
    value = request.POST.get(field_name)

    if value is None:
        return ""

    return value.strip()


def format_number(value):
    if value is None:
        return 0

    try:
        return f"{float(value):g}"
    except (TypeError, ValueError):
        return value


def calculate_percent(value, goal):
    try:
        value = float(value)
        goal = float(goal)
    except (TypeError, ValueError):
        return 0

    if goal <= 0:
        return 0

    percent = round(value / goal * 100)

    if percent > 100:
        return 100

    if percent < 0:
        return 0

    return percent


def calculate_body_data_percent(weight, height, fat_percentage):
    filled_fields = 0

    if weight > 0:
        filled_fields += 1

    if height > 0:
        filled_fields += 1

    if fat_percentage > 0:
        filled_fields += 1

    return round(filled_fields / 3 * 100)


def add_recent_record(recent_records, title, value):
    recent_records.insert(
        0,
        {
            "title": title,
            "time": "Today",
            "value": value,
        },
    )

    return recent_records[:6]


def handle_water_sleep_form(request, facade, today_date, state, recent_records):
    water = get_float_value(request, "water")
    sleep = get_float_value(request, "sleep")

    if water is not None and water > 0:
        facade.add_water(water, today_date)
        state["water"] += water

        recent_records = add_recent_record(
            recent_records,
            "Water added",
            f"{format_number(water)} L",
        )

    if sleep is not None and sleep > 0:
        facade.add_sleep(sleep, today_date)
        state["sleep"] += sleep

        recent_records = add_recent_record(
            recent_records,
            "Sleep added",
            f"{format_number(sleep)} h",
        )

    return state, recent_records


def handle_body_metrics_form(request, facade, today_date, state, recent_records):
    weight = get_float_value(request, "weight")
    height = get_float_value(request, "height")
    fat_percentage = get_float_value(request, "fat_percentage")

    if weight is not None and weight > 0:
        facade.add_weight(weight, today_date)
        state["weight"] = weight

        recent_records = add_recent_record(
            recent_records,
            "Weight updated",
            f"{format_number(weight)} kg",
        )

    if height is not None and height > 0:
        facade.add_height(height, today_date)
        state["height"] = height

        recent_records = add_recent_record(
            recent_records,
            "Height updated",
            f"{format_number(height)} cm",
        )

    if fat_percentage is not None and fat_percentage > 0:
        facade.add_fat_percentage(fat_percentage, today_date)
        state["fat_percentage"] = fat_percentage

        recent_records = add_recent_record(
            recent_records,
            "Fat updated",
            f"{format_number(fat_percentage)}%",
        )

    return state, recent_records


def create_medication_receipt_from_form(medication_name, today_date):
    medication_obj = Medication(
        medication_name,
        "tablet",
        "pcs",
    )

    medication_characteristic = (
        MedicationCharacteristicBuilder()
        .set_medication_dosage_per_one_take(1)
        .set_frequency(Frequency.Every_day.value)
        .set_interval(Interval.Forever.value)
        .set_start_time(today_date)
        .get_result()
    )

    receipt = MedicationReceipt()

    receipt.add_pair_to_receipt(
        medication_obj,
        medication_characteristic,
    )

    return receipt


def handle_medication_form(request, facade, today_date, recent_records):
    medication_name = get_text_value(request, "medication_name")

    if medication_name == "":
        return recent_records

    receipt = create_medication_receipt_from_form(
        medication_name,
        today_date,
    )

    facade.add_receipt(receipt)

    recent_records = add_recent_record(
        recent_records,
        "Medication receipt added",
        medication_name,
    )

    return recent_records


def build_context(state, recent_records):
    water_goal = 2.0
    sleep_goal = 8.0

    return {
        "dashboard_date": datetime.date.today(),

        "today_summary": {
            "water": format_number(state["water"]),
            "sleep": format_number(state["sleep"]),
            "weight": format_number(state["weight"]),
            "height": format_number(state["height"]),
            "fat_percentage": format_number(state["fat_percentage"]),
        },

        "progress": {
            "water_percent": calculate_percent(state["water"], water_goal),
            "sleep_percent": calculate_percent(state["sleep"], sleep_goal),
            "body_data_percent": calculate_body_data_percent(
                state["weight"],
                state["height"],
                state["fat_percentage"],
            ),
        },

        "recent_records": recent_records,
    }


def get_state_from_facade(facade):
    daily_result = facade.get_today_results()

    return {
        "water": daily_result.water if daily_result.water is not None else 0,
        "sleep": (
            daily_result.sleep_duration
            if daily_result.sleep_duration is not None
            else 0
        ),
        "weight": daily_result.weight if daily_result.weight is not None else 0,
        "height": daily_result.height if daily_result.height is not None else 0,
        "fat_percentage": (
            daily_result.fat_mass
            if daily_result.fat_mass is not None
            else 0
        ),
    }


def daily_tracking(request):
    facade = get_facade_for_request(request)
    today_date = datetime.date.today().isoformat()

    state = get_state_from_facade(facade)

    recent_records = []

    if request.method == "POST":
        form_type = request.POST.get("form_type")

        if form_type == "water_sleep":
            state, recent_records = handle_water_sleep_form(
                request,
                facade,
                today_date,
                state,
                recent_records,
            )

        elif form_type == "body_metrics":
            state, recent_records = handle_body_metrics_form(
                request,
                facade,
                today_date,
                state,
                recent_records,
            )

        elif form_type == "medication":
            recent_records = handle_medication_form(
                request,
                facade,
                today_date,
                recent_records,
            )

    context = build_context(state, recent_records)

    return render(request, "DailyTracking/daily_tracking.html", context)