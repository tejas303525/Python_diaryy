# mat= [[0,1]]




# def markrow(i):
#     for j in range(len(mat[i])):
#         if mat[i][j]!=0:
#             mat[i][j]=-1

# def markcol(j):
#     for i in range(len(mat)):
#         if mat[i][j]!=0:
#             mat[i][j]=-1


# for i in range(len(mat)):
#     for j in range(len(mat[i])):
#         if mat[i][j]==0:
#             print("Position of 0:", i, j)
#             markrow(i)
#             markcol(j)


# for i in range(len(mat)):
#     for j in range(len(mat[i])):
#             if mat[i][j]==-1:
#                 mat[i][j]=0
# print(mat)


# bruteforce approach

# class Solution:
#     def markrow(self,matrix,i):
#         for j in range(len(matrix[i])):
#             if matrix[i][j]!=0:
#                 matrix[i][j]= float('-inf')
#     def markcol(self,matrix,j):
#         for i in range(len(matrix)):
#             if matrix[i][j]!=0:
#                 matrix[i][j]= float('-inf')


#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         for i in range(len(matrix)):
#             for j in range(len(matrix[i])):
#                 if(matrix[i][j]==0):
#                     self.markrow(matrix,i)
#                     self.markcol(matrix,j)
                    
#         for i in range(len(matrix)):
#             for j in range(len(matrix[i])):
#                 if matrix[i][j]== float('-inf'):
#                     matrix[i][j]=0



# better approach

mat=[[1, 1, 1], [1, 0, 1], [1, 1, 1]]

row=[0]*len(mat)
col=[0]*len(mat[0])


for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j]==0:
            row[i]=1
            col[j]=1
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if(row[i]==1 or col[j]==1):
            mat[i][j]=0
print(mat)
