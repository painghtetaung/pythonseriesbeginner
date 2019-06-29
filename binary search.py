
def search(list, guess):
    lower = 0
    upper = len(list)-1
    while lower <= upper:
        mid = (lower + upper)//2
        if guess == list[mid] :
            globals()['p'] = mid
            return True
        elif guess > list[mid]:
            lower = mid+1
        else:
            upper = mid-1

    return False


list = [2,4,6,8,10,15,30,45,59,68]
guess = int(input("Guess The Number(binary)"))

if search(list, guess):
    print('Congratulation','Position is ->',p+1)
else:
    print('Not correct')