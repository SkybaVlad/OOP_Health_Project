import datetime
from typing import Any

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

import sys

from core import MainFacade
from core.dto_objects import DailyObjectDTO

import core


def create_facade_obj(user_obj: core.User) -> MainFacade:
    facade = core.create_and_configure_facade_for_start(user_obj)
    return facade


def add_demo_data_to_test_the_system(facade: MainFacade) -> None:
    facade.add_burned_calories(200.0, "2026-05-17")
    facade.add_water(1.5, "2026-05-17")
    facade.add_sleep(7.5, "2026-05-17")
    facade.add_count_of_steps(9000, "2026-05-17")
    facade.add_fat_percentage(10.0, "2026-05-17")
    facade.add_height(188.0, "2026-05-17")
    facade.add_weight(87.0, "2026-05-17")
    facade.set_water_goal(2.5)
    facade.set_step_goal(11000)
    facade.set_consumed_calories_goal(2500)
    facade.add_consumed_calories(1111, "2026-05-17")

    facade.add_burned_calories(22.0, "2026-05-15")
    facade.add_water(1.5, "2026-05-15")
    facade.add_sleep(7.2, "2026-05-15")
    facade.add_count_of_steps(900, "2026-05-15")
    facade.add_fat_percentage(10.0, "2026-05-15")
    facade.add_height(178.0, "2026-05-15")
    facade.add_weight(87.0, "2026-05-15")
    facade.add_consumed_calories(555, "2026-05-15")

    facade.set_water_goal(2.5)
    facade.set_step_goal(11000)
    facade.set_consumed_calories_goal(1000)

    facade.add_burned_calories(22.0, "2026-05-13")
    facade.add_water(1.5, "2026-05-13")
    facade.add_sleep(5.2, "2026-05-13")
    facade.add_count_of_steps(7000, "2026-05-13")
    facade.add_fat_percentage(10.0, "2026-05-13")
    facade.add_height(198.0, "2026-05-13")
    facade.add_weight(77.0, "2026-05-13")
    facade.add_consumed_calories(888, "2026-05-13")

    facade.set_water_goal(2.5)
    facade.set_step_goal(11000)

    facade.add_burned_calories(22.0, "2026-05-14")
    facade.add_water(1.5, "2026-05-14")
    facade.add_sleep(5.2, "2026-05-14")
    facade.add_count_of_steps(7000, "2026-05-14")
    facade.add_fat_percentage(10.0, "2026-05-14")
    facade.add_height(198.0, "2026-05-14")
    facade.add_weight(77.0, "2026-05-14")
    facade.add_consumed_calories(222, "2026-05-14")

    facade.set_water_goal(2.5)
    facade.set_step_goal(7000)
    facade.set_consumed_calories_goal(700)

    facade.add_burned_calories(400, "2026-05-12")
    facade.add_water(3, "2026-05-12")
    facade.add_sleep(9, "2026-05-12")
    facade.add_count_of_steps(1200, "2026-05-12")
    facade.add_fat_percentage(10.0, "2026-05-12")
    facade.add_height(190.0, "2026-05-12")
    facade.add_weight(77.0, "2026-05-12")
    facade.add_consumed_calories(666, "2026-05-12")

    facade.set_water_goal(2.5)
    facade.set_step_goal(7000)
    facade.set_consumed_calories_goal(300)

    facade.add_burned_calories(195.0, "2026-05-06")
    facade.add_water(2, "2026-05-16")
    facade.add_sleep(5.2, "2026-05-16")
    facade.add_count_of_steps(1800, "2026-05-16")
    facade.add_fat_percentage(9.0, "2026-05-16")
    facade.add_height(192.0, "2026-05-16")
    facade.add_weight(82.0, "2026-05-16")
    facade.set_water_goal(2.5)
    facade.set_step_goal(11000)
    facade.set_consumed_calories_goal(500)

    activity_obj = core.facade_logic.facade_api.SpecificActivityType(
        "Sport", "Football", 500, "14:20", "15:30"
    )
    facade.add_activity(activity_obj, "2026-05-10")
    activity_obj = core.facade_logic.facade_api.SpecificActivityType(
        "Sport", "Volleyball", 500, "14:20", "15:30"
    )
    facade.add_activity(activity_obj, "2026-05-10")
    facade.add_count_of_steps(1000, "2026-05-10")
    activity_obj = core.facade_logic.facade_api.SpecificActivityType(
        "Sport", "Swimming", 500, "14:20", "15:30"
    )
    facade.add_activity(activity_obj, "2026-05-10")


# get daily results
def get_daily_health_overview(facade):
    daily_result = facade.get_today_results()
    return daily_result


# get weekly results
def get_weekly_health_overview(facade: MainFacade) -> dict[str, Any]:

    # get time
    today_date: datetime.date = datetime.date.today()
    one_week_ago_date: datetime.date = today_date - datetime.timedelta(
        days=today_date.weekday()
    )

    weekly_result = facade.get_result_of_analyze_some_period(
        one_week_ago_date.isoformat(), today_date.isoformat()
    )

    return weekly_result


def get_metrics_info_for_left_side_dashboard_metrics(daily_result):

    return {
        "UserBodyMetrics": {
            "Height": daily_result.height,
            "Weight": daily_result.weight,
            "BMI": daily_result.body_mass_index,
            "BMR": daily_result.basal_metabolic_rate,
            "LBMI": daily_result.lean_body_mass_index,
            "Fat": daily_result.fat_mass,
        },
        "Activities": daily_result.activity,
        "Medications": daily_result.medication,
        "Meals": daily_result.meal,
    }


def get_information_for_graph(dict_of_dates_and_values: dict):
    max_value = max(dict_of_dates_and_values.values())

    info = {
        key: (
            1
            if dict_of_dates_and_values[key] == 0
            else dict_of_dates_and_values[key] / max_value * 100
        )
        for key in dict_of_dates_and_values
    }

    return info


def get_metrics_info_for_right_side_dashboard_metrics(daily_results, weekly_result):
    # this function process info and return list[dict] where each dict contain info about metric

    list_of_metrics_info = [
        {
            "metric_name": "Burned calories",
            "today_metric_value": round(daily_results.burned_calories, 2),
            "weekly_metric_value": round(weekly_result["total_burned_calories"], 2),
            "metric_goal_value": daily_results.burned_calories_goal,
            "dict_of_dates_and_percentage_for_graph": get_information_for_graph(
                weekly_result["burned_calories_value_for_each_day"]
            ),
        },
        {
            "metric_name": "Consumed calories",
            "today_metric_value": daily_results.consumed_calories,
            "weekly_metric_value": round(weekly_result["total_consumed_calories"], 2),
            "metric_goal_value": daily_results.consumed_calories_goal,
            "dict_of_dates_and_percentage_for_graph": get_information_for_graph(
                weekly_result["consumed_calories_value_for_each_day"]
            ),
        },
        {
            "metric_name": "Steps",
            "today_metric_value": daily_results.steps,
            "weekly_metric_value": round(weekly_result["total_steps"], 2),
            "metric_goal_value": daily_results.step_goal,
            "dict_of_dates_and_percentage_for_graph": get_information_for_graph(
                weekly_result["steps_value_for_each_day"]
            ),
        },
        {
            "metric_name": "Water",
            "today_metric_value": daily_results.water,
            "weekly_metric_value": round(weekly_result["total_drunk_water"], 2),
            "metric_goal_value": daily_results.water_goal,
            "dict_of_dates_and_percentage_for_graph": get_information_for_graph(
                weekly_result["drunk_water_value_for_each_day"]
            ),
        },
        {
            "metric_name": "Sleep",
            "today_metric_value": daily_results.sleep_duration,
            "weekly_metric_value": round(weekly_result["total_sleep_hours"], 2),
            "metric_goal_value": daily_results.sleep_duration_goal,
            "dict_of_dates_and_percentage_for_graph": get_information_for_graph(
                weekly_result["sleep_duration_value_for_each_day"]
            ),
        },
    ]

    return list_of_metrics_info


def create_user_obj(request_data) -> core.User:
    name = "Maks"  # request_data["username"]
    surname = "Skyba"
    age = 18
    sex = "Male"
    user = core.User(name=name, surname=surname, age=age, sex=sex)
    return user


# if user is not unauthenticated -> redirect to the settings.LOGIN_URL
@login_required
def health_overview(request: HttpRequest) -> HttpResponse:

    print(request.user)

    user = create_user_obj(request.user)

    facade = create_facade_obj(user)

    add_demo_data_to_test_the_system(facade)

    daily_results = get_daily_health_overview(facade)
    weekly_results = get_weekly_health_overview(facade)

    # get analysis result
    metrics_info_for_right_side_dashboard = (
        get_metrics_info_for_right_side_dashboard_metrics(daily_results, weekly_results)
    )

    # get data for left-side part of html
    metrics_info_for_left_side_dashboard: dict = (
        get_metrics_info_for_left_side_dashboard_metrics(daily_results)
    )

    return render(
        request,
        "healthoverview/health_overview.html",
        {
            "dashboard_date": datetime.date.today(),
            "user_data": user,
            "left_side_metrics": metrics_info_for_left_side_dashboard[
                "UserBodyMetrics"
            ],
            "medication": metrics_info_for_left_side_dashboard["Medications"],
            "activity": metrics_info_for_left_side_dashboard["Activities"],
            "meal": metrics_info_for_left_side_dashboard["Meals"],
            "right_side_metrics": metrics_info_for_right_side_dashboard,
        },
    )
