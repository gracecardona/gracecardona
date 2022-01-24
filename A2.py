""" This is a program which asks the user for their favorite color
as well as their name and preferred nickname and welcomes them.
"""


def print_menu():
    """ Obtain the user's favorite color from a menu."""
    print("1) Green")
    print("2) Blue")
    print("3) Purple")
    print("4) Quit")


def main():
    """ Obtain the user's name and select answer choice."""
    user_name = input('Please enter your name: ')
    print("Hi ", user_name,",", " Welcome to the main menu.",sep= '')
    print("Main Menu")
    print_menu()
    answer_choice = input("Please choose your favorite color: ")
    try:
        int_answer_choice = int(answer_choice)
    except ValueError:
        print("Next time please enter a number")
    else:
        if int_answer_choice == 1:
            print("Grass is green!")
        elif int_answer_choice == 2:
            print("Why so blue?")
        elif int_answer_choice == 3:
            print("Your royal highness!")
        elif int_answer_choice == 4:
            print("Thanks for playing!")
        else:
            print("Please enter a number from 1-4")
    finally:
            print("Come back soon!")


if __name__ == "__main__":
    main()


r"""
--- Sample Run #1 ---
Please enter your name: Grace
Hi Grace, Welcome to the main menu.
Main Menu
1) Green
2) Blue
3) Purple
4) Quit
Please choose your favorite color: 1
Grass is green!
Come back soon!

--- Sample Run #2 ---
Please enter your name: Grace
Hi Grace, Welcome to the main menu.
Main Menu
1) Green
2) Blue
3) Purple
4) Quit
Please choose your favorite color: two
Next time please enter a number
Come back soon!
"""
