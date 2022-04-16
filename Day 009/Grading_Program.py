# You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.
# Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values. The final version of the student_grades dictionary will be checked.
# This is the scoring criteria:
# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}



# student_grades = student_scores
# for names in student_grades:
#     if student_grades[names] >=91 and student_grades[names] <=100:
#         student_grades[names] = "Outstanding"
#     elif student_grades[names] >=81 and student_grades[names] <=90:
#         student_grades[names] = "Exceeds Expectations"
#     elif student_grades[names] >=71 and student_grades[names] <=80:
#         student_grades[names] = "Acceptable"
#     else:
#         student_grades[names] = "Fail"

# Alternative way

for names in student_scores:
    if student_scores[names] >90:
        student_grades[names] = "Outstanding"
    elif student_scores[names] >=80:
        student_grades[names] = "Exceeds Expectations"
    elif student_scores[names] >70:
        student_grades[names] = "Acceptable"
    else:
        student_grades[names] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)