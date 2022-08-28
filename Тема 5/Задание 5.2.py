def getPerim(*numbers):
    sum = 0
    for i in numbers:
        sum += int(i)
    return sum/len(numbers)