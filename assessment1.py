student_name = "Thallam Jyothisri"
student_age = 22
is_passed = True

subjects = ["Sanskrit", "Physics", "English", "Tamil","Telugu"]
marks = (90, 82, 90, 72, 93)

student_info = {"name": student_name, "age": student_age, "branch": "ECE", "marks": marks}

skills = {"C", "Python", "SQL", "MATLAB"}

def calculate_average(marks): # Function to calculate average marks
    return sum(marks) / len(marks)

print("\nStudent Information:")
for key, value in student_info.items():
    print(f"{key}: {value}")

print("\nSubjects:")
for subject in subjects:
    print(subject)

print("\nMarks:")
for mark in marks:
    print(mark)

print("\nSkills:")
for skill in skills:
    print(skill)

avg_marks = calculate_average(marks)
print(f"\nAverage Marks: {avg_marks}")

count = 3
print("\nGenerating Report:")
while count > 0:
    print(count)
    count -= 1

if avg_marks >= 60:
    print("\nResult: Passed")
else:
    print("\nResult: Failed")
