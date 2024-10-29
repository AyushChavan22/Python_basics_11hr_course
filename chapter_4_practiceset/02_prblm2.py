marks = []

m1 = int(input("Enter the marks of first  student:-"))
marks.append(m1) #.append attaches single element to a mentioned list
m2 = int(input("Enter the marks of second  student:-"))
marks.append(m2)
m3 = int(input("Enter the marks of third  student:-"))
marks.append(m3)
m4 = int(input("Enter the marks of fourth  student:-"))
marks.append(m4)
m5 = int(input("Enter the marks of fifth  student:-"))
marks.append(m5)
m6 = int(input("Enter the marks of sixth  student:-"))
marks.append(m6)


marks.sort()
print(marks)