'''
Asher Forman
9/21/20
Python Trip Planner
'''
#Greeting Code
print("Welcome to Vacation Planner!")
customer_name = input("What is your name? ")
destination = input(f'Nice to meet you, {customer_name}. To where are you traveling? ')
print(f'Great! {destination} sounds like a great trip.')
print("\n")

#
def days_money_currency():
    integer_number_of_days = int(input("How many days are you going to spend travelling? "))
    money_spent_input = int(input("What is your total budget for the trip in USD? "))
    currency_symbol_input = input("What is the currency symbol for their destination? ")
    conversion_input = float(input(f'How many {currency_symbol_input} are there in 1 USD? '))

    print("\n")
    print(f'If you are travelling for {integer_number_of_days} days, that is the same as {integer_number_of_days * 24} hours, {integer_number_of_days * 24 * 60} minutes, or {integer_number_of_days * 24 * 60 *60} seconds.')
    print(f'If you are going to spend ${money_spent_input} USD, that means per day you can spend up to ${round(money_spent_input / integer_number_of_days, 2)} USD.')
    print(f'Your total budget in {currency_symbol_input} is {round(conversion_input * money_spent_input, 2)} {currency_symbol_input}, which per day is {round((conversion_input * money_spent_input) / integer_number_of_days, 2)} {currency_symbol_input}.')


def time_calculation():
    print("\n")
    time_difference = int(input("What is the time difference, in hours, between your home and your destination? If the time is behind, use a negative symbole in front of the amount of hours. "))
    our_time_input = 12
    if time_difference > 1:
        our_time_input % 2
    elif time_difference < 1:
        our_time_input = our_time_input
    print(f'That means that when it is midnight at home it will be {our_time_input + time_difference}:00 in your travel destination ')

days_money_currency()
time_calculation()