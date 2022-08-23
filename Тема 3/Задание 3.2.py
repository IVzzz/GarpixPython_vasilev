password = "abc123"
while True:
    try_pass = input()
    if password == try_pass:
        print("Правильно")
        break
    elif try_pass == "q":
        print("Выход")
        break
