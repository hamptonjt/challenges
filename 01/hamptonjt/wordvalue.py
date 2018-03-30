from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    words_file = open(DICTIONARY, 'r')
    words = words_file.read()
    words_file.close()
    return words.split()


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    letters = list(word.upper())
    sum = 0
    for l in letters:
        if l.isalpha():
            sum += LETTER_SCORES[l]
    return sum


def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    max_word = ''
    old_max = 0

    if words == None:
        words = list(load_words())

    for word in words:
        val = calc_word_value(word)
        if val > old_max:
            max_word = word
            old_max = val

    return max_word


if __name__ == "__main__":
    pass  # run unittests to validate
