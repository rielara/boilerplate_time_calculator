def resolve_periods_and_days(added_hours, current_period):
  half_days_passed = 0
  days_passed = 0
  
  if added_hours >= 12:
    half_days_passed = int(added_hours / 12)

    days_passed = int(half_days_passed / 2)

    if half_days_passed % 2 == 1:
      if current_period == "PM":
        days_passed += 1
        current_period = "AM"
      else:
        current_period = "PM"

  return (current_period, days_passed, half_days_passed)


def format_result(result_hours, result_minutes, current_period, day, days_passed):
  days_of_the_week = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
  ]

  result = f"{result_hours}:{str(result_minutes).rjust(2, '0')} {current_period}"
  

  if day:
    current_day_index = days_of_the_week.index(day.capitalize()) + days_passed
    day = days_of_the_week[current_day_index % 7]
    result = result + f", {day}"

  if (days_passed > 0):
    if (days_passed == 1):
      result = result + " (next day)"
    else:
      result = result + f" ({days_passed} days later)"

  return result


def parse_times(start, duration):
  start_hour = int(start.split(":")[0])
  start_minutes = int(start.split(":")[1].split(" ")[0])
  duration_hour = int(duration.split(":")[0])
  duration_minutes = int(duration.split(":")[1])

  current_period = str(start.split(" ")[1])

  return (start_hour, start_minutes, duration_hour, duration_minutes, current_period)


def calculate_new_times(start_hour, start_minutes, duration_hour, duration_minutes):
  added_hours = start_hour + duration_hour
  added_minutes = start_minutes + duration_minutes

  added_hours += int(added_minutes / 60)

  return (added_hours, added_minutes)


def calculate_result(added_hours, added_minutes):
  result_hours = added_hours % 12
  if result_hours == 0:
    result_hours = 12

  result_minutes = added_minutes % 60

  return (result_hours, result_minutes)


def add_time(start, duration, day = None):
  (start_hour, start_minutes, duration_hour, duration_minutes, current_period) = parse_times(start, duration)

  (added_hours, added_minutes) = calculate_new_times(start_hour, start_minutes, duration_hour, duration_minutes)
  
  (current_period, days_passed, half_days_passed) = resolve_periods_and_days(added_hours, current_period)

  (result_hours, result_minutes) = calculate_result(added_hours, added_minutes)

  return format_result(result_hours, result_minutes, current_period, day, days_passed)