s = {1,2,3}
s2={2,4,5}
print("Set :", s)

'''s.add(5)
print(s)
s.remove(3)
print(s)'''


#removed = s.pop()
#print("Removed one : ",removed)

unions = s.union(s2)
print("After union :",unions)

inter = s.intersection(s2)
print("After Intersection:",inter)

diff = s.difference(s2)
print("Differences : ",diff)