my_dictionary = {
    "Python": "A programming language",
    "SQL": "A language for databases",
    "Jira": "A project management application"
}

word = input("Enter a word: ")
definition = my_dictionary[word]
print(definition)

# add entry to a dictionary
my_dictionary["HTML"] = "A programing language for ui"
print(my_dictionary)

# ask if a dictionary has key
if "SQL" in my_dictionary:
    print("YES")
else:
    print("NO")

# removing an entry
my_dictionary.pop("SQL")


