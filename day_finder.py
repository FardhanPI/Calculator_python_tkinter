
def function():
    date = int(input("Enter the date or day of the month (1-31) : "))
    month_number = int(input("Enter the number of month (1-12) : "))
    year = int(input("Enter the year (2000-2099) : "))
    month_sp = 0

    if (month_number == 1):
        month_sp = 13
    elif (month_number == 2):
        month_sp = 14
    else:
        month_sp = month_number

    year_sp = year % 100
    J = year // 100

    day_sp = (date + ((13 * (month_sp + 1)) / 5) + year_sp + (year_sp / 4) + (J / 4) - (2 * J)) % 7

    day = ""
    if (int(day_sp) == 0):
        day = "The day of date you provided is 'Saturday'"
    elif (int(day_sp) == 1):
        day = "The day of date you provided is 'Sunday'"
    elif (int(day_sp) == 2):
        day = "The day of date you provided is 'Monday'"
    elif (int(day_sp) == 3):
        day = "The day of date you provided is 'Tuesaday'"
    elif (int(day_sp) == 4):
        day = "The day of date you provided is 'Wednesday'"
    elif (int(day_sp) == 5):
        day = "The day of date you provided is 'Thursday'"
    elif (int(day_sp) == 6):
        day = "The day of date you provided is 'Friday'"
    else:
        print("Please provide correct information as given instrucations")

    print("")
    print(day)
    print("")
    check=int(input("Enter '1' to coutinue : "))
    if(check==1):
        function()
    print("")



function()








