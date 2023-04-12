import sys
from dateutil.parser import parse


def is_leap_year(year):
  return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def compute_date_number(year, month, day):
  num_days = 0

  for y in range(1900, year):
    num_days += 366 if is_leap_year(y) else 365

  for m in range(1, month):
    num_days += 30 if m in [4, 6, 9, 11] else 0

    num_days += 31 if m in [1, 3, 5, 7, 8, 10, 12] else 0

    if m == 2:
      num_days += 29 if is_leap_year(year) else 28

  num_days += day

  # subtract 1 to have 1900-1-1 indexed as 0
  return num_days - 1


# monday
first_date = [1900, 1, 1]

def count_sundays(start_date: str, end_date: str):
  start_year, start_month, start_day = [int(part) for part in start_date.split('-')]
  end_year, end_month, end_day = [int(part) for part in end_date.split('-')]
  start_number = compute_date_number(start_year, start_month, start_day)
  end_number = compute_date_number(end_year, end_month, end_day)


def compute(start: str, end: str):
  start_date = parse(start).date()
  end_date = parse(end).date()

def run():
  args = sys.argv
  default_start_date = '1900-1-1'
  default_end_date = '2000-12-31'
  if not args:
    return compute(default_start_date, default_end_date)
  if len(args) == 1:
    return compute(default_start_date, args[1])

  return compute(args[0], args[1])


if __name__ == "__main__":
    result = run()
    print('Answer:', result)