import random

num = random.randint(1,9)
chance = 5
print(num)
while chance > 0:
    guess = int(input('Guess a number between 1 and 9!'))
    chance = chance - 1
    if guess == num:
        print('Correct!')
        break
    elif guess < num:
        print('Good try! Try guessing a number higher than',guess,'and you have',chance,'chance(s) left.')
    elif guess > num:
        print('Good try! Try guessing a number lower than',guess,'and you have',chance,'chance(s) left.')
        

if chance == 0 and guess != num:
    print('You have run out of chances! The number was ', num)



