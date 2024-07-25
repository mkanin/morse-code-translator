import pytest

from main import encode
from main import encode_word
from main import decode
from main import decode_word


@pytest.mark.parametrize(
    "word, exp_letter_codes",
    [
        ("", ""),
        ("ABC", ".- -... -.-."),
        ("CBA", "-.-. -... .-"),
    ]
)
def test_encode_word(word, exp_letter_codes):
    letter_codes = encode_word(word)
    assert letter_codes == exp_letter_codes


@pytest.mark.parametrize(
    "letters_code, exp_word",
    [
        ("", ""),
        (".- -... -.-.", "ABC"),
        ("-.-. -... .-", "CBA"),
    ]       
)
def test_decode_word(letters_code, exp_word):
    word = decode_word(letters_code)
    assert word == exp_word


@pytest.mark.parametrize(
    "sentence, exp_code",
    [
        ("", ""),
        ("ABC", ".- -... -.-."),
        ("ABC CBA", ".- -... -.-. -.-. -... .-"),
    ]
)
def test_encode(sentence, exp_code):
    code = encode(sentence)
    assert code == exp_code


@pytest.mark.parametrize(
    "code, exp_sentence",
    [
        ("", ""),
        (".- -... -.-.", "ABC"),
        (".- -... -.-.  -.-. -... .-", "ABC CBA"),
    ]
)
def test_decode(code, exp_sentence):
    sentence = decode(code)
    assert sentence == exp_sentence
