import random 
import os

def run ():
    IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

    DB = [
        'LEON',
        'LUCIO',
        'NICOLAS',
        'BENJAMIN',
        'CARRANZA',
        'JONATHAN',
        'YASMIN',
        'DAIANA',
        'HODARA'
    ]

    word = random.choice(DB)
    spaces = ["_"] * len(word)
    attemps = 8

    while True:
        os.system('cls')
        for character in spaces:
            print (character, end= " ")
        print (IMAGES[attemps])    
        letter = input("ELIGE UNA LETRA: ").upper()

        found = False
        for idx, character in enumerate(word):
            if character == letter:
                spaces[idx] = letter 
                found = True

        if not found:
            attemps -= 1
        
        if "_" not in spaces:
            os.system('cls')
            print('GANASTEEE!!')
            break
            input()

        if attemps == 0:
            os.system('cls')
            print('PERDISTE')    
            break
            input()



if __name__ == '__main__':
    run()