
class run:
    def execute(self):
        print('compiling')
        print('running')




class check(run):
    def execute(self):
        super(check, self).execute()
        print('spell check')
        print('convention check')




class LapTop:
    def code(self,my):
        my.execute()

my = check()
lap1 = LapTop()
lap1.code(my)
