s = set()
s.add(20)
s.add(20.0)
s.add('20')
# length of s after these operations?
print(len(s))
#length 2 aaya cuzz python interprets 20.0 == 20
#example
a = 90 == 90.0
print(a)
# hence it shows true