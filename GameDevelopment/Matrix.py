#1D list
numbers = [1,2,3,4,5]
for number in numbers:
    print(number)
#2D list / matrix
even_odd_prime = [[2,4,6,8,10],[1,3,5,7,9],[2,3,5,7,11]]
print(even_odd_prime)

for i in range(0,len(even_odd_prime)):
    for j in range(0,len(even_odd_prime[0])):
        print(even_odd_prime[i][j],end=" ")

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
matrix = []
for i in range(rows):
    temp = []
    for j in range(columns):
        x = int(input("Enter the element for the matrix: "))
        temp.append(x)
    matrix.append(temp)
print(matrix)

matrixA = [[1,2,3],[4,5,6]]
matrixB = [[2,3,4],[5,6,7]]
addition_result = [[0,0,0],[0,0,0]]
for i in range(0,2):
    for j in range(0,3):
        addition_result[i][j] = matrixA[i][j] + matrixB[i][j]
print(addition_result)
