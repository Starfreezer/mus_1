import numpy as np
import matplotlib.pyplot as plt
import utils

x_range = np.arange(0, 11)
x_probs = np.zeros(len(x_range))  # now length 11

p = 5 / 6

for i in range(len(x_range)):
    x_probs[i] = (p ** i) * (1 - p)

print(x_probs)

plt, ax = plt.subplots(2, 1)
ax[0].bar(x_range, x_probs)
ax[0].set(xlim=(0, 10), xticks=np.arange(0, 11))
ax[0].set_xlabel("x")
ax[0].set_ylabel("P(X=x)")
ax[0].set_title("Verteilung von X")

discrete = utils.discrete_distribution(x_probs)
ax[1].bar(x_range, discrete)
ax[1].set(xlim=(0, 10), xticks=np.arange(0, 11))
ax[1].set_xlabel("x")
ax[1].set_ylabel("P(X<=x)")
ax[1].set_title("Verteilungsfunktion von X")

print("P(X <= 4) =  ", discrete[4])


plt.tight_layout()
plt.show()
