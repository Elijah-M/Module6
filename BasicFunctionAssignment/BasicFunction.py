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

    print("=====================\n")  # spacing
    print("Results:", "\nName: ", name, "\nHours Worked: ", hours_worked,
          "\nHourly Pay: ", hourly_pay)

if __name__ == '__main__':
    hourly_employee_input()