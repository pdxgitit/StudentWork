import random
dice_left = 5
compile_result = []

def roll_dice(num_dice):
    results = []
    while num_dice > 0:
        num_dice -= 1
        results.append(random.randint(1,6))
    return results

def keep_dice(resul):
    D = len(resul)
    while D > 0:
        D -= 1
        user = input('Keep '+ str(resul[D]) +'? Y/N? ')
        if user.upper() == 'Y':
            global compile_result
            compile_result.append(resul[D])
            global dice_left
            dice_left -= 1
        elif user.upper() == 'N':
            continue
        else:
            print('No Comprendo!')
def check_results(checkers, chuckles):
    for die in chuckles:
        for num in checkers:
            if die != num
                return False
            
def scoring(arg):



last_results = roll_dice(dice_left)
print(last_results)
keep_dice(last_results)
last_results = roll_dice(dice_left)
print(last_results)
keep_dice(last_results)
last_results = roll_dice(dice_left)
print(last_results)
print("Final Result " + str(last_results + compile_result))
