def score_input(test_name, test_score=0, invalid_message='Invalid test score, try again!'):
    """
    This function asks the user for a valid test score until it is in the range,
    then prints valid input as 'Test name: ##'.

    :param test_name:
    :param test_score:
    :param invalid_message:
    :return:
    """


    MIN = 0  # Min test score value
    MAX = 100  # Max test score value
    end_loop = True  # Used to break the loop
    while end_loop:
        choice = input("Is your test score greater than zero? (y/n): ")
        if choice != 'y' and choice != 'Y' and choice != 'n' and choice != 'N':
            print("Invalid input, please try again.")
        elif choice == 'y' or choice == 'Y':
            try:
                test_score = int(input("Please enter you test score (0-100): "))
                if MIN <= test_score <= MAX:
                    end_loop = False  # Good input (int between 0-100), breaks the loop
                else:
                    print(invalid_message)  # The user entered an int outside of 0-100
            except:
                print(invalid_message)
            end_loop = False
        else:  # user entered 'n' or 'N'
            end_loop = False

    print("======================\n", "Results:\n", "Test Name: ", test_name, "\n Test Score: ", test_score, "/ 100")

    # return { test_name: test_score}


if __name__ == '__main__':

    test_name = input("Please enter your test name: ")

    score_input(test_name)
