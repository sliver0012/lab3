count = 0

while True:
    n = int(input("Enter a number: "))
    if n == 0:
        break
    count += 1

print(f"You entered {count} numbers before entering 0.")