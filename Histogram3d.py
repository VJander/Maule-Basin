from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


Total = pd.read_excel('Results/Histograma.xls',sheet_name='Histogram', usecols='A:R')
bins = np.linspace(2020, 2060, 41)
bins2 = np.linspace(0, 1, 40)
bins3 = np.linspace(170000000, 630000000, 40)
bins4 = np.linspace(0.6, 0.8, 40)

x1 = Total['AnoLegumbreBajo']
y1 = Total['AnoLegumbreMedio']
z1 = Total['AnoLegumbreAlto']
x2 = Total['AnoCerealBajo']
y2 = Total['AnoCerealMedio']
z2 = Total['AnoCerealAlto']
x3 = Total['AlfaBajo']
y3 = Total['AlfaMedio']
z3 = Total['AlfaAlto']
x4 = Total['BetaBajo']
y4 = Total['BetaMedio']
z4 = Total['BetaAlto']
x5 = Total['FraccionLegumbreBajo']
y5 = Total['FraccionLegumbreMedio']
z5 = Total['FraccionLegumbreAlto']
x6 = Total['FraccionCerealBajo']
y6 = Total['FraccionCerealMedio']
z6 = Total['FraccionCerealAlto']

fig = plt.figure()

nbins = 41
ax = fig.add_subplot(611, projection='3d')
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
for c, z, l in zip(['lightblue', 'orange', 'green'], [10, 5, 0], [y1, x1, z1]):
    ys = np.random.normal(loc=10, scale=10, size=2000)

    hist, bins = np.histogram(l, bins=40)
    xs = (bins[:-1] + bins[1:])/10

    ax.bar(xs, hist, zs=z, zdir='y', alpha=0.8)

ax = fig.add_subplot(612, projection='3d')
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

for c, z, l in zip(['lightblue', 'orange', 'green'], [10, 5, 0], [y2, x2, z2]):
    ys = np.random.normal(loc=10, scale=10, size=2000)

    hist, bins = np.histogram(l, bins=nbins)
    xs = (bins[:-1] + bins[1:])/10

    ax.bar(xs, hist, zs=z, zdir='y', alpha=0.8)

ax = fig.add_subplot(613, projection='3d')
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

for c, z, l in zip(['lightblue', 'orange', 'green'], [10, 5, 0], [y3, x3, z3]):
    ys = np.random.normal(loc=10, scale=10, size=2000)

    hist, bins = np.histogram(l, bins=40)
    xs = (bins[:-1] + bins[1:])*20

    ax.bar(xs, hist, zs=z, zdir='y', alpha=0.8)

ax = fig.add_subplot(614, projection='3d')
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

for c, z, l in zip(['lightblue', 'orange', 'green'], [10, 5, 0], [y4, x4, z4]):
    ys = np.random.normal(loc=10, scale=10, size=2000)

    hist, bins = np.histogram(l, bins=40)
    xs = (bins[:-1] + bins[1:])/100000000

    ax.bar(xs, hist, zs=z, zdir='y', alpha=0.8)

ax = fig.add_subplot(615, projection='3d')
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

for c, z, l in zip(['lightblue', 'orange', 'green'], [10, 5, 0], [y5, x5, z5]):
    ys = np.random.normal(loc=10, scale=10, size=2000)

    hist, bins = np.histogram(l, bins=40)
    xs = (bins[:-1] + bins[1:])*10

    ax.bar(xs, hist, zs=z, zdir='y', alpha=0.8)

ax = fig.add_subplot(616, projection='3d')
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

for c, z, l in zip(['lightblue', 'orange', 'green'], [10, 5, 0], [y6, x6, z6]):
    ys = np.random.normal(loc=10, scale=10, size=2000)

    hist, bins = np.histogram(l, bins=40)
    xs = (bins[:-1] + bins[1:])*10

    ax.bar(xs, hist, zs=z, zdir='y', alpha=0.8)

# ax.set_xlabel('Year')
# ax.set_ylabel('Scenario')
# ax.set_zlabel('Frequency')

plt.show()
