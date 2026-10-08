my_dict = {1: "one", 2: "two"}
my_dict[3] = "three"

key = int(input("Enter key: "))
if key in my_dict:
    print(my_dict[key])
else:
    print("not in dict")

