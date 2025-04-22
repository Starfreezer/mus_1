import numpy as np
import matplotlib.pyplot as plt
import utils

maxima = np.arange(1, 7)
maxima_probs = []

for i in range(1, 7):
    prob = (i ** 2 - ((i - 1) ** 2)) / 36
    maxima_probs.append(prob)

print(maxima_probs)

discrete = utils.discrete_distribution(maxima_probs)
print(discrete)

plt, ax = plt.subplots(2, 1)

ax[0].bar(maxima, maxima_probs)
ax[0].set(xlim=(0, 7), xticks=np.arange(0, 7), ylim=(0, 0.5))
ax[0].set_xlabel("Maximum")
ax[0].set_ylabel("P(Max(x1,x2) = i)")
ax[0].set_title("Verteilung von " + '$X_{max}$')


ax[1].step(maxima, discrete)
ax[1].set(xlim=(0, 7), xticks=np.arange(0, 7), ylim=(0, 1.2))
ax[1].set_xlabel("t")
ax[1].set_ylabel("P(Max(x1,x2) <= t")
ax[1].set_title("Verteilungsfunktion von " + '$X_{max}$')



plt.tight_layout()
plt.show()
