# all variables load before program begins
run = True
while run:
    import random
    import time

    intro = 'Welcome to rock paper scissors! Choose one of the three options to make your move!'
    options = 'Choose one of these options:\n 1.Rock\n 2. Paper\n 3. Scissors'

    # actual game starts here
    print(intro)
    print(options)
    n = random.randint(1, 3)
    playerchoice = int(input('Your choice:'))

    print('You chose:', playerchoice)
    print(f'''Computer chose: {n}''')

    # checking to see whether you tied, won, or lost
    if playerchoice == n:
        print('Tie!')
    elif playerchoice > n:
        print('You win!')
    elif playerchoice < n:
        print('You lost.')
    else:
        # printing error in case computer fails to choose an option
        print('Error, restart program.')
    time.sleep(2)
