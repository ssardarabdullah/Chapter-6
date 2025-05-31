# Dictionary of people who have already taken the poll
favorite_languages = {
    'alice': 'python',
    'bob': 'java',
    'carol': 'c++',
    'dave': 'javascript'
}

# List of people who should take the poll (some in the dictionary, some not)
people_to_poll = ['alice', 'bob', 'erin', 'frank', 'carol', 'george']

# Loop through the list and check if they've already taken the poll
for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for already taking the poll.")
    else:
        print(f"{person.title()}, please take a moment to take our favorite languages poll!")