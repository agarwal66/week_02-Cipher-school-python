#MODIFY
winning_number = 44
guess = 1
number = input("guess a number between 1 and 100:")
game_over =  False
while not game_over:
    if number == winning_number:
        print("you win and you guesses this number in {guess} times")
    else:
        if number < winning_number:
            print("too low")
            guess +=1
            number = input("guess again:")
        else :
            print("too high")
        guess +=1
        number = int(input("guess again :"))    