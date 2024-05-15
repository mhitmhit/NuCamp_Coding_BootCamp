inches_snow = {"Monday": 2, "Tuesday": 4, "Wednesday": 5}

def print_total_snowfall(snow_calendar):
    total_inches = 0
    for inches in snow_calendar.values():
        total_inches = total_inches + inches
    print("Total snowfall inches:", total_inches)

print_total_snowfall(inches_snow)

thrusday_snow_fall = input("How many inches of snow fell on Thrusday? ")

inches_snow["Thursday"] = int(thrusday_snow_fall)

print_total_snowfall(inches_snow)
