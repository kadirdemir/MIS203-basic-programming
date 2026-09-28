# Display a short title before asking the user for information.
print("=== Student Introduction Card ===")

# input() waits for the user to type a value and stores the entered text
# in the variable on the left side of the assignment.
name = input("Name: ")
student_id = input("Student ID: ")
department = input("Department: ")
github_username = input("GitHub username: ")
programming_goal = input("Programming goal: ")

# Print a clear heading for the completed student card.
# \n starts the output on a new line to separate it from the input section.
print("\n==============================")
print("        STUDENT CARD")
print("==============================")

# f-strings place the values stored in our variables directly into the output.
print(f"Name: {name}")
print(f"Student ID: {student_id}")
print(f"Department: {department}")
print(f"GitHub: {github_username}")
print(f"Programming Goal: {programming_goal}")

# Print a final separator line to make the card easier to read.
print("==============================")
