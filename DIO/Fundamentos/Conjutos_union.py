#union
con_a = set([1,2])
con_b = set([3,4])

print(con_a.union(con_b))

#intersect
con_a = set([1,2,3])
con_b = set([2,3,4,5])

print(con_a.intersection(con_b))

#difference
con_a = set([1,2,3])
con_b = set([3,4,5])

print(con_a.difference(con_b))
print(con_b.difference(con_a))

#symmetric difference
con_c = set([1,2,3])
con_d = set([3,4,5,6,7])

print(con_c.symmetric_difference(con_d))

#issubset
con_a = set([1,2,3])
con_b = set([4,2,5,3,1,7])

print(con_a.issubset(con_b))
print(con_b.issubset(con_a))

#len
con =  set([1,2,3,4,5,6,7,4,2,1])
print(len(con))

#in   - verificar se o número está lá
con = set([1,2,3,4,7,5,6,8,9])
print(7 in con)
print(11 in con)