# nhập tuple
arrTuple = []
n = int(input())
# tạo mảng các tuple nhập vào
for i in range(0, n):
    t = input()
    a = tuple(str(x) for x in t.split())
    arrTuple.append(a)
for i in range(0, len(arrTuple) - 1):
    for j in range(i+1, len(arrTuple)):
        if arrTuple[i][0] <= arrTuple[j][0]:
            if arrTuple[i][1] <= arrTuple[j][1]:
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