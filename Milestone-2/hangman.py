import random

# defining function to display the working word
def display():
    for num in range(0,len(li)):
        print(li[num],end="")




word_list = ["Eldhose","Elsa","Sheela","Varghese"]

word = random.choice(word_list)
word = word.lower()
word = list(word)

num = 0
li=[]

for num in range(0,len(word)):
    print("-",end ="")
    li.append("-")
game = True
lives = 6
while game != False:
    guess = input("\nEnter your guess")
    guess = guess.lower()
    for num  in range(0,len(word)):
        if word[num] == guess:
            li[num] = guess
            print("You guessed it right")
        
    display()
    if lives == 0:
        game = False
        print("You lose...")   
        
    if "-" not in li:
        game = False   
        print("\nYou win babe")
    

    

    
        









