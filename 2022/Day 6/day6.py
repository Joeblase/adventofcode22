def characters_processed(puzzle_input, characters):
    with open(puzzle_input) as input_file:
        input_string = input_file.read()
    for num in range(len(input_string)-characters):
        letters = input_string[num:num+characters]
        duplicate_count = 0
        for letter in letters:
            if duplicate_count > 0:
                break
            matches = -1
            for letter_index in range(characters):
                if letter == letters[letter_index]:
                    matches += 1
            duplicate_count += matches
        if duplicate_count == 0:
            return input_string.find(letters) + characters


print(f"The amount of characters processed before the first start of packet marker is: {characters_processed('input.txt', 4)}")
# The amount of characters processed before the first start of packet marker is: 1833

print(f"The amount of characters processed before the first start of message marker is: {characters_processed('input.txt', 14)}")
# The amount of characters processed before the first start of message marker is: 3425
