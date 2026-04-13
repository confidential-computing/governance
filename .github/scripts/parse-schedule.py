#!/usr/bin/env python3
"""
Parse the TAC chair rotation schedule from TAC/chair-rotation.md.

Reads the "2026 Meeting Schedule" table and returns meeting info as JSON.
Used by GitHub Actions workflows for reminders and meeting prep.
"""

import json
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path


def parse_schedule(path: str = "TAC/meeting-schedule.md") -> list[dict]:
    """Parse the meeting schedule table from chair-rotation.md."""
    content = Path(path).read_text()

    # Find the 2026 Meeting Schedule section
    schedule_section = content.split("## 2026 Meeting Schedule")[-1]

    meetings = []
    for line in schedule_section.strip().splitlines():
        # Match table rows with 3 columns:
        # | Date | Rotating Chair | CCC Project Topic |
        match = re.match(
            r"\|\s*(\d{4}-\d{2}-\d{2})\s*\|"  # Date
            r"\s*(.*?)\s*\|"  # Rotating Chair
            r"\s*(.*?)\s*\|",  # CCC Project Topic
            line,
        )
        if match:
            date_str, chair, project_topic = match.groups()

            # Skip "no meeting" rows
            if "no meeting" in chair.lower():
                continue

            # Clean up chair field — skip TBD / placeholder entries
            chair = chair.strip()
            if "TBD" in chair or "<!--" in chair:
                chair = ""

            meetings.append(
                {
                    "date": date_str,
                    "chair": chair,
                    "project_topic": project_topic.strip(),
                }
            )

    return meetings


def find_next_meeting(meetings: list[dict], reference_date: datetime) -> dict | None:
    """Find the next upcoming meeting on or after reference_date."""
    for m in meetings:
        meeting_date = datetime.strptime(m["date"], "%Y-%m-%d")
        if meeting_date >= reference_date:
            return m
    return None


def find_meeting_on(meetings: list[dict], target_date: str) -> dict | None:
    """Find the meeting scheduled for a specific date."""
    for m in meetings:
        if m["date"] == target_date:
            return m
    return None


def get_next_meeting_date(meetings: list[dict], after_date: str) -> str | None:
    """Find the meeting date after the given date."""
    found_current = False
    for m in meetings:
        if found_current:
            return m["date"]
        if m["date"] == after_date:
            found_current = True
    return None


if __name__ == "__main__":
    action = sys.argv[1] if len(sys.argv) > 1 else "next"
    today = datetime.now()

    meetings = parse_schedule()

    if action == "next":
        meeting = find_next_meeting(meetings, today)
        if meeting:
            meeting["next_date"] = get_next_meeting_date(meetings, meeting["date"]) or ""
            print(json.dumps(meeting))
        else:
            print(json.dumps({"error": "No upcoming meetings found"}))

    elif action == "this-week":
        # Check if there's a meeting within the next 14 days.
        # With the workflow running every Friday and meetings every 2 weeks,
        # this ensures the chair gets two Friday reminders per meeting.
        week_end = today + timedelta(days=14)
        meeting = find_next_meeting(meetings, today)
        if meeting:
            meeting_date = datetime.strptime(meeting["date"], "%Y-%m-%d")
            if meeting_date <= week_end:
                meeting["next_date"] = (
                    get_next_meeting_date(meetings, meeting["date"]) or ""
                )
                meeting["days_until"] = (meeting_date - today).days
                print(json.dumps(meeting))
            else:
                print(json.dumps({"error": "No meeting this week"}))
        else:
            print(json.dumps({"error": "No upcoming meetings found"}))

    elif action == "all":
        print(json.dumps(meetings, indent=2))

    else:
        print(f"Unknown action: {action}", file=sys.stderr)
        sys.exit(1)
