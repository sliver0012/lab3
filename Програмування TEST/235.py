n = float(input("Enter calories burned per minute: "))

for minutes in [10, 15, 20, 25, 30]:
    print(f"Calories burned in {minutes} minutes: {n * minutes}")