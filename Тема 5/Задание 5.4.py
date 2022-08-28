list1 = ["Mike", "", "Emma", "Kelly", "", "Brad", "", "", ""]
delete_empty = lambda lst: lst.remove("")
while list1.count("") > 0:
    delete_empty(list1)
