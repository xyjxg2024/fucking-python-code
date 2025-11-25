def sum(number):
    sum = 0
    for digit in str(number):
        sum += int(digit)
    return sum
number = int(input())
result = sum(number)
print(result)
