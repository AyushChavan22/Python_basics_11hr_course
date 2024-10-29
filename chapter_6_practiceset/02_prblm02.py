marks1 = int(input("Enter your marks in DSP subject:- "))
marks2 = int(input("Enter your marks in MIE subject:- "))
marks3 = int(input("Enter your marks in MEMS subject:- "))

# for percentage
total_percentage = (100*(marks1+marks2+marks3))/300

#for checking if passed or not
if(total_percentage>40 and marks1>33 and marks2>33 and marks3>33):
    print("Congratulations!!! You have passed. Your percentage is:",total_percentage)
else:
    print("Oops!!! You have failed try again. Your percentage is:", total_percentage)