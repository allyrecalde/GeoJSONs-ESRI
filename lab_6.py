def display_menu():
    print('Menu\n')
    print('-------------\n')
    print('1. Encode\n')
    print('2. Decode\n')
    print('3. Quit\n')

def encode(password):
    encoded = ''
    for char in password:
        encoded += str(int(char) + 3 % 10) #make each character in password and integer, then add them together into a string
    return encoded #return string

def decode(password):
        decoded = ''
        for char in password:
            decoded += str(int(char) - 3 % 10)
            return decoded

password = '' #start password as empty string
option = 0 # starting off point

while option != 3:

    display_menu()
    option = int(input('Please enter an option: \n'))

    if option == 1:
        password = input('Please enter your password to encode: \n')
        if len(password) != 8 or not password.isdigit:
            print('Invalid password')
        else:
            password1 = encode(password)
            print('Your password has been encoded and stored!\n')
    elif option == 2:
        password2 = encode(password)
        print(f'The encoded password is {password2}, and the original password is {password}.')
    elif option == 3:
        break
    else:
        print('Invalid option, please select option 1, 2, or 3.')




