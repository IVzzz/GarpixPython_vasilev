list1 = list(map(int, input().split()))
for i in range(len(list1)):
    if list1[i] == 20:
        list1[i] = 200
print(list1)