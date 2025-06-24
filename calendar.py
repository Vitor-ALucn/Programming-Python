import calendar

def display_calendar():

    year = int(input("Enter the year: "))
    month = int(input("Enter the month (1-12): "))

    cal = calendar.TextCalendar(calendar.SUNDAY)

    month_calendar = cal.formatmonth(year, month)
    print(month_calendar)

display_calendar()

# This code uses the calendar module to display a text-based calendar for a specified month and year.
# It prompts the user to input a year and a month, then generates and prints the calendar
# for that month starting on Sunday.
# The calendar module provides useful functions for working with dates and calendars in Python.
# This code is useful for applications that require displaying or working with calendar data,
# such as scheduling applications, event planners, or educational tools.
# The calendar module is part of the standard Python library, making it easy to use without
# requiring additional installations.