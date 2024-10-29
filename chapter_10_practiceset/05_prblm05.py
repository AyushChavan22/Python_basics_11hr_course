from random import randint

class Train:
    def __init__(self,trainNo):
        self.trainNo = trainNo
    def book(self,fro,to):
        print(f"Train is booked of Train number {self.trainNo} from {fro} to {to}.")
    def getStatus(self):
        print(f"The train of train number {self.trainNo} is running late by 10-15 minutes. Sorry for inconvenience.")
    def getFare(self,fro,to):
        print(f"The train fare of train number {self.trainNo} departing from {fro} to {to} is {randint(222,5555)}")

t = Train(45678)
t.book("Mumbai","Delhi")
t.getStatus()
t.getFare("Mumbai","Delhi")
        