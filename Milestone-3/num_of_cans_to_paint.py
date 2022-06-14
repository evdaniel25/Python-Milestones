#Write your code below this line 👇
import math
def paint_calc(height, width, cover):
  area = height * width
  num_of_cans = math.ceil(area/cover)
  print(f"You need {num_of_cans} number of cans")






#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

paint_calc(test_h,test_w,coverage)  
  
  
  



