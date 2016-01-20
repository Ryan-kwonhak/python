from random import randint
number = randint(1,100)
i = 0
while True:
    i = i + 1
    guess = int(raw_input("Guess Number between 1 to 100: "))
    if number == guess and i < 6:
         print 'congratulation!! \nThe number is {0}'.format(guess)
         break
    elif number > guess and i < 6:
         print 'Your guess,{0}, is low!'.format(guess)    
    elif number < guess and i < 6:
         print 'Your guess,{0}, is high!'.format(guess)
    elif i == 6:
         print 'Game over!'
         break
