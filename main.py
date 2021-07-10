import random as r
word_list = ['apple', 'mango', 'litchi', 'banana', 'pear']
chosen_words = r.choice(word_list)
print(chosen_words)
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
    if "_" not in display:
        end = True
        print("You Win")
    else:
        pass
