# Given two text files containing numbers, return a list of the numbers
# that they share.  (Use happy.txt and primes.txt)

# This requires: reading a file, converting from strings to integers
# and some list manipulation

a_file = open('happy.txt', encoding='utf-8')
a_string = a_file.read()
a_file.close()

b_file = open('primes.txt', encoding='utf-8')
b_string = b_file.read()
b_file.close()
#open primes.text
#convert strings to integers
#
a_list = a_string.split('\n')
b_list = b_string.split('\n')

string_list = []
print(a_list)
print(b_list)

for a_num in a_list:
    for b_num in b_list:
        if a_num == b_num:
            string_list.append(a_num)

def cleanup(x):
    listt = []
    for char in x:
        if char != '':
            listt.append(int(char))
    return listt

int_list = cleanup(string_list)

print(int_list)
