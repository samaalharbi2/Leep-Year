## Day 10 - Section 10: Beginner - Leep Year

def is_leap_year(year):
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # Check if the year is divisible by 100
        if year % 100 == 0:
            # Check if the year is divisible by 400
            if year % 400 == 0:
                return True  # It's a leap year
            else:
                return False  # Not a leap year
        else:
            return True  # It's a leap year
    else:
        return False  # Not a leap year

# Call your function with hard-coded values
print(is_leap_year(2400))  # Example Return 1: True
print(is_leap_year(1989))  # Example Return 2: False


