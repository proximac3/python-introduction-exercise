def print_upper_words(words):
    """ print word in a list in uppercase with a line break 
    after every word"""

    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())
            print('\n')

print_upper_words(["egg", "hey", "goodbye", "yo", "yes"])


def general_print_upper_words(words, must_start_with){
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper)
                break
}