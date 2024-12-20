 # Function to calculate the sum of numbers from 1 to n
def sum_of_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Input the value of n
n = int(input("Enter a number n: "))

# Get the sum and print the result
result = sum_of_numbers(n)
print(f"The sum of numbers from 1 to {n} is {result}.")
