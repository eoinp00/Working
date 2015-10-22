import random #importing random to allow random gneration of word from list.


HANGMANPICS = ['''
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


#wordList = "cunning bats problem avacado boxing bright elbow knowlege strings integers mistake parsing error guitar road brick".split()  # SPLIT at end defaults as splitting where the space is and turning into a list.
#wordList = "cunning bats".split()

#List = open("filename.txt").readlines()

def pickRandomWord(fname):      #.readlines(), #line.split(), #for i in fname:  wordList.append(i.rstrip().split(','))
    wordList = open(fname).readlines()
    wordIndex = random.randint(0, len(wordList)-1)
    word = wordList[wordIndex]
    #print (word)
    return word

def changeWordToStars (word):
    starVersionOfWord = "*" * len(word)     #creates starVersionOfWord list of starts (*) by multiplying the string value '*' by the amount of letters in the variable word.
    starVersionOfWord = list(starVersionOfWord)         # this converts the '*' version of the word into a list, to allow better indexing and replacing of letters, also comparing of lists.
    return starVersionOfWord

def convertStarsToList (starVersionOfWord):
    listStarVersionOfWord = list(starVersionOfWord)
    return listStarVersionOfWord

'''
def pickRandomWord(fname):
    wordList = []
    with open(fname) as inputfile:
        for line in inputfile:
            wordList.append(line.split())
    wordIndex = random.randint(0, len(wordList)-1)
    word = wordList[wordIndex]
    print (word)
    return word
'''

'''
def pickRandomWord (wordList):  # paramter is the list created above (which has been "split" where space are and turned into a list. Thus allowing indexing
    wordIndex = random.randint(0, len(wordList)-1)  #creating a varaible to use to pick a word at a random index. -1 as otherwise list index out of range
    word = wordList[wordIndex] # creates word variable (to be returned and used elsewhere) by calling the string that is at the index position in the word list.
    return word   #OTHER OPTION ##RANDOM.CHOICE(WORDLIST).LOWER WOULD WORK TOO??
'''

'''def pickRandomWord (wordList):
    wordList = importfromtxt()
    word = random.choice(wordList).lower
    return word
'''

def compareGuess (listStarVersionOfWord, word, word_listversion): # function asks for letter, compares against secret word
    print (listStarVersionOfWord)
    guesses_made = []
    lives = 6  #defined lives outside of while loop. this figure will reduce every time a wrong guess is made. when it hits 0, the loop below ends, printing line 36 "the end"



    while(lives > 0 and listStarVersionOfWord != word_listversion): # as long as the user has lives, and the blank word(which is a list) does not match the random word (also converted to a list) this will loop
        image_to_display = int(6 - lives)
        print (HANGMANPICS[image_to_display])
        print ("lives = ", lives)   #prints lives, a variable assigned in this function, but outside of this while loop.
        print ("guesses made so far", guesses_made) #prints guesses made , an empty list assigned in this function, but outside of this while loop.
        while True:     #Sets loop to true (means it will loop infinitely until value returns as "false" or told to break. ASKS USER FOR INPUT
            guess = str.lower(input("enter letter or guess full word: "))   ## asks for input, converts to lower case.
            if guess in guesses_made:       #if the user input is in the guesses made list (defined above) it will NOT break the true loop as it REMAINS TRUE.
                print ("You have already guessed this, no lives lost. Guess again.")
                print ("guesses made so far", guesses_made)
            elif guess not in "abcdefghijklmnopqrstuvwyxz":
                print ("Please enter VALID letter")
            elif guess in "abcdefghijklmnopqrstuvwyxz" or word:  #other wise, if user input is a letter or is in the word (so as letter combinations that are included in the word are accepted
                guesses_made.append(guess)              # this takes what the user has just input and adds it to the guesses made list, only if it satisfyes conditions before.
                break           # if above happens, conditions are satisfied and while loop breaksm going on to the if conditions below.

        print(listStarVersionOfWord)   ## this prints blank at start of guess

        if guess == word:    # correct guess # if full word guessed correctly. will print full word (list version) and break loop to end game.
            print (list(word))
            print ("Great guess! You won the game! http://linuxart.com/stuff/gnome/gegl.png ")
            break
        elif guess in word:   # letter in word # otherwise, if the user input is in the word  it will loop through to replace '*' with correct letter
            for i in range(len(word)):  #  i loops through the range of the word, range being defined as th length of the word.(i being the int that represents the position of the loop inside of the range),
                if guess == word[i]:    #if the user input matches exactly the letter that is in the word at i, then it will....
                    listStarVersionOfWord[i] = guess    #... replace the '*' that is in the same position that was just checked above. So 3rd * will be replaced with user input, IF the user input matched the 3rd LETTER of the Word
                    print ("congratulations, correct guess")
                    print(listStarVersionOfWord)        #prints new version of blank that has just been amended to include letter (if matched)
        elif guess not in word:     # letter not in word
            print ("sorry, wrong guess")
            lives -= 1 # this removes a life from the accumular defined at the begining of this function(def compareGuess (blank, word, word_listversion))

def main():

    #pickRandomWord (wordList) # runs function that picks random word from list
    #word = pickRandomWord (wordList) #defines variable word which is apart of function "def pickRandomWord (wordList)"
    #pickRandomWord("listofwords.txt")
    word =  pickRandomWord("listofwords.txt")
    starVersionOfWord = changeWordToStars (word)
    listStarVersionOfWord = convertStarsToList (starVersionOfWord)

    word_listversion = list(word)  #converst variable "word" into a list. This allows us to better calculate index of each letter and compare vs other lists..
    '''blank = "*" * len(word)     #creates blank list of starts (*) by multiplying the string value '*' by the amount of letters in the variable word.
    blank = list(blank)         # this converts the '*' version of the word into a list, to allow better indexing and replacing of letters, also comparing of lists.
    '''

    compareGuess (listStarVersionOfWord, word, word_listversion )  #this runs function where most of the work for the game is happening.

    print("THE END")

    playAgain = str.lower(input("Would you like to play again?")) ## play again, if yes, run main.
    if playAgain in "yes":
        main()



    print ("Goodbye")
main()