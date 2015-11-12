import random


def messup(words):
    """
        Messes up the inner spelling of words. To test this theory:
            https://en.wikipedia.org/wiki/Typoglycemia

        It's a lot harder to read than the exapmles online...
    """

    result = ''
    sub_word = ''

    for char in words + ' ':
        if char.isalpha():
            sub_word += char
        else:
            if len(sub_word) > 3:
                result += sub_word[0]
                result += ''.join(random.sample(sub_word[1:-1], len(sub_word)-2))
                result += sub_word[-1]
            else:
                result += sub_word
            sub_word = ''

            result += char

    return result[:-1]


def main():
    while True:
        print(messup(input()))


if __name__ == '__main__':
    main()
