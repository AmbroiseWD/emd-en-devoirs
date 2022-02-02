from datetime import date


def is_it_xmas():
    today = date.today()
    day = today.day
    month = today.month
    print(f"[code] I think that now is: {day}/{month}")
    it_is_xmas = day == 23 and month == 12
    return it_is_xmas
