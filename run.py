''' zodiac zone imports '''

import os
import random
import time
from random import randint
import pyfiglet


def main():
    # ASCII generated art for main logo
    title = pyfiglet.figlet_format(
        "Zodiac Zone", font="standard", justify="center")

    print(title)

    # List/ dictionary for random horoscope generation
    first = [
        "Today is perfect for new endeavors.",
        "Today is the day to cherish and embrace others.",
        "The tensions of this week will feel heavier today.",
        "Making yourself useful is a main component of a successful day.",
        "Today, exercise caution when crossing the street.\n"]

    second = [
        "Remember that good things come to those who work hard. ",
        "Dont let the circumstances bring you down."
        "Patience is key, but sometimes a little push can get it done.",
        "A smile can get you a long way.\n"]

    third = [
        "Looking ahead may seem like a waste, but it pays off in the end.",
        "Luck favors those who mind the risks and take them. ",
        "Today is the day for that thing you always wanted to do. ",
        "Luck is on your side today, so seize it! ",
        "Things are looking up for you!\n"]

    color = [
        "Red", "Green", "Orange", "White", "Black", "Purple", "Silver",
        "Brown", "Gray", "Pink", "Cream", "Gold", "Teal", "Navy Blue",
        "Turquoise", "Amber", "Mint"]

    star = [
        "An Aries", "A Taurus", "A Gemini", "A Cancer", " A Leo",
        "A Virgo", "A Libra", " A Scorpio", "A Sagittarius",
        "A Capricorn", "An Aquarius", "A Pisces"]

    print('Welcome to The Zodiac Zone \n',
          'The place to find out your Zodiac sign\n',
          'And get a personalized horoscope for your sign\n')

    name = input('Please enter you name to begin\n')

    print("", 'Hello ' + name)

    print("", "Please enter your Month and Day of Birth\n")

# Defines month funtion

    def month():
        """
        This function only excepts numbers from user input
        for month of birth
        """
        while True:
            try:
                month = int(input("What is your month of birth?[eg.10]\n"))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue

            if month not in range(1, 13):
                print("Sorry, your reply must be a number between 1 and 12.")
                continue
            else:
                break

        return month

    month = month()

    # Defines day function
    def day():
        """
        This function only excepts numbers from user input
        for day of birth
        """
        while True:
            try:
                day = int(input("What is your day of birth?:[eg.12]\n"))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue

            if day not in range(1, 32):
                print("Sorry, your reply must be a number between 1 and 31.")
                continue
            if month in (1, 3, 5, 7, 10, 12):
                max_days = 31
            elif month in (4, 6, 9, 11):
                max_days = 30
            elif month == 2:
                max_days = 29
            else:
                break
            if month < 1 or month > 12:
                print("Entered invalid date")
            elif day < 1 or day > max_days:
                print("Entered invalid day")
            else:
                break
        return day

    day = day()

    # prints out user feedback
    print("")
    print('Thank you! I will now consult the cosmos & return your star sign\n')
    time.sleep(3)
    os.system('cls||clear')

    # Defines day and month and calculates which sign to display
    def sign(day, month):
        """
        Depending on user input, if/elif statement will calculate which
        sign to display after user inputs date of birth
        """
    # returns Aquarius if user input is within month and day parameters

        if ((int(month) == 1 and int(day) >= 20) or
                (int(month) == 2 and int(day) <= 18)):
            sign = ("Aquarius")

        # returns Pisces if user input is within month and day parameters
        elif ((int(month) == 2 and int(day) >= 19) or
                (int(month) == 3 and int(day) <= 20)):
            sign = ("Pisces")

        # displays Aries if user input is within month and day parameters
        elif ((int(month) == 3 and int(day) >= 21) or
                (int(month) == 4 and int(day) <= 19)):
            sign = ("Aries")

        # displays Taurus if user input is within month and day parameters
        elif ((int(month) == 4 and int(day) >= 20) or
                (int(month) == 5 and int(day) <= 20)):
            sign = ("Taurus")

        # displays Gemini if user input is within month and day parameters
        elif ((int(month) == 5 and int(day) >= 21) or
                (int(month) == 6 and int(day) <= 20)):
            sign = ("Gemini")

        # displays Cancer if user input is within month and day parameters
        elif ((int(month) == 6 and int(day) >= 21) or
                (int(month) == 7 and int(day) <= 22)):
            sign = ("Cancer")

        # displays Leo if user input is within month and day parameters
        elif ((int(month) == 7 and int(day) >= 23) or
                (int(month) == 8 and int(day) <= 22)):
            sign = ("Leo")

        # displays Virgo if user input is within month and day parameters
        elif ((int(month) == 8 and int(day) >= 23) or
                (int(month) == 9 and int(day) <= 22)):
            sign = ("Virgo")

        # displays Libra if user input is within month and day parameters
        elif ((int(month) == 9 and int(day) >= 23) or
                (int(month) == 10 and int(day) <= 22)):
            sign = ("Libra")

        # displays Scorpio if user input is within month and day parameters
        elif ((int(month) == 10 and int(day) >= 23) or
                (int(month) == 11 and int(day) <= 21)):
            sign = ("Scorpio")

        # displays Sagittarius if user input is within month and day parameters
        elif ((int(month) == 11 and int(day) >= 22) or
                (int(month) == 12 and int(day) <= 21)):
            sign = ("Sagittarius")

        # displays Capricorn if user input is within month and day parameters
        elif ((int(month) == 12 and int(day) >= 22) or
                (int(month) == 1 and int(day) <= 19)):
            sign = ("Capricorn")

        # count down display and user feedback
        print("Calculating...\n")
        time.sleep(1)
        print("Consulting the cosmos...\n")
        time.sleep(1)
        print("Searching the stars...\n")
        time.sleep(1)
        print("Diving deep into the Zodiac...\n")
        time.sleep(2)
        print('Your zodiac sign is ...' " " + sign)
        print("")
        time.sleep(2)
        print('Generating horoscope for' " " + sign)
        time.sleep(4)
        print("")

    sign(day, month)

    # Print random generated horoscope
    print(
        "Your Horoscope today is....\n",
        random.choice(first), random.choice(second),
        random.choice(third))

    print("")
    time.sleep(2)

    # prints  6 random generated lotto numbers
    print("You Lucky Lotto numbers for your sign are...\n")

    lotto = random.sample(range(0, 48), 6)
    print(lotto)

    print("")
    time.sleep(2)

    # prints lucky color
    print(
        "Your lucky color for today is....\n",
        random.choice(color))

    print("")
    time.sleep(2)

# prints a sign to for user to get to know
    print(
        "The sign to get flirty with today is...\n",
        random.choice(star))
    time.sleep(8)

# restart or quit application depending on user input

    while True:
        answer = input("Would you like another Horoscope? Enter y/n:").lower()
        if answer == 'y':
            os.system('cls||clear')
            main()
            continue

        # if no, stop the execution of the program
        elif answer == 'n':
            end = pyfiglet.figlet_format(
                "I hope you have a Great day!",
                font="standard", justify="center")
            print(end)
            exit(1)
        # if invalid response, ask the player to enter a valid choice
        else:
            print('Apologies, Please enter Y or a N.')


main()
