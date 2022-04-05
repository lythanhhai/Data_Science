import pandas as pd
import math
data = pd.read_csv("../State/state.csv")

# mad
N = len(data["Murder.Rate"])
averValue = sum(data["Murder.Rate"]) / N
Sum = 0

for index in range(0, N):
    Sum += math.abs(data["Murder.Rate"][index] - averValue)

print(str(1 / N * Sum))

# iqr

# std
Sum1 = 0
for index in range(0, N):
    Sum1 += math.pow(math.abs(data["Murder.Rate"][index] - averValue), 2)

print(str(math.sqrt(Sum1 / N)))