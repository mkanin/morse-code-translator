import re


def encode_word(word):
    letters = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
    }

    letter_codes = [letters.get(letter, "") for letter in word]

    return " ".join(letter_codes)


def encode(sentence):
    words = sentence.split()
    codes = [encode_word(word) for word in words]

    return "  ".join(codes)


def decode_word(encoded_word):
    morse_codes = {
        ".-": "A",
        "-...": "B",
        "-.-.": "C",
    }

    codes = encoded_word.split()
    letters = [morse_codes.get(code, "") for code in codes]

    return "".join(letters)


def decode(encoded_sentence):
    encoded_words = re.split(r'\s{2}', encoded_sentence)
    words = [decode_word(encoded_word) for encoded_word in encoded_words]

    return " ".join(words)
