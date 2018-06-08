# get and process input for a list of names
names = input("Enter names separated by commas:").split(",")
# get and process input for a list of the number of assignments
assignments = input("Enter assignment counts separated by commas:").split(",")
# get and process input for a list of grades
grades = input("Enter grades separated by commas:").split(",")

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for index in range(len(names)):
    name = names[index].title()
    assignment = int(assignments[index])
    grade = int(grades[index])
    increase_grade = grade + 2 * assignment

    print(message.format(name, assignment, grade, increase_grade))

for name, assignment, grade in zip(names, assignments, grades):
    increase_grade = grade + 2 * assignment
    print(message.format(name, assignment, grade, increase_grade))
