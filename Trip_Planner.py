'''
Asher Forman
9/21/20
Python Trip Planner
'''
#Part 1 Greeting Code
print("Welcome to Vacation Planner!")
customer_name = input("What is your name? ")
destination = input(f'Nice to meet you, {customer_name}. To where are you traveling? ')
print(f'Great! {destination} sounds like a great trip.')
print('*********************************')
print("\n")

#Part 2 Travel Time and Budget
def travel_time_budget():
    integer_number_of_days = int(input("How many days are you going to spend travelling? "))
    money_spent = int(input("What is your total budget for the trip in USD? "))
    currency_symbol = input("What is the currency symbol for their destination? ")
    conversion_for_money = float(input(f'How many {currency_symbol} are there in 1 USD? '))

    print("\n")
    print(f'If you are travelling for {integer_number_of_days} days, that is the same as {integer_number_of_days * 24} hours, {integer_number_of_days * 24 * 60} minutes, or {integer_number_of_days * 24 * 60 *60} seconds.')
    print(f'If you are going to spend ${money_spent} USD, that means per day you can spend up to ${round(money_spent / integer_number_of_days, 2)} USD.')
    print(f'Your total budget in {currency_symbol} is {round(conversion_for_money * money_spent, 2)} {currency_symbol}, which per day is {round((conversion_for_money * money_spent) / integer_number_of_days, 2)} {currency_symbol}.')
    print('*********************************')

#Part 3 Time Difference
def time_change():
    print("\n")
    noon = 12
    midnight = 0
    time_difference = int(input("What is the time difference, in hours, between your home and your destination? If the time is behind, use a negative symbole in front of the amount of hours. "))
    # so the time difference could be + or -
    # convert the string to a int
    int_time_difference = int(time_difference)

    difference_hrs_noon = noon + int_time_difference
    difference_hrs_midnight = midnight + int_time_difference

    # use % to get how many hours over into the next day could be + or -
    adjusted_noon = difference_hrs_noon % 24
    adjusted_midnight = difference_hrs_midnight % 24

    #For noon
    if difference_hrs_noon <= 24 and difference_hrs_noon >= 0:
        print(f'Destination time is {difference_hrs_noon}:00 from noon 12:00.')
    if difference_hrs_noon > 24:
        print (f'Destination time is {adjusted_noon}:00 hrs(s) on the next day from noon 12:00.')
    if difference_hrs_noon < 0:
        print(f'Desination time is {adjusted_noon}:00, in the previous day from noon 12:00.')

    #For Midnight
    if difference_hrs_midnight <= 24 and difference_hrs_midnight >= 0:
        print(f'Destination time is {difference_hrs_midnight}:00 from midnight 0:00.')
    if difference_hrs_midnight > 24:
        print (f'Destination time is {adjusted_midnight}:00 hrs(s) on the next day from midnight 0:00.')
    if difference_hrs_midnight < 0:
        print(f'Desination time is {adjusted_midnight}:00, in the previous day from midnight 0:00.')
    print('*********************************')
#Part 4 Country Area
def country_area():
    print("\n")
    size_country = int(input('What is the square area of your destination country in KM2? '))
    print(f'In miles2, that is {round(size_country * 0.386102, 2)}')
    print('*********************************')


travel_time_budget()
time_change()
country_area()
