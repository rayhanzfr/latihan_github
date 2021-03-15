set1={1,3,5,7,9}
set2={2,3,5,7,11}

set3=set1.difference(set2)#{1,9}
print(set3)

set3=set1.symmetric_difference(set2)#{1,2,9,11}
print(set3)

set3=set1.intersection(set2)#{3,5,7}
print(set3)