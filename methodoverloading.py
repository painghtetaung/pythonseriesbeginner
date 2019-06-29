class Student:

    def sum(self,a = None,b = None,c = None):
        s = 0
        if a != None and b != None and c != None:
            s = a+b+c
        elif a != None and b != None:
            s = a+b
        else:
            s = a
        return s



s1 = Student()


print(s1.sum(4,1))

#another example for methodoverloading

class A:
    def show(self):
        print('in A show')

class B:
    def show(self):
        print('in B show')

b = B()
b.show()
#result will show ->(in B show) -< like this