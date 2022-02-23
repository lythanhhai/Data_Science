# số lượng tuple
n = int(input())

# tạo mảng các tuple nhập vào
arrTuple = []

# nhập tuple
for i in range(0, n):
    t = input()
    a = tuple(str(x) for x in t.split(','))
    #a = map(int, input().split(','))
    arrTuple.append(a)

#C2:
#arrCopy = sorted(arrTuple)
#print(arrCopy)

#C1:
#print(arrTuple.sort(key= lambda row: (row[0], row[1], row[2])))
def swap(a, b):
    temp = a
    a = b
    b = temp

# dùng thuật toán bubble sort
for i in range(0, len(arrTuple) - 1):
    for j in range(i+1, len(arrTuple)):
        # so sánh name
        if arrTuple[i][0] <= arrTuple[j][0]:
            # so sánh age
            if arrTuple[i][1] <= arrTuple[j][1]:
                # so sánh height
                if arrTuple[i][2] <= arrTuple[j][2]:
                    break
                else:
                    temp = arrTuple[i]
                    arrTuple[i] = arrTuple[j]
                    arrTuple[j] = temp
                    break
            else:
                temp = arrTuple[i]
                arrTuple[i] = arrTuple[j]
                arrTuple[j] = temp
                break
        else:
            temp = arrTuple[i]
            arrTuple[i] = arrTuple[j]
            arrTuple[j] = temp
            break

print(arrTuple)