from datetime import date , datetime
class Person :
    name = ''
    dob = ''
    def getInput(self):
        self.name = input('Name: ')
        dob = input('DOB(yy/mm/dd)')
        self.dob = datetime.strptime(dob,'%y/%m/%d')
    def isEligible(self):
        #print(self.dob)
        diff =  datetime.today() - self.dob 
        difinse=diff.total_seconds()
        years = divmod(difinse, 31556926)[0] 
        print(years)
        if(years>=18):
            return True
        else:
            return False

a = Person()
a.getInput()
print(a.isEligible())

        
