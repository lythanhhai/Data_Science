#!/usr/bin/env python
"""
This a an example module.
"""
import sys, os

__PUNCTUATION__ = ".,?!%"

def introduce(family = "Ly", first = "Thanh Hai"): 
    """
    This a an example function.
    """
    print("Ho va ten: " + family + " "+ first)

def count_word(lines):
    freqDict = {}
    for line in lines:
        words = line.split()
        for word in words:
            word_copy = ""
            for normal_letter in word:
                if normal_letter in __PUNCTUATION__:
                    continue
                else:
                    word_copy += normal_letter
            word = word_copy
            if word in freqDict:
                freqDict[word] += 1
            else:
                freqDict[word] = 1
    # print("File co tat ca %d tu" % len(freqDict))
    # print("Bang tan suat xuat hien cac tu:")
    # print(freqDict)
    return freqDict

def count_sentence(lines):
    freqDict = {}
    new_document = ""
    #print(lines[0][:-1])
    for index in range(0, len(lines)):
        if index == len(lines) - 1: 
            new_document += lines[index][:-1]
        else:
            new_document += lines[index][:-1] + " "

    for sentence in new_document.split("."):
        if sentence in freqDict:
            freqDict[sentence] += 1
        else:
            freqDict[sentence] = 1

    # print("File co tat ca %d cau" % len(freqDict))
    # print("Bang tan suat xuat hien cac cau:")
    # print(freqDict)
    return freqDict

def main():
    """
    Main function
    """
        
    #===== process command-line arguments =====#
    strUsage = 'Usage: module1.py path_to_text_file'
    if len(sys.argv) != 2:
        sys.exit(strUsage)   
    filePath = sys.argv[1]      
    try:
        with open(filePath, 'r', encoding='utf8') as f:
            lines = f.readlines()
            #print(lines)
    except IOError:
        sys.exit('ERROR: Failed to load input file ' + filePath)
    
    #count_word(lines)
    #count_sentence(lines)
    end_program = False
    while not end_program:
        your_choice = int(input("Please enter your choice(1 for count sentences, 2 for count word, 3 for print frequently word, 4 for word apperance one times): "))
        if your_choice == 1:
            print("File co tat ca %d cau" % len(count_sentence(lines)))
        elif your_choice == 2:
            print("File co tat ca %d tu" % len(count_word(lines)))
        elif your_choice == 3:
            print("Bang tan suat xuat hien cac cau:")
            print(count_word(lines))
        elif your_choice == 4:
            freDict_Copy = {}
            for word in count_word(lines):
                if count_word(lines)[word] == 1:
                    freDict_Copy[word] = 1
            print(freDict_Copy)
        else:
            end_program = True

 
#===== This module is to be run as the top-level script =====
if __name__ == "__main__":
    main()
    
