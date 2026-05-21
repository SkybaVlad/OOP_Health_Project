import datetime

from django.shortcuts import render


def daily_tracking(request):
    context = {
        "dashboard_date": datetime.date.today(),
        "today_summary": {
            "water": 1.5,
            "sleep": 7.5,
            "weight": 87,
            "fat_percentage": 14,
        },
        "progress": {
            "water_percent": 60,
            "sleep_percent": 94,
            "body_data_percent": 100,
        },
        "recent_records": [
            {
                "title": "Water added",
                "time": "Today",
                "value": "1.5 L",
            },
            {
                "title": "Sleep added",
                "time": "Today",
                "value": "7.5 h",
            },
            {
                "title": "Weight updated",
                "time": "Today",
                "value": "87 kg",
            },
        ],
    }

    return render(request, "DailyTracking/daily_tracking.html", context)
