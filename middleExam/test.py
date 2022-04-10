import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sb

# read csv
data = pd.read_csv('../State/Nobel/complete.csv')
prizeAmountAdjusted = np.array(data["prizeAmountAdjusted"])
# Std = np.std(prizeAmountAdjusted)

N = len(prizeAmountAdjusted)
n = 500
M = 1000
x = 90
def myBootstrap(n, M, x):
    for _ in range(0, M):
        index = np.random.randint(0, n, N)
        sample = prizeAmountAdjusted[index]
        Std = np.std(sample)
        resample.append(Std)
        
    Cut = (np.max(resample) - np.min(resample)) * ((100 - x) / 2 / 100)
    Head = np.min(resample) + Cut
    Tail = np.max(resample) - Cut
    return (resample, Head, Tail)
    
resample, Head, Tail = myBootstrap(n, M, x)
plt.hist(resample, bins=50)
print(Head)
print(Tail)
# print(np.max(resample))
# print(np.min(resample))
# print((np.max(resample) - np.min(resample)) * ((100 - x) / 2 / 100))
