##pig latin
#idea is to find the first constanant group (letters before first vowel) remove from the start of the word, add to the end and ad "ay"
#piglatin

import re

def takeUserWord():

    while True:
        word = str.lower(input("Enter word: "))



        if not len(word) < 2 and re.match("[a-z]", word):
            #print ("Word must be more than 2 and a-z only!")
            return word


            elif not all word in
            #for i in range (0, len(word)):
             #   if word[i] in "abcdefghijklmnopqrstuvwxyz":

              #      return word




def findfirstvowel(word): #checks if first letter of word is a vowel
    i = 0
    if word[i] not in "aeiou":
        i +=1
    return i  ##returns i = 0 if first letter was a vowel.

def translate (word):
    i = findfirstvowel(word)
    if i == 0:   ## if first letter was a vowel, just ad "ay"
        return word + "yay"
    elif i != 0: ## modifies based on position of first vowel
        return word[i:]+word[:i] + "ay"

    '''
    cluster = word[: i] #+1?
    core = word [i : ]
    print ("translation for ", word, "is: ", core+cluster + "ay")
    '''
    ##or could just return the values neededreturn
    # print ("translation for ", word, "is: ", word[i:]+word[:i] + "ay")
    return word[i:]+word[:i] + "ay"




def main():
    #word = str(input("Enter word: "))
    #translate(word)
    word = takeUserWord()
    print ("translation for ", word, "is: ", translate(word))





main()