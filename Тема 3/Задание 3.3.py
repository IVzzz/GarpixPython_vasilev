lst = [10, 17, 13, 44, 23, 88, 100, 99]
style = int(input("Введите 0, если хотите, чтобы программа считала количество четных чисел, и 1, если нечетных"))
counter = 0
for elem in lst:
    if elem % 2 == style:
        counter += 1
print(counter)