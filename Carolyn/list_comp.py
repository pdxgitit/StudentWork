color_list = ['red', 'blue', 'green', 'orange']

# def color_combos(color_list):
#     for item in color_list:
#         if item[0] == 'a' or 'e':
#             print('Orange is warm')
#         elif item[1] == 'a' or 'e':
#             print('Red is warm')
#         else:
#             return item +' is cool'
# print(color_combos(color_list


new_colors = [  "bright " + color     for color in color_list     ]
print(new_colors)
