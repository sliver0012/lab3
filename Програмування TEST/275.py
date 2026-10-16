n = input("Enter a natural number: ")

digits = [int(i) for i in n]

max_digit = max(digits)
min_digit = min(digits)

if (max_digit - min_digit) % 2 == 0:
    print("true")
else:
    print("false")