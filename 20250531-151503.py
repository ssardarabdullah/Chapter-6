Question 5_____

Make two new dictionaries
representing different people,
and store all three 
dictionaries in a list called
people. Loop through your list of
people. As you 
loop through the list, print 
everything you know about each
person.

solution ____________


person_1 = {
    'first_name': 'Alice',
    'last_name': 'Johnson',
    'age': 28,
    'city': 'New York'
}

person_2 = {
    'first_name': 'Bob',
    'last_name': 'Smith',
    'age': 34,
    'city': 'Los Angeles'
}

person_3 = {
    'first_name': 'Charlie',
    'last_name': 'Brown',
    'age': 22,
    'city': 'Chicago'
}

 Store all dictionaries in a list
people = [person_1, person_2, person_3]

 Loop through the list and print info about each person
for person in people:
    print("\nPerson Information:")
    for key, value in person.items():
        print(f"{key.title()}: {value}")
