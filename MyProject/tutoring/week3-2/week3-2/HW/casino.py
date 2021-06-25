from random import sample

class Pachinko:
    def __init__(self, mode='easy'):
        self.coins = 10000

        if mode == 'easy':
            num_cases = 3
        elif mode == 'normal':
            num_cases = 5
        elif mode == 'hard':
            num_cases = 10
        else:
            num_cases = 100

        self.pool = list(range(num_cases))
        self.multiple = num_cases

    def run(self, coins, guess):
        number = sample(self.pool, 1)[0]
        print("You bet {} coins on {}".format(coins, guess))
        print("number {}".format(number))

        if number == guess:
            print("Congratulation!!")
            return coins * self.multiple

        else:
            print("Sorry, try again")
            return 0
