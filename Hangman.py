import random

word_list = ['aardvark', 'baboon', 'camel', 'abruptly', 'absurd', 'abyss', 'affix', 'askew', 'buzzing', 'buzzwords', 'caliph', 'cockiness']


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)

word = random.choice(word_list).lower()

chosen_word = []

for x in range(0, len(word)):
    chosen_word.append('_')

print(chosen_word)

count = 6

while count >= 0:
    guess = input('guess a letter: ').lower()
    if guess in chosen_word:
        print(f'{guess} is already exist. plz try different letter')

    if guess in word:
        for x in range(len(word)):
            if word[x] == guess:
                chosen_word[x] = guess
                # print(' '.join(chosen_word))
            else:
                continue
    else:
        print(stages[count])
        count -= 1

    print(' '.join(chosen_word))
    if '_' not in chosen_word:
        print('you won')
        break

else:
    print('you lose')
    print(f'{word} is the correct word')