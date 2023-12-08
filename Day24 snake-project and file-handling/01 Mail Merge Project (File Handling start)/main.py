#   TODO: Create a letter using starting_letter.txt

PLACEHOLDER = "[name]"
with open("Input/Names/invited_names.txt") as names_data:
    names = names_data.readlines()

with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
