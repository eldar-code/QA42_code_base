# list is orders and allow duplicates
x = [2, 4, 6, 8]
y = [5, "Hello", True]
print(x)
print(y)

school_schedule = [
    "Python",
    "Python",
    "Java",
    "HTML",
    "HTML",
]

hour = int(input("Enter Hour: "))
print(school_schedule[hour-1])

# use append to add elements to the end of the list
new_subject = input("Enter a new learning subject: ")
school_schedule.append(new_subject)
print(school_schedule)

# use insert to add elements to a specific index in the list
new_subject = input("Enter a new learning subject: ")
hour = int(input("Enter Hour: "))
school_schedule.insert(hour-1, new_subject)
print(school_schedule)
