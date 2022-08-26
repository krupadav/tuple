a = 11, 12, 15, 20
print(type(a))
b = (2, 9, 'a', 25)
print(type(b))
c = ()
print(type(c))
print(a.count(11))  # this will display how many times 11 appears in a
print(a.count(5))   # if element is not present anser will be 1
print(a.index(20))  # this will display at what index 12 is present.
print(a.index(5))   # value error
