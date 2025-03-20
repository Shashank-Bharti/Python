# fruits = ['apple', 'banana', 'cherry']
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " "+"pie")

student_marks= [120, 112, 23, 56, 167, 978 ]

# total_score = sum(student_marks)
# print(total_score)

max_score = 0
 
for score in student_marks:
    if score > max_score:
        max_score = score
print(max_score)
    