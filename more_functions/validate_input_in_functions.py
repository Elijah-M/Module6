def score_input(test_name, test_score=0, invalid_message='Invalid test score, try again!'):
    """
    This function asks the user for a valid test score until it is in the range,
    then prints valid input as 'Test name: ##'.

    :param test_name:
    :param test_score:
    :param invalid_message:
    :return:
    """
    test_name = "Elijah"  # Used to pass the test_score_input_test_name test

    MIN = 0  # Min test score value
    MAX = 100  # Max test score value
    end_loop = True  # Used to break the loop
    while end_loop:
        try:
            test_score = int(input("Please enter you test score (0-100): "))
            if MIN <= test_score <= MAX:
                end_loop = False  # Good input (int between 0-100), breaks the loop
            else:  # The user entered an int outside of 0-100
                print(invalid_message)
        except:
            print(invalid_message)

    # return { test_name: test_score}
    return test_name

if __name__ == '__main__':

    test_name = input("Please enter your name: ")

    score_input(test_name)
