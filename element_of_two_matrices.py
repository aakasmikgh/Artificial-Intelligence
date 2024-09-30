matrix1=[]
n=int(input("Enter Number of Rows:"))
m=int(input("Enter Number of Columns:"))
print("Enter Elements of First Matrix")
for i in range(0,n):
  row=[]
  for j in range(0,m):
      e=int(input())
      row.append(e)
  matrix1.append(row)
 
matrix2=[]
print("Enter Elements of Second Matrix")
for i in range(0,n):
  row=[]
  for j in range(0,m):
      e=int(input())
      row.append(e)
  matrix2.append(row)
 
print("matrix1:",matrix1)
print("matrix2:",matrix2)
print("First Row of Matrix1",matrix1[0])
print("3rd Element of Second Row of Matrix1:",matrix1[1][2])
print("Matrix1*2",matrix1*2)
sum=[]
for i in range(0,n):
  row=[]
  for j in range(0,m):
   e=matrix1[i][j]+matrix2[i][j]
   row.append(e)
  sum.append(row)
print("Sum:",sum)