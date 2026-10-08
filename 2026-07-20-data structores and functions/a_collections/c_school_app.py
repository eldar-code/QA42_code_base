# data layer
subjects = []

# display layer
print("Menu=====================")
print("view subjects ........... view")
print("add a subject ........... add")
print("remove a subject ........ remove")
print("quite.................... x")
print("=========================")

while True:
    # application layer
    user_input = input("Enter you choice: ")
    if user_input == "view":
        print(subjects)
    elif user_input == "add":
        new_subject = input("Enter new subject: ")
        subjects.append(new_subject)
    elif user_input == "remove":
        subject_to_remove = input("Enter subject to remove: ")
        subjects.remove(subject_to_remove)
    elif user_input == "x":
        break
    else:
        print(f"The choice {user_input} is not supported!")
    print("-----------------------------------------")

print("Bye!")

