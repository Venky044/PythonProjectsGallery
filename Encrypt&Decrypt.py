alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def game():
    direction = input("Type 'encrypt' to encode, type 'decrypt' to decode:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    return direction, text, shift


def encryption(texts, shift_no):
    encoded_word = []
    for word in texts:
        if word.isalpha():
            position = alphabet.index(word)
            position += shift_no
            letter = alphabet[position]
            encoded_word.append(letter)
        else:
            encoded_word.append(word)
    print("encrypted text is: ", "".join(encoded_word))


decoded_word = []


def decryption(texts, shift_no):
    for word in texts:
        if word.isalpha():  # or word in alphabet
            position = alphabet.index(word)
            position -= shift_no
            letter = alphabet[position]
            decoded_word.append(letter)
        else:
            decoded_word.append(word)


game_on = True

while game_on:
    direction, text, shift = game()

    if direction == "encrypt":
        encryption(text, shift)
    elif direction == "decrypt":
        decryption(text, shift)
        print("decrypted text is: ", "".join(decoded_word))
    else:
        print("you enter the wrong direction")

    play = input("do you want to continue? say Y or N: ").lower()
    if play == "y":
        game_on = True
    else:
        game_on = False

# -----------------------------------------------------------------

# _______________SHORTEST FORM_________________

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
#             'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
#             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
#
# def game():
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
#     return direction, text, shift
#
#
# def coding(texts, shifl_no, direction):
#     encode = ''
#     for word in texts:
#         if word.isalpha():
#             position = alphabet.index(word)
#
#             if direction == 'encrypt':
#                 position += shifl_no
#             else:
#                 position -= shifl_no
#             encode += alphabet[position]
#         else:
#             encode += word
#     print(f'{direction} of the text is: {encode}')
#
#
# game_on = True
#
# while game_on:
#     direction, text, shift = game()
#
#     coding(text, shift, direction)
#     play = input('do you want to continue? say Y or N: ').lower()
#     if play == 'y':
#         game_on = True
#     else:
#         game_on = False
