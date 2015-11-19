# write a function that takes two lists and returns a dictionary where the first
# list is the keys and the second list is the values.

def take_two(key_list, value_list):
    new_dict = dict()
    if len(key_list) - len(value_list) != 0:
        for k in range(len(key_list)-len(value_list)):
            value_list.append("")
    for v in range(len(key_list)):
        new_dict[key_list[v]] = value_list[v]
        print (new_dict)

take_two(["frog", "cat", "owl", "snake"], ["hop", "meow", "hoot",])



# if the first list is longer than the second list then the keys should still be
# created with the value set to the empty string

# if the first list is shorter then any elements in the second list with no keys
# should be discarded
