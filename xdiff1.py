import numpy as np
import matplotlib.pyplot as plt
import utils

green_dice = np.arange(1, 7)
red_dice = np.arange(1, 7)

pairs = [(g, r) for g in green_dice for r in red_dice]
print(pairs)

diffs = []

for (g, r) in pairs:
    mx = max(g, r)
    mn = min(g, r)
    diffs.append(mx - mn)

occurrences = {}

for d in diffs:
    if d in occurrences.keys():
        occurrences[d] = occurrences[d] + 1
    else:
        occurrences[d] = 1

diff_probs = [0, 0, 0, 0, 0, 0]
for k in occurrences.keys():
    diff_probs[k] = occurrences[k] / 36

discrete = utils.discrete_distribution(diff_probs)

plt, ax = plt.subplots(2, 1)

ax[0].bar(list(set(diffs)), diff_probs)
ax[0].set(xlim=(-1, 6), xticks=np.arange(0, 6), ylim=(0, 0.5))
ax[0].set_xlabel("i (Difference)")
ax[0].set_ylabel("P(X_diff = i)")

ax[1].step(list(set(diffs)), discrete)
ax[1].set(xlim=(0, 6), xticks=np.arange(0, 6), ylim=(0, 1.2), yticks=(np.linspace(0.0, 1.0, num=5)))
ax[0].set_xlabel("t")
ax[0].set_ylabel("P(X_diff <= t)")

plt.tight_layout()
plt.show()
