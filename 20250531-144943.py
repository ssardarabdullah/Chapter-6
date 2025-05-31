Question 2 ____
 Favorite Numbers: Use a dictionary to 
store people’s favorite numbers.
Think of five names, and use
them as keys in your dictionary. 
Think of a favorite number for
each person, and store each as a
value in your dictionary. 
Print each person’s name and their
favorite number. For even more fun,
poll a few friends and get some 
actual data for your program.

solution -__________
favorite_numbers = {
    "Alice": 7,
    "Bob": 42,
    "Charlie": 3,
    "Diana": 14,
    "Ethan": 9
}
for name, number in favorite_numbers
.items():
    print(f"{name}'s favorite numbe
    r is {number}.")
    glossary = {
    "variable": "A container for
    storing data values.",
    "function": "A block of code 
    that performs a specific task.",
    "loop": "A way to repeat a block
    of code multiple times.",
    "dictionary": "A collection of 
    key-value pairs.",
    "list": "An ordered collection 
    of items."
}
 for term, definition in glossary
.items():
    print(f"{term.title()}:\n 
    {definition}\n")
