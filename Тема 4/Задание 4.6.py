str_list = []
while True:
    new_str = input("Print next string")
    if new_str == "q":
        break
    else:
        str_list.append(new_str)
print(str_list)