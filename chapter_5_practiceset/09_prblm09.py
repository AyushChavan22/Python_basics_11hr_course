# Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "Harry", [1,2]}
# No, you cannot include a list inside a set in Python because sets
# require their elements to be hashable and lists are not hashable 
# due to their mutable nature.
