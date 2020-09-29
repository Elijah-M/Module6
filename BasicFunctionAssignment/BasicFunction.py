def weekly_pay(hours_worked, hourly_pay_rate):
    """ This function calculates and returns the product of
    hours_worked & hourly_pay_rate"""
    return hours_worked * hourly_pay_rate

def hourly_employee_input():
    """ This function takes user input for their name, hours worked, &
    and hourly pay, and then prints the information to the screen
    """
    name = input("Please enter your name: ")
    right_input = True  # bool for the while loop

    while right_input == True:
        try:
            hours_worked = int(input("Please enter how many hours you worked: "))
            right_input = False  # The correct input was entered, the loop ends
        except:
            print("Invalid input, please try again")

    while right_input == False:
        try:
            hourly_pay = float(input("Please enter your hourly pay: "))
            right_input = True  # The correct input was entered, the loop ends
        except:
            print("Invalid input, please try again")

    # Store the name and weekly pay in a string
    name_and_weekly_pay = "Name: " + name + ", Weekly Revenue: $" \
                          + str(weekly_pay(hours_worked, hourly_pay))

    print("=====================\n")  # spacing

    return name_and_weekly_pay

if __name__ == '__main__':
    print(hourly_employee_input())
