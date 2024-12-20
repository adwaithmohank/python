# Initialize sum variable
sum_even_numbers = 0

# Loop through numbers between 10 and 90 (inclusive)
for num in range(10, 91):  # range is inclusive of 10 and exclusive of 91
    if num % 2 == 0:  # Check if the number is even
        sum_even_numbers += num

# Output the result
print("Sum of all even numbers between 10 and 90 is:", sum_even_numbers)
