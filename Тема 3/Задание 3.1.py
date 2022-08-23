numbers = map(int, input().split())
counter = 0
for i in numbers:
    if i % 2 == 0:
        counter += 1
print(counter)
