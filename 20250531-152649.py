# Dictionary to store people's names and their favorite numbers
favorite_numbers = {
    'Alice': [7, 42],
    'Bob': [3],
    'Charlie': [5, 9, 14],
    'Diana': [8, 22],
}

# Print each person's name along with their favorite numbers
for name, numbers in favorite_numbers.items():
    print(f"{name}'s favorite numbers are: {', '.join(str(num) for num in numbers)}")