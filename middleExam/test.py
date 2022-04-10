import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# read csv
data = pd.read_csv('../State/Nobel/complete.csv')
prizeAmountAdjusted = np.array(data["prizeAmountAdjusted"])
# Std = np.std(prizeAmountAdjusted)

N = len(prizeAmountAdjusted)
n = 200
M = 1000
x = 90
resample = []
def myBootstrap(n, M, x):
    for _ in range(0, M):
        index = np.random.randint(0, N - 1, n)
        sample = prizeAmountAdjusted[index]
        Std = np.std(sample)
        resample.append(Std)

    Max = np.max(resample)
    Min =  np.min(resample)
    Cut_Segment = (Max - Min) * ((100 - x) / 2 / 100)
    Head = Min + Cut_Segment
    Tail = Max - Cut_Segment
    return (resample, Head, Tail)
    
resample, Head, Tail = myBootstrap(n, M, x)
print("Head point: ", Head)
print("Tail point: ", Tail)
counts, bins, bars = plt.hist(resample, bins = 50)
plt.rcParams.update({'font.size': 12})
plt.xlabel('prizeAmountAdjusted')
plt.ylabel('Count')
plt.title(f'standard deviation sampling distribution')
plt.axvline(Head, color = 'k', linestyle = 'solid', linewidth = 1)
plt.axvline(Tail, color = 'k', linestyle = 'solid', linewidth = 1)
plt.axvline(np.mean(resample), color = 'k', linestyle = 'dashed', linewidth = 1)
plt.ylim([0, np.max(counts) + 40])
min_ylim, max_ylim = plt.ylim()
plt.text(np.mean(resample) * 1.005, max_ylim * 0.4, 'Mean: {:.2f}'.format(np.mean(resample)))
plt.text(Head * 1.005, max_ylim * 0.75, '{:.2f}'.format(Head))
plt.text(Tail * 1.005, max_ylim * 0.75, '{:.2f}'.format(Tail))
x_values = [Head, Tail]
y_values = [np.max(counts) + 10, np.max(counts) + 10]
plt.plot(x_values, y_values, 'bo', linestyle="--")
plt.text((Head + Tail) / 2, max_ylim * 0.75, f'{x}%')
plt.show()
# print(len(resample))
# print(np.max(resample))
# print(np.min(resample))
# print((np.max(resample) - np.min(resample)) * ((100 - x) / 2 / 100))
