
def search(list, guess):
    for i in list:
        if i == guess:
            globals()['p'] = i # to use i outside of this function and also to find the index number
            return True
    return False






list = [5,4,8,7,3,2]
guess = int(input("Guess The Number(for loop method)"))

if search(list, guess):
    print('Congratulation','Position is ->',list.index(p)+1)
else:
    print('Not correct')