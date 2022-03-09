import numpy as np

array = np.zeros(10)
print(array)

array = np.ones(10)
print(array)

array = np.ones(10) * 5
print(array)

array = np.arange(51)
print(array)

array = np.arange(10, 51)
print(array)

array = np.arange(9).reshape((3, 3))
print(array)

array = np.identity(3)
print(array)

rand_num = np.random.normal(0,1,1)
print(rand_num)

array = np.random.randn(5, 5)
print(array)

array = np.arange(1, 101).reshape((10, 10)) * 0.01
print(array)

array = np.linspace(0, 1, 20)
print(array)

mat = np.arange(1,26).reshape(5,5)
mat
print(mat[2:, 1:])
print(mat[3][4])
print(mat[:3, 1].reshape(3, 1))
print(mat[4:])
print(mat[3:])
sum(sum(mat))
np.std(mat)

sum(mat)
# cột
# mat.sum(axis=0)
# hàng
# mat.sum(axis=1)

#np.max(mat[0, :])
indexCol = np.argmax(mat[0])
row = mat[:, indexCol]
indexRow = np.argmax(row)

mat = np.array([[1, 2, 3], [3, 2, 1]])
loc = np.where(mat == np.max(mat))
#print(mat)
#for i in range(0, len(loc)):
    #print(f"Phan tu thu {i + 1} nam o hang {loc[i][1]} va o cot {loc[i][0]}")

rows = loc[0]
cols = loc[1]
z = zip(rows, cols)
cnt = 0
for r, c in z:
    cnt += 1
    print('Phan tu thu', cnt, 'o hang', r, 'va cot', c)

rows = list(loc[0])
cols = list(loc[1])
z = list(zip(rows, cols))
for i, x in enumerate(z):
    print(i + 1, x[0], x[1])

#print(list(zip(loc[0], loc[1])))

# tính độ lệch chuẩn 
# m = mat.mean()
# n = np.mean((mat - m) ** 2)
# print(np.sqrt(n))
