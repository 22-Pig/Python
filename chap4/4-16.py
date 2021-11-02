sum = 0
count = 0
while True:
    number = int(input())
    if number == -1:
        break
    if number % 2 == 1:
        continue
    sum += number
    count += 1
average = sum / count
print(average)
