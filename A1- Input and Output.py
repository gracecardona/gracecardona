""" This is a program which asks the user for their name and preferred nickname
and welcomes them.
"""


def main():
    """ Obtain the user's name and nickname."""
    user_name = input('Please enter your birth name: ')
    user_nickname = input('If you prefer a "nickname" please enter it or enter N/A: ')
    if user_nickname == 'N/A':
        print("Welcome,", user_name, "!", " Very nice to meet you!" ,sep= '' )
    else:
        print("Welcome,", '"', user_nickname, '"', "!", " Very nice to meet you!",sep= '' )


if __name__ == "__main__":
    main()

r"""
--- Sample Run #1---
Please enter your birth name: Grace
If you prefer a "nickname" please enter it or enter N/A: Gracie
Welcome,"Gracie"! Very nice to meet you!

--- Sample Run #2---
Please enter your birth name: Grace
If you prefer a "nickname" please enter it or enter N/A: N/A
Welcome,Grace! Very nice to meet you!
"""
