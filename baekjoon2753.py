year=int(input())
def check_leap_year(year):
    is_leap_year = 0
    if year % 4 == 0:
        if year % 400 == 0 or year % 100 != 0:
            is_leap_year = 1
    return is_leap_year
print(check_leap_year(year))
