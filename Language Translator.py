# Johnny Geng, johnnyge@usc.edu

# Description:
# This program is a language translator that translates certain English words to certain languages.


# getLanguages(fileName)
# Parameter: a string containing the name of a CSV file to read from
# and it has a default value of "languages.csv"
# Return value: a list of strings representing the languages in the header row
# Open the CSV file and get the header row with the languages and put it into a list.
# Close the file and return the list
def getLanguages(fileName):
    fileIn = open(fileName, "r")
    languages = fileIn.readline()
    langList = languages.split(",")
    fileIn.close()
    return langList


# getSecondLanguage(langList)
# Parameter: langList is a list of the languages
# Return value: a string for the second language
# Display to the user the languages that are available for translation.
# Get input from the user for the second language. They must enter in a valid
# language. The user’s input is not case sensitive.
# Return the language.
def getSecondLanguage(langList):
    print("Translate English words to one of the following languages:\n"
          "\tDanish Dutch Finnish French German Indonesian Italian\n"
          "\tJapanese Latin Norwegian Portuguese Spanish Swahili Swedish")
    langStr = input("Enter a language: ")
    while not langStr.capitalize() in langList:
        print("This program does not support", langStr)
        langStr = input("Enter a language: ")
    return langStr.capitalize()


# readFile(langList, langStr, fileName)
# Parameter 1: langList is a list of the languages
# Parameter 2: langStr is a string of containing the name of a language and it has
# a default value of "English"
# Parameter 3: fileName is a string containing the name of a CSV file to read from
# and it has a default value of "languages.csv"
# Return value: a list of words in the language identified by the langStr parameter
# Open the CSV file and read the header row to skip it.
# Use the langList and langStr parameters to determine which column of data to save.
def readFile(langList, langStr, fileName):
    fileIn = open(fileName, "r")
    fileIn.readline()
    numColumn = langList.index(langStr)
    outputList = []
    for line in fileIn:
        line = line.strip()
        wordList = line.split(",")
        word = wordList[numColumn]
        outputList.append(word)
    fileIn.close()
    return outputList


# createResultsFile(language, resultsFile)
# Parameter 1: language is a string containing the name of the second language
# Parameter 2: resultsFile is a string containing the name of the results file
# Return value: none
# Open the results text file such that if there is an existing file, it will be overwritten.
# Write text to the file stating the second language.
# Close the file.
def createResultsFile(language, resultsFile):
    fileOut = open(resultsFile, "w")
    print("Words translated from English to " + language, file=fileOut)
    fileOut.close()


# translateWords(englishList, secondList, resultsFile)
# Parameter 1: englishList is a list of words in English
# Parameter 2: secondList is a list of words in the second language
# Parameter 3: resultsFile is a string containing the name of the text file
# Return value: none
# Open the results file in order to append text into it.
# Ask the user to enter an English word to translate.
# If the word is not in the English list, then display a message to the user.
# Translate the word. If there is a translation, then display a message to the user
# and write the word and its translation to the file.
# Example message: rabbit is translated to kani
# Example text to file: rabbit = kani
# If there is no translation (i.e., the value is "-"), then display a message to the
# user.
# Ask the user if they want to translate another word and repeat until they
# answer "n" (case insensitive).
# Close the file.
def translateWords(englishList, secondList, resultsFile):
    fileOut = open(resultsFile, "a")
    englishWord = input("\nEnter a word to translate: ")
    if englishWord.lower() in englishList:
        orderNum = englishList.index(englishWord.lower())
        secondWord = secondList[orderNum]
        if secondWord == "-":
            print(englishWord, "did not have a translation.")
        else:
            print(englishWord, "is translated to", secondWord)
            print(englishWord + " = " + secondWord, file=fileOut)
    else:
        print(englishWord, "is not in the English list.")
    error = True
    while error:
        repeat = input("Another word (y or n)? ")
        if repeat.lower() == "y" or repeat.lower() == "n":
            error = False
    while repeat.lower() == "y":
        englishWord = input("\nEnter a word to translate: ")
        if englishWord.lower() in englishList:
            orderNum = englishList.index(englishWord.lower())
            secondWord = secondList[orderNum]
            if secondWord == "-":
                print(englishWord, "did not have a translation.")
            else:
                print(englishWord, "is translated to", secondWord)
                print(englishWord + " = " + secondWord, file=fileOut)
        else:
            print(englishWord, "is not in the English list.")
        error = True
        while error:
            repeat = input("Another word (y or n)? ")
            if repeat.lower() == "y" or repeat.lower() == "n":
                error = False
    fileOut.close()


# Call the function you created to get the list of languages
# Call the appropriate function to read the CSV file for the English words.
# Call the appropriate function to get the second language.
# Call the appropriate function to read the CSV file for that language.
# Ask the user to enter a name for the results file. Use the second language with
# ".txt" as a default file name. If the second language is Italian, then the default
# file name is "Italian.txt". If the user enters only the enter/return key, use the
# default name.
def main():
    print("Language Translator")
    langList = getLanguages("languages.csv")
    englishList = readFile(langList, "English", "languages.csv")
    language = getSecondLanguage(langList)
    secondList = readFile(langList, language, "languages.csv")
    resultsFile = input("Enter a name for the results file (return key for "
                        + language + ".txt): ")
    if resultsFile == "":
        resultsFile = language + ".txt"
    createResultsFile(language, resultsFile)
    translateWords(englishList, secondList, resultsFile)
    print("Translated words have been saved to", resultsFile)


main()