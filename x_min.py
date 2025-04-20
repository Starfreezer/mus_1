import numpy as np
import matplotlib.pyplot as plt
import utils

minima = np.arange(1, 7)
minima_probs = []

for i in range(0, 6):
    val = ((7 - (i + 1)) ** 2 - (6 - (i + 1)) ** 2) / 36
    minima_probs.append(val)

discrete = utils.discrete_distribution(minima_probs)
print(discrete)

plt, ax = plt.subplots(2, 1)

ax[0].bar(minima, minima_probs)
ax[0].set(xlim=(0, 7), xticks=np.arange(1, 7), ylim=(0, 0.5))
ax[0].set_xlabel("Minimum")
ax[0].set_ylabel("P(Min(x1,x2) = i")


ax[1].step(minima, discrete)
ax[1].set(xlim=(0, 7), xticks=np.arange(1, 7), ylim=(0.2, 1.1))
ax[1].set_xlabel("t")
ax[1].set_ylabel("P(Min(x1,x2) <= t)")

expected_value = utils.expected_value(minima, minima_probs)
variance = utils.variance(minima, minima_probs)

print("Expected value: ", expected_value)
print("Variance: ", variance)


plt.tight_layout()
plt.show()
