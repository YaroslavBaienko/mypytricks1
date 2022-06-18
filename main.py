import numpy as np


dataset = np.arange(234, 234234, 34)
print(dataset)

for i in dataset:
    assert isinstance(i, object)
    print(i)

i = 12
print(i)

a = 234
a = a * 2
print(a)