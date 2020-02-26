import sys, random
while True:
    guessNumber = int(input('Guess a number from 7 to 10\n'))
    randomNumber = random.randint(7, 10)
    if guessNumber == randomNumber:
        print('Perfect!')
        sys.exit()
    else:
        print('You are wrong the number was: ', randomNumber)
        continue
