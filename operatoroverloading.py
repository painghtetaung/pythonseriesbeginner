class Student:
    def __init__(self,c1,c2):
        self.m1 = c1
        self.m2 = c2

    def __add__(self, other):
        d1 = self.m1 + other.m1
        d2 = self.m2 + other.m2
        s3 = Student(d1,d2)
        return s3


    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)



s1 = Student(20,30)
s2 = Student(50,60)

s3 = s2 + s1

print(s3.m1)
if s1 > s2:
    print('s1 win')
else:
    print('s2 wins')

a = 7
print(a)
print(s1)