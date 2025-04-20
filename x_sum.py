import numpy as np
import matplotlib.pyplot as plt
import utils

x_1 = np.repeat(1 / 6, 6)
x_2 = x_1.copy()

# Wertebereich [2,12]
x_labels = np.arange(2, 13)

x = np.convolve(x_1, x_2)

fig, ax = plt.subplots(2, 1)

ax[0].bar(x_labels, x)
ax[0].set(xlim=(1, 13), xticks=np.arange(1, 13))
ax[0].set_title("Verteilung von X")
ax[0].set_xlabel("Augensumme")
ax[0].set_ylabel("Wahrscheinlichkeit")

print(utils.discrete_distribution(x))

print("Erwartungswert X: ", utils.expected_value(x_labels, x))
print("Varianz X: ", utils.variance(x_labels, x))

ax[1].step(x_labels, utils.discrete_distribution(x))
ax[1].set_title("Verteilungsfunktion von X")
ax[1].set_xlabel("P(X <= t)")
ax[1].set_ylabel("Kumulative Wahrscheinlichkeit")

plt.tight_layout()
plt.show()
