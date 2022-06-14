# 🚨 Don't change the code below 👇
# High score calculation


student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
big = 0
for n in range(0, len(student_scores)):
  if(student_scores[n]>big):
    big = student_scores[n]
print("The highest score is "+str(big))
