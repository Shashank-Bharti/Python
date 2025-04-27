import random as r 
# new_dict = {new_key:new_value for (key,value) in dict.items()if test}

names = ['Raju', 'Meera', 'Sheena', 'Hitesh', 'Rupa', 'Sahil']
student_scores = {student :r.randint(0,100) for student in names}
passed_students = {student:score for (student ,score)in student_scores.items() if score > 60  }
print(student_scores)
print(passed_students)