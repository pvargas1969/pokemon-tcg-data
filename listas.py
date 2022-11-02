import pandas as pd

l1 = []
l2 = []

l1 = ["A", "B", "C"]
l2 = ["C", "D", "E"]

l3 = []
l3.extend(l1)
print(l3)

l3.extend(l2)
print(l3)

l3 = list(pd.unique(l3))
print(l3)

