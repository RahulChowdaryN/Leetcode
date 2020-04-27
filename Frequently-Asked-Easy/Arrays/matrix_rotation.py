a =[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]


#c = matrix
#a = [1,2,5,3,4]
##reverse of an array
#for i in range(len(a)//2):
#    a[i],a[len(a)-1-i] = a[len(a)-1-i],a[i]

# length = len(matrix)
# for i in range(length-1,-1,-1):
#     row = []
#     for j in range(length-1,-1,-1):
#         row.append(matrix[j][i])
#     matrix.append(row)
# for i in range(length):
#     matrix.pop(0)
#
# for i in range(length//2):
#     matrix[i],matrix[length-1-i] = matrix[length-1-i],matrix[i]
#
#
print(a)
for i in range(len(a)//2):
     a[i],a[len(a)-1-i] = a[len(a)-1-i],a[i]

print(a)
length = len(a)
for i in range(length-1,-1,-1):
     row = []
     for j in range(length-1,-1,-1):
         row.append(a[j][i])
     a.append(row)
print(a)