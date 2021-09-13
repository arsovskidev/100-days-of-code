# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# 🚨 Don't change the code above 👆

# Write your code below this row 👇

total = 0
students = 0

for x in student_heights:
    total += x
    students += 1

avg = round(total / students)

print(avg)