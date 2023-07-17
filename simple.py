def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def calculate_principal(simple_interest, rate, time):
    return (simple_interest * 100) / (rate * time)

def calculate_rate(simple_interest, principal, time):
    return (simple_interest * 100) / (principal * time)

def calculate_time(simple_interest, principal, rate):
    return (simple_interest * 100) / (principal * rate)

print("Select what you want to calculate:")
print("1. Simple Interest")
print("2. Principal")
print("3. Rate")
print("4. Time")

choice = int(input("Enter your choice: "))

if choice == 1:
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter rate of interest (in %): "))
        time = float(input("Enter time period (in years): "))
        simple_interest = calculate_simple_interest(principal, rate, time)
        print(f"Simple Interest: {simple_interest:.2f}")
elif choice == 2:
        simple_interest = float(input("Enter simple interest amount: "))
        rate = float(input("Enter rate of interest (in %): "))
        time = float(input("Enter time period (in years): "))
        principal = calculate_principal(simple_interest, rate, time)
        print(f"Principal: {principal:.2f}")
elif choice == 3:
        simple_interest = float(input("Enter simple interest amount: "))
        principal = float(input("Enter principal amount: "))
        time = float(input("Enter time period (in years): "))
        rate = calculate_rate(simple_interest, principal, time)
        print(f"Rate: {rate:.2f}")
elif choice == 4:
        simple_interest = float(input("Enter simple interest amount: "))
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter rate of interest (in %): "))
        time = calculate_time(simple_interest, principal, rate)
        print(f"Time: {time:.2f}")
else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")

