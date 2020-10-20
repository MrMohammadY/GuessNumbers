from random import choice, randint


def get_guess_user():
    """
    get user guess and check,return that
    :return:
    """
    try:
        return int(input('Please Enter Your Choice: '))
    except ValueError:
        return get_guess_user()


def get_choice_system(num1, num2):
    """
    :param num1: get this in menu func start_num
    :param num2: get this in menu func end_num
    :return: choice system
    """
    return randint(num1, num2)


def find_winner(sys, user):
    """
    find winner
    :param sys: system choice
    :param user: user guess
    :return: message like: You win
    """
    message = str()

    if sys == user:
        message = f'You win\nYour Guess is: {user} and system choice is: {sys}'
    else:
        print('Your guess is not correct! try again...')
        return find_winner(sys, get_guess_user())

    return message
