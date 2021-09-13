import caesar

print(caesar.logo)

running = True


def caesar(text, shift_amount, direction):
    result = ""

    if direction == "decode":
        shift_amount *= -1

    for char in text:
        if char in caesar.alphabet:
            new_index = caesar.alphabet.index(char)
            result += caesar.alphabet[new_index + shift_amount]
        else:
            result += char

    print(f"The {direction}d text is {result}")


while running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    caesar(text, shift, direction)

    status = input(
        "\nType 'yes' if you want to go again. Otherwise type 'no'.\n"
    ).lower()

    if status == "no":
        running = False
        print("Goodbye!")
