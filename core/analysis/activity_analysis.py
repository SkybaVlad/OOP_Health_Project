from datetime import datetime

from core.activity.activity_type import SpecificActivityType
from core.daily_health import HealthDaily


class ActivityAnalyzer:
    """This class provides the API that analyzes different activity metrics."""

    def __init__(self):
        self.start_time: str | None = None
        self.end_time: str | None = None
        self.list_of_activities: list[SpecificActivityType] | None = None
        self.list_of_days: list[HealthDaily] | None = None

    def load_default_values_to_initialize(
            self,
            start_time: str,
            end_time: str,
            list_of_activities: list[SpecificActivityType],
            list_of_days: list[HealthDaily],
    ):
        self.start_time = start_time
        self.end_time = end_time
        self.list_of_activities = list_of_activities
        self.list_of_days = list_of_days

    def set_period(self, start_time: str, end_time: str):
        self.start_time = start_time
        self.end_time = end_time

    def set_list_of_activities(self, list_of_activities: list[SpecificActivityType]):
        self.list_of_activities = list_of_activities

    def set_list_of_days(self, list_of_days: list[HealthDaily]):
        self.list_of_days = list_of_days

    def format_date_for_statistics(self, date_value) -> str:
        if date_value is None:
            return ""

        if hasattr(date_value, "strftime"):
            return date_value.strftime("%d.%m")

        try:
            parsed_date = datetime.strptime(str(date_value), "%Y-%m-%d").date()
            return parsed_date.strftime("%d.%m")
        except ValueError:
            return str(date_value)

    def is_workout_activity(self, activity: SpecificActivityType) -> bool:
        workout_activity_names = [
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
            "Skiing",
            "Snowboarding",
            "Rock climbing",

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

            "Hiking",
            "Kayaking",
            "Boating",
            "Exploring nature",
            "Dog walking",
        ]

        return activity.activity_name in workout_activity_names

    def get_total_time_spend_on_activity(self) -> float:
        total_time = 0.0

        if self.list_of_activities is None:
            return total_time

        for activity in self.list_of_activities:
            if not self.is_workout_activity(activity):
                continue

            total_time += activity.calculate_activity_duration_in_minutes()

        return total_time

    def get_total_burned_calories_with_activity(self):
        total_burned_calories = 0.0

        if self.list_of_activities is None:
            return total_burned_calories

        for activity in self.list_of_activities:
            if not self.is_workout_activity(activity):
                continue

            total_burned_calories += activity.burned_calories

        return total_burned_calories

    def get_count_of_days_in_period(self) -> int:
        fallback_days_count = len(self.list_of_days) if self.list_of_days is not None else 1

        if fallback_days_count <= 0:
            fallback_days_count = 1

        if self.start_time is None or self.end_time is None:
            return fallback_days_count

        try:
            start_date = datetime.strptime(self.start_time, "%Y-%m-%d").date()
            end_date = datetime.strptime(self.end_time, "%Y-%m-%d").date()
        except ValueError:
            return fallback_days_count

        count_of_days = (end_date - start_date).days + 1

        if count_of_days <= 0:
            return fallback_days_count

        return count_of_days

    def get_list_of_activities_names_that_exist_in_period(self) -> list[str]:
        lst_of_activities_names = []

        if self.list_of_activities is None:
            return lst_of_activities_names

        for activity in self.list_of_activities:
            if not self.is_workout_activity(activity):
                continue

            lst_of_activities_names.append(activity.activity_name)

        return lst_of_activities_names

    def get_list_of_activities_categories_that_exist_in_period(self) -> list[str]:
        lst_of_activities_categories = []

        if self.list_of_activities is None:
            return lst_of_activities_categories

        for activity in self.list_of_activities:
            if not self.is_workout_activity(activity):
                continue

            lst_of_activities_categories.append(activity.activity_category)

        return lst_of_activities_categories

    def get_time_spend_on_activities_categories(self):
        dict_of_activities_categories = {}

        if self.list_of_activities is None:
            return dict_of_activities_categories

        for activity in self.list_of_activities:
            if not self.is_workout_activity(activity):
                continue

            if dict_of_activities_categories.get(activity.activity_category, None) is None:
                dict_of_activities_categories[activity.activity_category] = (
                    activity.calculate_activity_duration_in_minutes()
                )
            else:
                dict_of_activities_categories[activity.activity_category] += (
                    activity.calculate_activity_duration_in_minutes()
                )

        return dict_of_activities_categories

    def get_most_popular_activity_category_and_time_spend_on_this_activity(self):
        dict_of_activities_categories = self.get_time_spend_on_activities_categories()

        if not dict_of_activities_categories:
            return "No data"

        return max(
            dict_of_activities_categories,
            key=lambda key: dict_of_activities_categories[key],
        )

    def get_most_popular_activity_name_and_time_spend_on_this_category(self):
        dict_of_activities_names = {}

        if self.list_of_activities is None:
            return "No data"

        for activity in self.list_of_activities:
            if not self.is_workout_activity(activity):
                continue

            if dict_of_activities_names.get(activity.activity_name, None) is None:
                dict_of_activities_names[activity.activity_name] = (
                    activity.calculate_activity_duration_in_minutes()
                )
            else:
                dict_of_activities_names[activity.activity_name] += (
                    activity.calculate_activity_duration_in_minutes()
                )

        if not dict_of_activities_names:
            return "No data"

        return max(
            dict_of_activities_names,
            key=lambda key: dict_of_activities_names[key],
        )

    def get_color_by_class(self, color_class: str) -> str:
        colors = {
            "green-dot": "#8AAD08",
            "purple-dot": "#514493",
            "blue-dot": "#9EC2EC",
            "gray-dot": "#BDBDBD",
            "other-dot": "#D9D9D9",
        }

        return colors.get(color_class, "#D9D9D9")

    def build_donut_gradient(self, activity_summary: list[dict]) -> str:
        if not activity_summary:
            return "conic-gradient(#D9D9D9 0deg 360deg)"

        current_degree = 0
        gradient_parts = []

        for index, activity in enumerate(activity_summary):
            percent = activity.get("percent", 0)
            color = activity.get("color", "#D9D9D9")

            if index == len(activity_summary) - 1:
                next_degree = 360
            else:
                next_degree = current_degree + percent * 3.6

            gradient_parts.append(
                f"{color} {current_degree}deg {next_degree}deg"
            )

            current_degree = next_degree

        return "conic-gradient(" + ", ".join(gradient_parts) + ")"

    def get_activity_summary(self) -> list[dict]:
        if self.list_of_activities is None:
            return []

        time_by_activity = {}

        for activity in self.list_of_activities:
            if not self.is_workout_activity(activity):
                continue

            activity_name = activity.activity_name
            activity_time = activity.calculate_activity_duration_in_minutes()

            if activity_name not in time_by_activity:
                time_by_activity[activity_name] = 0.0

            time_by_activity[activity_name] += activity_time

        total_activity_time = sum(time_by_activity.values())

        if total_activity_time <= 0:
            return []

        sorted_activities = sorted(
            time_by_activity.items(),
            key=lambda item: item[1],
            reverse=True,
        )

        main_activities = sorted_activities[:4]
        other_activities = sorted_activities[4:]

        visible_items = []

        for activity_name, activity_time in main_activities:
            visible_items.append(
                {
                    "name": activity_name,
                    "time": activity_time,
                }
            )

        if other_activities:
            other_time = sum(activity_time for _, activity_time in other_activities)

            visible_items.append(
                {
                    "name": "Other",
                    "time": other_time,
                }
            )

        color_classes = [
            "green-dot",
            "purple-dot",
            "blue-dot",
            "gray-dot",
            "other-dot",
        ]

        activity_summary = []
        used_percent = 0

        for index, item in enumerate(visible_items):
            activity_name = item["name"]
            activity_time = item["time"]

            if index < len(visible_items) - 1:
                percent = round(activity_time / total_activity_time * 100)
                used_percent += percent
            else:
                percent = 100 - used_percent

            if percent <= 0:
                continue

            if activity_name == "Other":
                color_class = "other-dot"
            else:
                color_class = color_classes[index]

            activity_summary.append(
                {
                    "name": activity_name,
                    "percent": percent,
                    "color_class": color_class,
                    "color": self.get_color_by_class(color_class),
                }
            )

        return activity_summary

    def get_result_of_analysis(self):
        if self.list_of_days is None:
            self.list_of_days = []

        if self.list_of_activities is None:
            self.list_of_activities = []

        days = []

        for day in self.list_of_days:
            days.append(
                {
                    "date": day.date_of_day,
                    "day": day.name_of_day[:3],
                    "burned_calories": round(day.burned_calories_for_day, 2),
                }
            )

        if len(self.list_of_days) == 0:
            activity_summary = []
            donut_gradient = self.build_donut_gradient(activity_summary)

            return {
                "days": [],
                "best_calories_day": "No data",
                "best_calories_date": "",
                "best_calories_value": 0,
                "lowest_calories_day": "No data",
                "lowest_calories_date": "",
                "lowest_calories_value": 0,
                "top_activity": "No data",
                "top_activity_calories": 0,
                "average_calories": 0,
                "total_steps": 0,
                "total_calories": 0,
                "activity_summary": activity_summary,
                "donut_gradient": donut_gradient,
            }

        best_day = max(
            self.list_of_days,
            key=lambda day: day.burned_calories_for_day,
        )

        active_days = [
            day for day in self.list_of_days
            if day.burned_calories_for_day > 0
        ]

        if active_days:
            lowest_day = min(
                active_days,
                key=lambda day: day.burned_calories_for_day,
            )
        else:
            lowest_day = min(
                self.list_of_days,
                key=lambda day: day.burned_calories_for_day,
            )

        total_steps = sum(day.count_of_steps_for_day for day in self.list_of_days)
        total_calories = sum(day.burned_calories_for_day for day in self.list_of_days)

        count_of_days_in_period = self.get_count_of_days_in_period()
        average_calories = round(total_calories / count_of_days_in_period, 2)

        calories_by_activity = {}

        for activity in self.list_of_activities:
            if not self.is_workout_activity(activity):
                continue

            activity_name = activity.activity_name

            if activity_name not in calories_by_activity:
                calories_by_activity[activity_name] = 0.0

            calories_by_activity[activity_name] += activity.burned_calories

        if calories_by_activity:
            top_activity = max(
                calories_by_activity,
                key=lambda activity_name: calories_by_activity[activity_name],
            )
            top_activity_calories = calories_by_activity[top_activity]
        else:
            top_activity = "No data"
            top_activity_calories = 0

        activity_summary = self.get_activity_summary()
        donut_gradient = self.build_donut_gradient(activity_summary)

        return {
            "days": days,

            "best_calories_day": best_day.name_of_day,
            "best_calories_date": self.format_date_for_statistics(best_day.date_of_day),
            "best_calories_value": round(best_day.burned_calories_for_day, 2),

            "lowest_calories_day": lowest_day.name_of_day,
            "lowest_calories_date": self.format_date_for_statistics(lowest_day.date_of_day),
            "lowest_calories_value": round(lowest_day.burned_calories_for_day, 2),

            "top_activity": top_activity,
            "top_activity_calories": round(top_activity_calories, 2),

            "average_calories": average_calories,
            "total_steps": round(total_steps),
            "total_calories": round(total_calories, 2),

            "activity_summary": activity_summary,
            "donut_gradient": donut_gradient,
        }