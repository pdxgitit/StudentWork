text = input('Type text you wish to encrypt: ')
keyword = input('Type desired keyword, 5 characters in length: ')
letter_list = list('abcdefghijklmnopqrstuvwxyz')
# print(letter_list.index('d'))
# zero = keyword[0]
# one = keyword[1]
# two = keyword[2]
# three = keyword[3]
# four = keyword[4]
# p0 = keyword.index(zero)
# p1 = keyword.index(one)
# p2 = keyword.index(two)
# p3 = keyword.index(three)
# p4 = keyword.index(four)


def remove_spaces(x):
    no_spaces_string = ''
    for char in x:
        if char not in ' ,./?!@#$%^&*():;\'"':
            no_spaces_string += char
    return no_spaces_string.lower()

print(remove_spaces(text))

def letters_to_nums():
    key_num_list = []
    for char in keyword:
        key_num_list.append((letter_list.index(char)))
    return key_num_list

key_list = letters_to_nums()

print(letters_to_nums())

def letter_num():
    txt_num_list = []
    for char in remove_spaces(text):
        txt_num_list.append(letter_list.index(char))
    return txt_num_list

print(letter_num())

text_list = letter_num()

def pack_coset(kw,array):
    length = len(kw)
    nested_list = []
    for n in range(length):
        nested_list.append(array[n::length])
    return nested_list

nested_list = (pack_coset(keyword, text_list))

def coset_shift(nested_list, key_list):
    for n in range(len(nested_list)):
        val = key_list[n]
        for i, x in enumerate(nested_list[n]):
            if val + x > 25:
                x -= 26
            nested_list[n][i] = val + x
    return nested_list
nested_list = coset_shift(nested_list, key_list)

def num_to_letter(nested_list, letter_list):
    alpha_list = []
    beta_list = []
    for lst in nested_list:
        for num in lst:
            beta_list.append(letter_list[num])
        alpha_list.append(beta_list)
        beta_list = []
    return alpha_list
print(num_to_letter(nested_list, letter_list))
