from time import sleep
from threading import *
class Hello(Thread):
    def run(self):
        for i in range(1,6):
            print("hello",i)
            sleep(1)


class Hi(Thread):
    def run(self):
        for i in range(1,6):
            print("hi",i)
            sleep(1)





t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.3)
t2.start()

t1.join()
t2.join()

print("bye")