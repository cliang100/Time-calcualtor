def add_time(start, duration, day=None):

    # List for the days of the week, initialize days_passed
    days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    days_passed = 0

    # Split start (i.e. '3:00 PM') into the 3:00 and PM, and time into hours and minutes
    start_time, period = start.split()
    start_hours, start_minutes = map(int, start_time.split(':'))

    # Split up duration into hours and minutes
    duration_hours, duration_minutes = map(int, duration.split(':'))

    # Add duration to start
    start_hours += duration_hours
    start_minutes += duration_minutes

    # Minutes overflow
    if start_minutes >= 60:
        start_hours += start_minutes // 60
        start_minutes %= 60

    # Determine AM/PM, hours overflow, and days_passed increments
    if start_hours >= 12:
        if period == 'AM':
            period = 'PM'
            if duration_hours == 24:
                period = 'AM'
                days_passed += 1
        elif period == 'PM':
            period = 'AM'
            days_passed += (duration_hours // 24) + 1
        start_hours %= 12
        if start_hours == 0:
            start_hours = 12

    # Calculating which day it is (if day is called)
    if day:
        day = day.lower()

        if day in [d.lower() for d in days_of_the_week]:
            day_index = [d.lower() for d in days_of_the_week].index(day)
            final_day_index = (day_index + days_passed) % 7
            day = days_of_the_week[final_day_index]

    # Messages for days passed
    if days_passed == 1:
        days_message = '(next day)'
    elif days_passed > 1:
        days_message = f'({days_passed} days later)'
    else:
        days_message = ''

    # Format new_time
    new_time = f'{start_hours}:{start_minutes:02} {period}'
    if day:
        new_time += f', {day}'
    if days_message:
        new_time += f' {days_message}'
    return new_time
    
if __name__ == '__main__':
    print(add_time('8:16 PM', '466:02', 'tUeSday'))
    # Returns: '6:18 AM, Monday (20 days later)'