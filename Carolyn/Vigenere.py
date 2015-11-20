text = input('Type text you wish to encrypt: ')
keyword = input('Type desired keyword, 5 characters in length: ')
letter_list = list('abcdefghijklmnopqrstuvwxyz')
# print(letter_list.index('d'))
zero = keyword[0]
one = keyword[1]
two = keyword[2]
three = keyword[3]
four = keyword[4]
p0 = keyword.index(zero)
p1 = keyword.index(one)
p2 = keyword.index(two)
p3 = keyword.index(three)
p4 = keyword.index(four)


def remove_spaces():
    no_spaces_string = ''
    for char in text:
        if char != ' ' and char != ',' and char != '.' and char != '!':
            no_spaces_string += char
    return no_spaces_string.lower()

# print(remove_spaces())

def letters_to_nums():
    key_num_list = []
    for char in keyword:
        key_num_list.append((letter_list.index(char)))
    return key_num_list

key_list = letters_to_nums()
shift_one = key_list[0]

print(letters_to_nums())


def letter_num():
    txt_num_list = []
    for char in remove_spaces():
        txt_num_list.append(letter_list.index(char))
    return txt_num_list

print(letter_num())

text_list = letter_num()
coset_one = text_list[::5]
coset_two = text_list[1::5]
coset_three = text_list[2::5]
coset_four = text_list[3::5]
coset_five = text_list[4::5]
# print(coset_one)
# print(coset_two)
# print(coset_three)
# print(coset_four)
# print(coset_five)
coset_shift_one = []
def coset_shift():
    for item in coset_one:
        coset_shift_one.append(item + shift_one)
    return coset_shift_one
print(coset_shift)
