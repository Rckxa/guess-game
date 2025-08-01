'''
Basic refresher
concepts used:
    * functions
    * libraries
    * variables and strings, loops and conditionals, strings, formating f""
'''

import random



def start(guess_bool, num_tries, max_val):
    ans = random.randint(0, max_val)
    initial_tries = 5
    while not guess_bool and num_tries > 0:
        print(f'''
        Tries left: {num_tries}
              ''')
        while True:
            try:
                guess = int(input(f"Guess the number between 1 and {max_val}:"))
                break
            except ValueError:
                print('Your guess should be a number')
        num_tries = num_tries - 1

        if guess < ans:
            print("Too Low")
        if guess > ans:
            print("Too High")
        if guess == ans:
            print(f"The answer was {ans}")
            break
        if num_tries == 0:
            print(f"You have run out of tries, the answer was {ans}")
            break

    print('''
    1. Next level
    2. Restart
    3. Quit
           ''')
    choice = int(input(''))
    if choice == 1:
        max_val = max_val + 10
        ans = random.randint(0, max_num)
        guess_bool = False
        num_tries = initial_tries + 3
        initial_tries = num_tries
    elif choice == 2:
        ans = random.randint(0, max_num)
        guess_bool = False
        num_tries = initial_tries
    else:
        print('Quitting... Goodbye!')
        guess_bool = True


        # break
    pass

max_num = 10
guessed = False
tries = 4
start(guessed, tries, max_num)

