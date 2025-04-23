import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import geom, expon


p = 0.3
lam = 2

x_geom = np.arange(1, 15)
x_expon = np.linspace(0, 5, 500)


cdf_geom = geom.cdf(x_geom, p)
cdf_expon = expon.cdf(x_expon, scale=1/lam)

pmf_geom = geom.pmf(x_geom, p)
pdf_expon = expon.pdf(x_expon, scale=1/lam)

plt.figure(figsize=(12, 5))
plt.step(x_geom, cdf_geom, where='post', label='Geometrisch (diskret)')
plt.plot(x_expon, cdf_expon, label='Exponentiell (kontinuierlich)')
plt.title('Verteilungsfunktionen (CDF)')
plt.xlabel('x')
plt.ylabel('F(x)')

plt.tight_layout()
plt.show()


plt.stem(x_geom, pmf_geom, basefmt=" ", linefmt="C0-", markerfmt="C0o", label='Geometrisch (PMF)')
plt.plot(x_expon, pdf_expon, 'C1-', label='Exponentiell (PDF)')
plt.title('Verteilung / Dichtefunktion')
plt.xlabel('x')
plt.ylabel('f(x)')

plt.tight_layout()
plt.show()



