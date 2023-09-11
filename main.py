while True:
    user_input = input()

    if user_input.lower() == 'quit':
        break

    input_parts = user_input.split()

    if len(input_parts) != 2:
        print(
            "Invalid input format. Please enter a word and an integer separated by space.")
        continue

    word = input_parts[0]
    integer_input = input_parts[1]

    try:
        integer_input = int(integer_input)
    except ValueError:
        print("Invalid input for integer. Please enter a valid integer.")
        continue
    if integer_input == 0:
        continue
    # Here you can construct a sentence using the input values
    sentence = f"Eating {integer_input} {word} a day keeps the doctor away."
    print(sentence)

print("Goodbye!")
