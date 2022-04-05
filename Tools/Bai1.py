from math import floor
import pandas as pd
data = pd.read_csv('../State/state.csv')

N = len(data['Murder.Rate'])

# mean
print(str(sum(data['Murder.Rate']) / N))

# trimmed mean
# p = 10%
p = 0.1
Sum = 0
Min = 0 + p * N
Max = N - p * N
for index in range(0, N):
    if index > Min and index <= Max:
        Sum += data['Murder.Rate'][index]

print(str(Sum / N))

# weight mean
Sum1 = 0
for index in range(0, N):
        Sum1 += data['Murder.Rate'][index] * data['Population'][index]
Sum2 = 0
for index in range(0, N):
        Sum2 += data['Population'][index]
print(Sum1 / Sum2)

# median
if N % 2 == 1:
    median = data['Murder.Rate'][floor(N / 2) + 1]
else:
    median = data['Murder.Rate'][floor(N / 2)] + data['Murder.Rate'][floor(N / 2) + 1]

print(str(median))