pos = -1
def search(list, guess):
    i = 0
    while i < len(list):

        i = i+1
        if list[i] == guess:
            globals()['pos'] = i # to use i outside of this function and also to find the index number
            return True
    return False





list = [3,4,8,7,6,9]
guess = int(input("Guess The Number"))

if search(list, guess):
    print('Congratulation',pos+1)
else:
    print('Not Correct')