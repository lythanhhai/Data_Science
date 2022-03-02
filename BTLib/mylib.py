def count_word(file):

    infile = open(file, "r")

    split_string = infile.read().split()
    string_dict = {}

    for word in split_string:
        string_dict[word] = 0

    for word in split_string:
        if word in string_dict.keys():
            string_dict[word] = string_dict[word] + 1

    print(string_dict)
    infile.close()

def count_sentence(file):

    infile = open(file, "r")

    split_string = infile.read().split('.')
    string_dict = {}

    for sentence in split_string:
        string_dict[sentence] = 0

    for sentence in split_string:
        if sentence in string_dict.keys():
            string_dict[sentence] = string_dict[sentence] + 1

    print(string_dict)
    infile.close()

#Main Program
name_infile = input("Enter the name of a text file: ")
count_word(name_infile)
count_sentence(name_infile)
