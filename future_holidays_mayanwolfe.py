# from Mayanwolfe Python Part 3 vod

import holidays   # all holidays and observed days
from datetime import timedelta  # for calculating +/- days

# get holidays for specific year range
us_holidays = holidays.US(years=range(1999, 2024))

# list of holidays not observed
excluded_holidays = {

}

# put remaining dates and names in a list, excluding weekend holidays
refined_holidays = {
    date: name 
    for date, name in us_holidays.items() if name not in excluded_holidays and date.weekday() not in {5, 6}
}

# final list, will add additional special days
business_week_holidays = {}
for date, name in refined_holidays.items():
    business_week_holidays[date] = name

# calculate Thanksgiving Break (always day after Thanksgiving)
for date, name in refined_holidays.items():
    if name == 'Thanksgiving':
        thanksgiving_break = date + timedelta(days=1)
        business_week_holidays[thanksgiving_break] = 'Thanksgiving Break'

# calculate Christmas Break (business day before Xmas)
for date, name in refined_holidays.items():
    if name == 'Christmas Day':
        if date.weekday() in {0,2,3}: # if Xmas on Monday, Wed, or Thur, take day off after
            christmas_break = date + timedelta(days=1)
        elif date.weekday() in {1,4}: # if Xmas on Tues, Fri, take day off before
            christmas_break = date - timedelta(days=1)
        business_week_holidays[christmas_break] = 'Christmas Break'
    if name == 'Christmas Day (observed)':
        if date.weekday() == 0: # if observed Xmas on Mon
            christmas_break = date - timedelta(days=3) # Friday prior to Xmas
        elif date.weekday() == 4: # if observed Xmas on Fri
            christmas_break = date - timedelta(days=1) # day before Xmas observed (thurs)
        business_week_holidays[christmas_break] = 'Christmas Break'

# sort complete list by date and print
for holiday_date, holiday_name in sorted(business_week_holidays.items()):
    print(holiday_date, holiday_name)