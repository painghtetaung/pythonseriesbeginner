a = 10
b = 2

try:
    print('resource open')
    print(a/b)
    k = int(input('Enter a number'))
    print(k)

except ZeroDivisionError as e:# not even e you can use another....
    print('You cannot divide a number by zero',e)

except ValueError as e:
    print('Invalid Input',':',e)

except Exception as e:
    print('something went wrong',':',e)

finally:
    print('resource closed')

print('bye')