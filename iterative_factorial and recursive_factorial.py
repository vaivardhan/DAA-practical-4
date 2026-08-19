def iterative_factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact


def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * recursive_factorial(n - 1)

n = int(input("Enter a number: "))

print("\nChoose a method:")
print("1. Iterative")
print("2. Recursive")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Factorial =", iterative_factorial(n))

elif choice == 2:
    print("Factorial =", recursive_factorial(n))

else:
    print("Invalid choice")
