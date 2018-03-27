from random import  randint
machine_number=randint(1,10)
counter=int(input('Max guesses?: '))

while True:

    if counter==0:
        print('You reach you guess limit!')
        break

    user=int(input('Input your number: '))

    if user==machine_number:
        print('Bravo')
        break;
    elif user<machine_number:
        print('your guess is less than my number.Try again')
    elif user >machine_number:
        print('Your guess is greater than my number.Try again')


    counter=counter-1