d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(d['k1'][3]['tricky'][3]['target'][3])

str = "ahhaha"
seq = ['soup','dog','salad','cat','great']
res = []
def filterFunc(seq):
    for i in seq:
        if i[0] == 's':
            res.append(i)

filterFunc(seq)
print(res)
#print(list(filter(filterFunc(seq), seq)))