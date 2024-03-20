def get_user_mood():
    while True:
        name = input('Please enter your name: ')
        print('Hi there,', name)

        try:
            mood = int(input('On a scale of 1-5 (1 being the worst and 5 the best): How are you today? '))

            if mood < 1 or mood > 5:
                print("Please enter a number between 1 and 5.")
                continue

            if mood > 3:
                print("That's the spirit! Enjoy the rest of your day.")
            elif mood == 3:
                print("Balance is key! Wishing you a lovely day.")
            else:
                print("I'm sorry to hear that, hope your day gets better.")
            break  # Exit the loop if input is valid
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    get_user_mood()
