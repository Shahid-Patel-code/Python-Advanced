import datetime as dt
class person:
    def info(self):
        self.name=input("Enter name: ")
        self.birth=input("Enter Birth Date: ")
        self.date=dt.datetime.now()
        self.n=dt.datetime.strptime(self.birth,"%d-%m-%Y")
        self.age=(self.date.year-self.n.year)

        
class voter(person):
    def claculate(self):
        if self.age >=18:
            print(f"{self.name}'s Age is: {self.age}")
            print(f"{self.name} is elligible for Voting ")
        else :
            print(f"{self.name}'s Age is: {self.age}")
            print(f"{self.name} Not eligible for voting")


c1=voter()
c1.info()
c1.claculate()


