import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# plt.style.use("seaborn")

fig, axes = plt.subplots(nrows=3, ncols=1)
# fig.suptitle('Hedging Variables over Agricultural System Performance', fontsize=21)

Low = pd.read_excel('Escenarios/Variables_Performance.xls',sheet_name='Low', usecols='A:M')
Medium = pd.read_excel('Escenarios/Variables_Performance.xls',sheet_name='Medium', usecols='A:M')
High = pd.read_excel('Escenarios/Variables_Performance.xls',sheet_name='High', usecols='A:M')
size = Low['Resilience'].to_numpy()
s = [(s*10)**2.5 for s in size]
primero = axes[0].scatter(Low['Alpha'], Low['Beta'], c=Low['Vulnerability'], vmin=30, vmax=80, s=s, cmap='RdYlGn_r', edgecolors='black')
segundo = axes[0].scatter(Low['Alpha'], Low['Beta'], c=Low['Vulnerability'], vmin=30, vmax=80, s=Low['Minimo'], cmap='RdYlGn_r', edgecolors='black', label=0.44)
tercero = axes[0].scatter(Low['Alpha'], Low['Beta'], c=Low['Vulnerability'], vmin=30, vmax=80, s=Low['Maximo'], cmap='RdYlGn_r', edgecolors='black', label=0.52)
# axes[0].legend(loc= 'upper right', title=r'Ag. Resilience', fontsize= 12, title_fontsize=15, labelspacing=1.5)

size2 = Medium['Resilience'].to_numpy()
sdos = [(sdos*10)**2.5 for sdos in size2]
cuarto = axes[1].scatter(Medium['Alpha'], Medium['Beta'], c=Medium['Vulnerability'], vmin=30, vmax=80, s=sdos, cmap='RdYlGn_r', edgecolors='black')
quinto = axes[1].scatter(Medium['Alpha'], Medium['Beta'], c=Medium['Vulnerability'], vmin=30, vmax=80, s=Medium['Minimo'], cmap='RdYlGn_r', edgecolors='black', label=0.67)
sexto = axes[1].scatter(Medium['Alpha'], Medium['Beta'], c=Medium['Vulnerability'], vmin=30, vmax=80, s=Medium['Maximo'], cmap='RdYlGn_r', edgecolors='black', label=0.91)
# axes[1].legend(loc= 'upper right', title=r'Ag. Resilience', fontsize= 12, title_fontsize=15, labelspacing=1.5)

size3 = High['Resilience'].to_numpy()
stres = [(stres*10)**2.5 for stres in size3]
quinto = axes[2].scatter(High['Alpha'], High['Beta'], c=High['Vulnerability'], vmin=0, vmax=80, s=stres, cmap='RdYlGn_r', edgecolors='black')
quinto = axes[2].scatter(High['AlphaFake'], High['BetaFake'], facecolors='none', s=High['Minimo'], cmap='RdYlGn_r', edgecolors='black', label=0.44, linewidths=2)
quinto = axes[2].scatter(High['AlphaFake'], High['BetaFake'], facecolors='none', s=High['Maximo'], cmap='RdYlGn_r', edgecolors='black', label=0.91, linewidths=2)
axes[2].legend(bbox_to_anchor=(1.38, 0.7), title=r'Ag. Resilience', fontsize= 16, title_fontsize=17, labelspacing=1.5)

axes[0].set_title(label='(a)', loc='left', size=16)
axes[1].set_title(label='(b)', loc='left', size=16)
axes[2].set_title(label='(c)', loc='left', size=16)
# axes[0].set_ylabel(r'Lowest Flow', size=20, labelpad=50)
# axes[1].set_ylabel(r'Average Flow', size=20, labelpad=50)
# axes[2].set_ylabel(r'Highest Flow', size=20, labelpad=50)
axes[0].set_xlim(left=0.58, right=0.76)
axes[0].xaxis.set_tick_params(labelsize=14)
axes[0].yaxis.set_tick_params(labelsize=14)
axes[1].set_xlim(left=0.58, right=0.76)
axes[1].xaxis.set_tick_params(labelsize=14)
axes[1].yaxis.set_tick_params(labelsize=14)
axes[2].set_xlim(left=0.58, right=0.76)
axes[2].xaxis.set_tick_params(labelsize=14)
axes[2].yaxis.set_tick_params(labelsize=14)
axes[0].set_ylim(bottom=100, top=700)
axes[1].set_ylim(bottom=100, top=700)
axes[2].set_ylim(bottom=100, top=700)

cbar = fig.colorbar(primero, ax=axes[:])
cbar.ax.tick_params(labelsize=15)

plt.xlabel(r'Hedging Coefficient $\alpha$', fontsize=20)
plt.figtext(0.05, 0.3, r'Storage Hedging Zone $\beta$ $[Hm^3]$', fontsize=20, rotation=90)
plt.figtext(0.87, 0.4, r'Ag. Vulnerability $[m^3/s]$', fontsize=20, rotation=-90)
plt.show()