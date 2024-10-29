from random import randint

class Train:
    def __init__(ayush,trainNo):
        ayush.trainNo = trainNo
    def book(ayush,fro,to):
        print(f"Train is booked of Train number {ayush.trainNo} from {fro} to {to}.")
    def getStatus(ayush):
        print(f"The train of train number {ayush.trainNo} is running late by 10-15 minutes. Sorry for inconvenience.")
    def getFare(ayush,fro,to):
        print(f"The train fare of train number {ayush.trainNo} departing from {fro} to {to} is {randint(222,5555)}")

t = Train(45678)
t.book("Mumbai","Delhi")
t.getStatus()
t.getFare("Mumbai","Delhi")
#nothing happens if you remane self with any string just readability of code is disturbed
        