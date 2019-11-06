i=[i for i in range(1,10)]
print(i)

i=[i for i in range(1,10) if i%2==0 ]
print(i)

i=[(i,j) for i in range(1,10) for j in  range(1,10)]
print(i)

i=[(i,j,k) for i in range(1,10) for j in  range(1,10) for k in range(1,5)]
print(i)

i=[{i,j,k} for i in range(1,10) for j in  range(1,10) for k in range(1,5)]
print(i)