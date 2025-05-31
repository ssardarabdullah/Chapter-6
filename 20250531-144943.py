favorite_numbers = {
    "Alice": 7,
    "Bob": 42,
    "Charlie": 3,
    "Diana": 14,
    "Ethan": 9
}

for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}.")
    glossary = {
    "variable": "A container for storing data values.",
    "function": "A block of code that performs a specific task.",
    "loop": "A way to repeat a block of code multiple times.",
    "dictionary": "A collection of key-value pairs.",
    "list": "An ordered collection of items."
}

for term, definition in glossary.items():
    print(f"{term.title()}:\n  {definition}\n")