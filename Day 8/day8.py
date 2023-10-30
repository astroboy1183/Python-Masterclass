import string


def encode_decode_string(inp, n):
    new = ''
    for char in inp:
        if 97 <= ord(char) <= 122:
            new += (chr((ord(char) + n - 97) % 26 + 97))
        elif 65 <= ord(char) <= 90:
            new += (chr((ord(char) + n - 65) % 26 + 65))
        else:
            new += char
    return new


end = False

while not end:
    input_type = input("Do you want to encode or decode?").lower()
    if input_type != "encode" and input_type != "decode":
        print("Invalid input!")

    if input_type == "encode":
        user_input = input("Enter the string to encode")
        n = int(input("Enter the shift number:"))
        print(encode_decode_string(user_input, n))
    else:
        user_input = input("Enter the string to encode")
        n = int(input("Enter the shift number:"))
        print(encode_decode_string(user_input, -n))

    cont = input("Do you want to continue? y or n").lower()
    if cont == "n" or cont == "no":
        end = True

# print(ord(' '))
