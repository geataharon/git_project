
name = input('please enter your name: ')
print('Hi there', name)

mood = int(input('On a scale of 1-5 (1 being the worst and 5 the best): How are you today?'))

if mood >3:
    print("That's the spirit! enjoy the rest of your day")
elif mood == 3:
    print("Balance is key!, wishing you a lovely day")
else:
    print("I'm sorry to hear that, hope your day gets better")
