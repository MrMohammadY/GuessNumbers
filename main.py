from choices import get_choice_system, get_guess_user, find_winner


def menu():
    """
    getting start number and end number, like: start_num < X <end_num
    :return:
    """
    print('Choosing a system between what numbers?')

    try:
        start_num = int(input('start: '))
        end_num = int(input('end: '))
    except ValueError:
        print('Please Enter Number Again!')
        return menu()

    if start_num > end_num or start_num == end_num:
        print('Please Enter Number Again!')
        return menu()

    return start_num, end_num


def run():
    level = menu()
    choice_system = get_choice_system(level[0], level[1])
    choice_user = get_guess_user()
    winner = find_winner(choice_system, choice_user)
    print(winner)

    play_again = input('If you want play again press(y/Y): ')

    if play_again == 'y' or play_again == 'Y':
        return run()


if __name__ == '__main__':
    run()
