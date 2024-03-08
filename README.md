---

# Time Calculator

This Python script, `add_time`, calculates the time after adding a specified duration to a given starting time. It does so without relying on any external Python libraries.

## How It Works

### Input Parameters

The function `add_time` takes three parameters:

1. `start`: The starting time in the format "HH:MM AM/PM".
2. `duration`: The duration to be added to the starting time, provided in the format "HH:MM".
3. `day` (optional): The starting day of the week, specified as a string (e.g., "Monday", "Tuesday", etc.). If not provided, the function will only calculate the time without considering the day.

### Implementation

1. **Parsing Input**: The `start` and `duration` strings are split into hours, minutes, and periods (AM/PM) using Python's string manipulation techniques.

2. **Adding Duration**: The hours and minutes from the `duration` are added to the `start` time. If the sum of minutes exceeds 60, it is accounted for by adjusting the hours accordingly.

3. **Handling AM/PM and Overflow**: If the resulting hour after adding duration is 12 or greater, the period (AM/PM) is adjusted accordingly. Additionally, if the duration exceeds 24 hours, it adjusts the period and increments the `days_passed` counter.

4. **Calculating Day**: If the `day` parameter is provided, the function calculates which day it will be after adding the specified duration. It handles both the case where the provided day is specified in lowercase and where it's not. In other words, it is case insensitive.

5. **Formatting Output**: The function constructs the new time string in the format "HH:MM AM/PM". If the `day` parameter was provided or if there are any days passed, it appends the respective day information to the output.

6. **Returning Output**: Finally, the function returns the calculated new time string.

## Example Usage

```python
print(add_time('8:16 PM', '466:02', 'tUeSday'))
# Returns: '6:18 AM, Monday (20 days later)'
```

In this example:
- The starting time is '8:16 PM'.
- The duration to be added is '466:02' (466 hours and 2 minutes).
- The starting day of the week is 'Tuesday'.
- The output indicates that the resulting time is '6:18 AM' on the following 'Monday', with a total of '20 days later'.
