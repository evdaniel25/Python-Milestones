# Average Student Height Calculation


student_heights = input("Input a list of student heights ").split()
sum = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

for n in range(0, len(student_heights)):
  sum+=student_heights[n]
avg = sum//len(student_heights)
print("The average height is "+str(avg))
  




