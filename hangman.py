import random
from words import words
import string

live =int(input("Enter the no of Lives u needed to guess the word : "))
def get_system_guessed_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    #print(1)
    while "-" in word or " " in word:
        word = random.choice(words)
        #print(2)
    return word.upper()
def hangman():
    #print("3")
    word=get_system_guessed_word(words)
    #print(4)
    print("System choosen randown word is :",word)
    word_letters=set(word)#letters in the system guessed word
    print(word_letters)
    alphabet=set(string.ascii_uppercase)
    used_letters=set()#for taracking the letters what user have guessed
    lives=live
    while len(word_letters)>0 and lives >0 :
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(" ")
            else:
                lives=lives-1
                print('\nYour letter,', user_letter, 'is not in the word.')
        elif user_letter in used_letters:
           print('\nYou have already used '+user_letter +' letter. Guess another letter.')
        else:
            print('\nThat is not a valid letter.')
    if lives==0:
        print("U have exceeded the limit ,U are dead")
    else:
        print('YAY! You guessed the word', word, '!!')

if __name__=='__main__':
    hangman()
