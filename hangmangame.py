import random

words=["banana" , "flight" , "tejas", "raam"]
wrd=[]
word=random.choice(words)

for i in range(len(word)):
    wrd+="_"

print(wrd)
print("")
print("Welcome to Hangman, You have 5 guesses ")
game_over=0
num=0
while not game_over:
    guess=input("Enter your guess: ") #complicated logic XD
    for position in range(len(word)):
        letter=word[position]
        if letter == guess:
            wrd[position]=letter
    if guess not in word:
        num+=1
        print(f"you have {5-num} guesses left")
        if num >=5:
            print("You lose!")
            game_over=1

    print(wrd)

    if '_' not in wrd:
        print("You win")
        break
