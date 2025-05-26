def add(*numbers):
    return sum(numbers)


DIGIT_TO_WORD_MAPPING = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}


def digit_to_word(digit):
    return DIGIT_TO_WORD_MAPPING[digit]


def word_to_digit(word):
    return DIGIT_TO_WORD_MAPPING.index(word)
