import numpy as np
import matplotlib.pyplot as plt
import utils

green_dice = np.arange(1, 7)
red_dice = np.arange(1, 7)

pairs = [(r, g) for r in red_dice for g in green_dice]

diffs = []

for (r, g) in pairs:
    diffs.append(r - g)

occurrences = {}

for d in diffs:
    if d in occurrences.keys():
        occurrences[d] = occurrences[d] + 1
    else:
        occurrences[d] = 1

print(occurrences)
possible_vals = np.sort(list(set(diffs)))

diff_probs = []

for val in possible_vals:
    diff_probs.append(occurrences[val] / 36)

expected = utils.expected_value(possible_vals, diff_probs)
variance = utils.variance(possible_vals, diff_probs)

discrete = utils.discrete_distribution(diff_probs)

print("Expected Value: ", expected)
print("Variance: ", variance)


plt, ax = plt.subplots(2, 1)
ax[0].bar(possible_vals, diff_probs)
ax[0].set(xlim=(-6, 6), xticks=np.arange(-5, 6), ylim=(0, 0.5))
ax[0].set_xlabel("Diff")
ax[0].set_ylabel("P(x1-x2 = i)")
ax[0].set_title("Verteilung von " + '$X_{diff2}$')


ax[1].step(possible_vals, discrete)
ax[1].set(xlim=(-5, 6), xticks=np.arange(-5, 6), ylim=(0.0, 1.1))
ax[1].set_xlabel("t")
ax[1].set_ylabel("P(x1-x2 <= t)")
ax[1].set_title("Verteilungsfunktion von " + '$X_{diff2}$')


plt.tight_layout()
plt.show()
