import string
from words import choose_word
from images import IMAGES
# End of helper code
# ==========================================
def is_word_guessed(secret_word,letters_guessed):
    """
    secret word : ek string word h jo ki user ko guess karna h
    letters_guessed = ek list h, jisme wo letter h jo ki user nai abhi tak guess kare
    return: return true kare agar saare letters jo ki user ne guess kiye h wo secret_word m h.warna no
    False othervise
    """

    if secret_word==get_guessed_word(secret_word,letters_guessed):
        return True
    return False
# Iss function ko test karne ke liye aap get_guessed_word(*kindness',[k,n,d]) call kr skte h
def get_guessed_word(secret_word,letters_guessed):
    '''
    secret word : ek string word h jo ki user ko guess karna h
    letters_guessed = ek list h, jisme wo letter h jo ki user nai abhi tak guess kare
    returns: ek string return karni hai jisme wo letter h jo sahi guess huye ho anf baki jagah underscore ho
    to hum return karenge "k_n_n_ss")
    '''
    index=0
    guessed_word=""
    while index<len(secret_word):
        if secret_word[index] in letters_guessed:
            guessed_word+=secret_word[index]
        else:
            guessed_word+="_"
        index+=1
    return guessed_word
def get_available_letters(letters_guessed):
    '''
    letters_guessed = ek list h, jisme wo letter h jo ki user nai abhi tak guess kare
    returns: string, hume  ye return karna hai kaun kaun se letters aapne nhi guess kare abhi tak
    eg agar letter guessed =['e','a'] hai to humne baki character return karne hai
    jo ki 'bcdfghijklmnopqrstuvwxyz' ye hoga
    '''
    import string
    letters_left=string.ascii_lowercase
    i=0
    alphabet=""
    while i<len(letters_left):
        if letters_left[i]!=letters_guessed:
            alphabet=alphabet+letters_left[i]
        i+=1
    return alphabet
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Hangman game yeh start karta hai:

    * Game ki shuruaat mei hi, user ko bata dete hai ki
      secret_word mei kitne letters hai

    * Har round mei user se ek letter guess karne ko bolte hai

    * Har guess ke baad user ko feedback do ki woh guess uss
      word mei hai ya nahi

    * Har round ke baar, user ko uska guess kiya hua partial word
      display karo, aur underscore use kar kar woh letters bhi dikhao
      jo user ne abhi tak guess nahi kiye hai

    '''
    print ("Welcome to the game, Hangman!")
    print ("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print ("")

    letters_guessed = " "
    chance=8
    print(secret_word)
    i=0
    while chance>0:
        available_letters=get_available_letters(letters_guessed)
        print("Available letters: "+ available_letters)
        guess=input("Please guess a letter: ")
        letter=guess.lower()
        if letter in secret_word:
            letters_guessed = letters_guessed+letter
            print ("Good guess: "+" "+str(get_guessed_word(secret_word, letters_guessed)))
            print ("")
            if is_word_guessed(secret_word, letters_guessed) == True:
                print (" * * Congratulations, you won! * * ")
                print ("")
                break
        else:
            print ("Oops! That letter is not in my word: "+" "+str(get_guessed_word(secret_word, letters_guessed)))
            chance=chance-1
            print("You have "+str(chance)+" more chance to get letter")
            print(IMAGES[i])
            i=i+1
            letters_guessed = letters_guessed+letter
            print(" ")
    else:
        print("Sorry you have lost your "+ " "+ "Your secret word was"+" "+secret_word)
secret_word = choose_word()
hangman(secret_word)