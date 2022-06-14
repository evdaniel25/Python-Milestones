#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

l=[]
for iter1 in range(0,nr_letters-1):
  alpha = random.randint(0,25)
  print(letters[alpha],end="")
  l.append(letters[alpha])
for iter2 in range(0,nr_symbols-1):
  alpha = random.randint(0,8)
  print(symbols[alpha],end="")
  l.append(symbols[alpha])
for iter3 in range(0,nr_numbers-1):
  alpha = random.randint(0,9)
  print(numbers[alpha],end="")
  l.append(numbers[alpha])

li=[]
li=random.sample(l,len(l))
for item in li:
  print(item,end="")