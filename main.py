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

passphrase_gen()
