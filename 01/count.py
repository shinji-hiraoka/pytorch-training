from function import add

def count_word(text, char):
    assert isinstance(text, str)
    assert isinstance(char, str) and len(char) == 1

    count = 0

    for c in text:
        if c == char:
            count = add(count, 1)

    return count