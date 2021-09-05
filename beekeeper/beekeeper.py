from sys import stdin


vowel_pairs = ["aa", "ee", "ii", "oo", "uu", "yy"]
vowels = ["a", "e", "i", "o", "u", "y"]


def number_of_vowels(word):
    number_of_vowels = 0
    for x, i in enumerate(word[:-1]):
        if i in vowels and word[x + 1] == i:
            number_of_vowels += 1
    return number_of_vowels


number_of_words = stdin.readline()

while number_of_words != "":
    if int(number_of_words) == 0:
        break
    max_vowels = 0
    best_word = ""
    for _ in range(int(number_of_words)):
        new_word = stdin.readline()[:-1]
        new_vowels = sum([new_word.count(x) for x in vowel_pairs])
        if max_vowels <= new_vowels:
            max_vowels = new_vowels
            best_word = new_word
    print(best_word)
    number_of_words = stdin.readline()
