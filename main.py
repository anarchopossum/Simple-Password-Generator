from random_word import RandomWords
from random import randrange

random_word = RandomWords()
# print(random_word.get_random_word())

def passphrase_gen():
    word_count = 0
    while not (1 <= word_count <= 9 and str(word_count).isdigit()):
        word_count = int(input("Enter the amount of words you would like to have\n (1 to 9 Words): "))

    char_spacer = ""
    while (char_spacer == "" or char_spacer.isalnum()):
        char_spacer = input('Please enter a special character to divde\n the words for your password. example:(".","$","!"): ')
    
    add_num = input("Would you like to add a random number into your password (y/n): ").lower()

    input("The program will now generate a password that has " + str(word_count) + " word(s) in it.\nPress Enter to Generate...")
    password = ""

    num_pos = randrange(word_count-1)
    if word_count == 1: 
        num_pos = 0
        

    for i in range(word_count):
        password += random_word.get_random_word()
        if add_num == 'y' and num_pos == i:
            password += str(randrange(100))
        if i != word_count-1:
            password += char_spacer
    print(password)

# --------------------------------------------------------
print('\n==================================================================================================')
print('.dP"Y8 88 8b    d8 88""Yb 88     888888    88""Yb    db    .dP"Y8 .dP"Y8     dP""b8 888888 88b 88 ')
print('`Ybo." 88 88b  d88 88__dP 88     88__      88__dP   dPYb   `Ybo." `Ybo."    dP   `" 88__   88Yb88 ')
print('o.`Y8b 88 88YbdP88 88"""  88  .o 88""      88"""   dP__Yb  o.`Y8b o.`Y8b    Yb  "88 88""   88 Y88 ')
print('8bodP" 88 88 YY 88 88     88ood8 888888    88     dP""""Yb 8bodP" 8bodP"     YboodP 888888 88  Y8 ')
print('==================================================================================================\n')
print('Please Make a selection for what type of password you would like to generate:\n')
print('1. PassPhrase - This will let generate a password with multiple english words with special and Numerical characters too')
print('2. Char Scramble - This will use random characters such as letters, numbers and special characters\n')
print('please make a selection!')
passphrase_gen()
