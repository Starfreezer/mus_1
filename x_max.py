import numpy as np
import matplotlib.pyplot as plt
import utils

maxima = np.arange(1, 7)
maxima_probs = []

for i in range(1, 7):
    prob = (i ** 2 - ((i - 1) ** 2)) / 36
    maxima_probs.append(prob)

print(maxima_probs)
print(sum(maxima_probs))
