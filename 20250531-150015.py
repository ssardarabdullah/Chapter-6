# Create the dictionary
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china'
}

# Print a sentence about each river
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print()  # Blank line for readability

# Print the name of each river
print("Rivers included in the dictionary:")
for river in rivers:
    print(river.title())

print()  # Blank line for readability

# Print the name of each country
print("Countries included in the dictionary:")
for country in rivers.values():
    print(country.title())