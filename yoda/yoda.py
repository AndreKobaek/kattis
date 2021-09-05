from sys import stdin

input = stdin.readlines()
word1 = list(input[0][:-1])
word2 = list(input[1][:-1])


def compare_chars(char1, char2):
    if int(char1) >= int(char2):
        return char1
    return ''


def compare_char_lists(char_list_1, char_list_2):
    return_list = char_list_1.copy()
    compare_list = char_list_2.copy()
    while len(return_list) > len(compare_list):
        compare_list.insert(0, '0')
    while len(return_list) < len(compare_list):
        return_list.insert(0, '0')
    for i in range(len(return_list)):
        return_list[i] = compare_chars(return_list[i], compare_list[i])
    if len("".join(return_list)) == 0:
        return "YODA"
    return_list = int("".join(return_list))
    return return_list


print(compare_char_lists(word1, word2))
print(compare_char_lists(word2, word1))
