import datetime
from random import random
from typing import Any

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

import sys

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from core import MainFacade
from core.dto_objects import DailyObjectDTO

import core


def create_facade_obj(user_obj: core.User) -> MainFacade:
    facade = core.create_and_configure_facade_for_start(user_obj)
    return facade


from random import Random
import datetime


def get_demo_activity_calories(
    activity_category: str,
    random_generator: Random,
) -> int:
    if activity_category in ["Sport", "Fitness", "Training"]:
        return random_generator.randint(250, 700)

    if activity_category in ["Travel", "Nature"]:
        return random_generator.randint(120, 450)

    if activity_category in ["Health"]:
        return random_generator.randint(80, 260)

    if activity_category in ["Leisure", "Relaxation", "Meditation"]:
        return random_generator.randint(30, 160)

    if activity_category in ["Work", "Study", "Learning"]:
        return random_generator.randint(40, 180)

    if activity_category in [
        "Hobby",
        "Art",
        "Music",
        "Game",
        "Creativity",
        "Entertainment",
        "Social",
        "Volunteering",
    ]:
        return random_generator.randint(40, 230)

    return random_generator.randint(50, 250)


def add_demo_data_to_test_the_system(facade: MainFacade) -> None:
    random_generator = Random(42)

    today = datetime.date.today()
    start_day = today - datetime.timedelta(days=60)

    facade.set_water_goal(2.5)
    facade.set_step_goal(11000)
    facade.set_consumed_calories_goal(2500)

    activity_variants_by_category = {
        "Sport": [
            "Football",
            "Basketball",
            "Volleyball",
            "Tennis",
            "Table tennis",
            "Swimming",
            "Boxing",
            "Karate",
            "Badminton",
            "Frisbee",
            "Paintball",
            "Laser tag",
            "Skiing",
            "Snowboarding",
            "Rock climbing",
        ],
        "Fitness": [
            "Walking",
            "Running",
            "Yoga",
            "Cycling",
            "Gym workout",
            "Aerobics",
            "Stretching",
            "CrossFit",
            "Pilates",
            "Jump rope",
            "Gymnastics",
            "Fitness",
            "Nordic walking",
            "Morning exercise",
            "Home workout",
        ],
        "Leisure": [
            "Walking",
            "Reading",
            "Board games",
            "Watching movies",
            "Watching TV series",
            "Puzzle solving",
            "Sudoku solving",
            "Lego building",
            "City walking tour",
            "Shopping",
        ],
        "Travel": [
            "Traveling",
            "Hiking",
            "Camping",
            "Boating",
            "Kayaking",
            "Museum visiting",
            "City walking tour",
            "Exploring nature",
        ],
        "Work": [
            "Programming",
            "Project work",
            "Public speaking practice",
            "Time management practice",
            "House renovation",
            "Car washing",
            "DIY projects",
            "Day planning",
        ],
        "Study": [
            "Reading",
            "Writing",
            "Learning languages",
            "Online learning",
            "Study session",
            "Project work",
            "Reading news",
        ],
        "Hobby": [
            "Chess",
            "Checkers",
            "Drawing",
            "Reading",
            "Writing",
            "Cooking",
            "Photography",
            "Video recording",
            "Gardening",
            "Fishing",
            "Hunting",
            "Boating",
            "Kayaking",
            "Skateboarding",
            "Handcrafting",
            "Knitting",
            "Embroidery",
            "Origami",
            "Calligraphy",
            "3D printing",
            "Modeling",
            "Lego building",
            "RC car driving",
            "Drone flying",
            "Birdwatching",
            "Stargazing",
        ],
        "Art": [
            "Drawing",
            "Photography",
            "Video recording",
            "Creative writing",
            "Calligraphy",
            "Origami",
            "Handcrafting",
            "Embroidery",
            "Modeling",
        ],
        "Music": [
            "Playing guitar",
            "Playing piano",
            "Singing",
            "Listening to music",
            "Podcasting",
        ],
        "Game": [
            "Chess",
            "Checkers",
            "Board games",
            "Playing video games",
            "Puzzle solving",
            "Sudoku solving",
            "Lego building",
            "RC car driving",
            "Drone flying",
        ],
        "Health": [
            "Yoga",
            "Stretching",
            "Breathing exercises",
            "Dog walking",
            "Sauna",
            "Massage",
            "Morning exercise",
            "Mindfulness practice",
        ],
        "Social": [
            "Talking with friends",
            "Family time",
            "Volunteering",
            "Public speaking practice",
        ],
        "Nature": [
            "Walking",
            "Hiking",
            "Gardening",
            "Fishing",
            "Camping",
            "Birdwatching",
            "Stargazing",
            "Exploring nature",
            "Dog walking",
        ],
        "Relaxation": [
            "Meditation",
            "Relaxation",
            "Napping",
            "Mindfulness practice",
            "Listening to music",
            "Watching movies",
            "Watching TV series",
            "Sauna",
            "Massage",
        ],
        "Meditation": [
            "Meditation",
            "Mindfulness practice",
            "Breathing exercises",
            "Journaling",
        ],
        "Learning": [
            "Learning languages",
            "Online learning",
            "Reading",
            "Study session",
            "Reading news",
            "Self-development",
            "Goal setting",
            "Public speaking practice",
            "Time management practice",
        ],
        "Training": [
            "Running",
            "Gym workout",
            "CrossFit",
            "Boxing",
            "Karate",
            "Jump rope",
            "Morning exercise",
            "Home workout",
            "Public speaking practice",
            "Time management practice",
        ],
        "Creativity": [
            "Drawing",
            "Writing",
            "Creative writing",
            "Blogging",
            "Podcasting",
            "Brainstorming",
            "Photography",
            "Video recording",
            "Calligraphy",
            "3D printing",
            "Modeling",
            "DIY projects",
        ],
        "Entertainment": [
            "Watching movies",
            "Watching TV series",
            "Playing video games",
            "Board games",
            "Listening to music",
            "Podcasting",
            "RC car driving",
            "Drone flying",
            "Laser tag",
            "Paintball",
        ],
        "Volunteering": [
            "Volunteering",
            "Dog walking",
            "Family time",
            "Talking with friends",
        ],
    }

    for day_index in range(61):
        current_date = start_day + datetime.timedelta(days=day_index)
        current_date_str = current_date.isoformat()

        weekday = current_date.weekday()

        if weekday in [5, 6]:
            steps = random_generator.randint(3500, 9500)
            burned_calories = random_generator.randint(150, 450)
            consumed_calories = random_generator.randint(2000, 3000)
            sleep = round(random_generator.uniform(7.0, 9.3), 1)
            water = round(random_generator.uniform(1.8, 3.3), 1)
        else:
            steps = random_generator.randint(5500, 14500)
            burned_calories = random_generator.randint(220, 680)
            consumed_calories = random_generator.randint(1800, 2750)
            sleep = round(random_generator.uniform(5.8, 8.2), 1)
            water = round(random_generator.uniform(1.5, 3.0), 1)

        base_weight = 87.0
        weight_trend = -0.035 * day_index
        weight_noise = random_generator.uniform(-0.7, 0.7)
        weight = round(base_weight + weight_trend + weight_noise, 1)

        height = 188.0

        base_fat_percentage = 14.0
        fat_trend = -0.025 * day_index
        fat_noise = random_generator.uniform(-0.4, 0.4)
        fat_percentage = round(base_fat_percentage + fat_trend + fat_noise, 1)

        facade.add_burned_calories(burned_calories, current_date_str)
        facade.add_water(water, current_date_str)
        facade.add_sleep(sleep, current_date_str)
        facade.add_count_of_steps(steps, current_date_str)
        facade.add_fat_percentage(fat_percentage, current_date_str)
        facade.add_height(height, current_date_str)
        facade.add_weight(weight, current_date_str)
        facade.add_consumed_calories(consumed_calories, current_date_str)

        count_of_activities_for_day = random_generator.choice([0, 1, 1, 1, 2])

        for _ in range(count_of_activities_for_day):
            activity_category = random_generator.choice(
                list(activity_variants_by_category.keys())
            )

            activity_name = random_generator.choice(
                activity_variants_by_category[activity_category]
            )

            start_hour = random_generator.randint(7, 20)
            start_minute = random_generator.choice([0, 10, 20, 30, 40, 50])

            duration_minutes = random_generator.choice([20, 30, 40, 45, 60, 75, 90])

            start_time = datetime.time(start_hour, start_minute)

            end_datetime = datetime.datetime.combine(current_date, start_time)
            end_datetime += datetime.timedelta(minutes=duration_minutes)
            end_time = end_datetime.time()

            activity_calories = get_demo_activity_calories(
                activity_category,
                random_generator,
            )

            activity_obj = core.facade_logic.facade_api.SpecificActivityType(
                activity_category,
                activity_name,
                activity_calories,
                start_time.strftime("%H:%M"),
                end_time.strftime("%H:%M"),
            )

            facade.add_activity(activity_obj, current_date_str)

        if day_index % 7 == 0:
            facade.set_water_goal(round(random_generator.uniform(2.2, 3.0), 1))

            facade.set_step_goal(
                random_generator.choice([8000, 9000, 10000, 11000, 12000])
            )

            facade.set_consumed_calories_goal(
                random_generator.choice([2200, 2400, 2500, 2700])
            )


# get daily results
def get_daily_health_overview(facade):
    daily_result = facade.get_today_results()
    return daily_result


# get weekly results
def get_weekly_health_overview(facade: MainFacade) -> dict[str, Any]:

    # get time
    today_date: datetime.date = datetime.date.today()
    date_of_monday: datetime.date = today_date - datetime.timedelta(
        days=today_date.weekday()
    )

    print(today_date)
    print(date_of_monday)

    weekly_result = facade.get_result_of_analyze_some_period(
        date_of_monday.isoformat(), today_date.isoformat()
    )

    print(weekly_result)

    return weekly_result


def get_metrics_info_for_left_side_dashboard_metrics(daily_result):

    return {
        "UserBodyMetrics": {
            "Height": f"{round(daily_result.height, 2)} cm",
            "Weight": f"{round(daily_result.weight, 2)} kg",
            "BMI": round(daily_result.body_mass_index, 2),
            "BMR": f"{round(daily_result.basal_metabolic_rate, 2)} kcal",
            "LBMI": round(daily_result.lean_body_mass_index, 2),
            "Fat": f"{round(daily_result.fat_mass, 2)} %",
        },
        "Activities": daily_result.activity,
        "Medications": daily_result.medication,
        "Meals": daily_result.meal,
    }


def get_information_for_graph(list_of_values: dict):
    max_value = max(list_of_values)

    info = [1 if value == 0 else value / max_value * 100 for value in list_of_values]

    # info = {
    #     key: (
    #         1
    #         if dict_of_dates_and_values[key] == 0
    #         else dict_of_dates_and_values[key] / max_value * 100
    #     )
    #     for key in dict_of_dates_and_values
    # }

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
        {
            "metric_name": "Activity time",
            "today_metric_value": daily_results.activity_time,
            "weekly_metric_value": round(weekly_result["total_activity_time"], 2),
            "metric_goal_value": daily_results.activity_time_goal,
            "dict_of_dates_and_percentage_for_graph": get_information_for_graph(
                weekly_result["activity_time_value_for_each_day"]
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
