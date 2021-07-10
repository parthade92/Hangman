import random as r
word_list = ['apple', 'mango', 'litchi', 'banana', 'pear']
chosen_words = r.choice(word_list)
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
man = ['''
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
print(logo)
print(chosen_words)  # testing purpose
stage = 6
length = len(chosen_words)
display = []
for i in range(length):
    display.append('_')
end = False
while not end:
    guess = input("\nGuess a letter: ").lower()
    for i in range(length):
        if chosen_words[i] == guess:
            display[i] = guess
        else:
            pass
    print(display)
    if guess not in chosen_words:
        stage -= 1
        print(f"You've guessed {guess}, that's not in the word.")
        if stage == 0:
            end = True
            print("You Lose.")
    if "_" not in display:
        end = True
        print("You Win")
    print(man[stage])
    print(f'Lives Left: {stage}')
