import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
plt.style.use("seaborn")

fig, axes = plt.subplots(nrows=2, ncols=1)
# fig.suptitle('Scenarios Performance Improvement by Adaption Strategies', fontsize=18)


Before = pd.read_excel('Escenarios/Scenario_Performance_Evolution.xls',sheet_name='Scenario_Performance', usecols='A:Z')
u  = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
v  = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
u1 = Before['Resilience2']-Before['Resilience']
v1 = Before['Reliability2']-Before['Reliability']
u2 = Before['Benefit2']-Before['Benefit']
v2 = Before['Hydropower2']-Before['Hydropower']


plot1 = axes[0].scatter(Before['Reliability'], Before['Resilience'], c=Before['Vulnerability'], vmin=12, vmax=70, s=100, cmap='RdYlGn_r', edgecolors='black', alpha=0.5)
plot2 = axes[0].scatter(Before['Reliability2'], Before['Resilience2'], c=Before['Vulnerability2'], vmin=12, vmax=70, s=100, cmap='RdYlGn_r', edgecolors='black')
quiver1 = axes[0].quiver(Before['Reliability'],Before['Resilience'], v1, u1, alpha=0.3, angles='xy', scale_units='xy', scale=1, width=0.006)

plot3 = axes[1].scatter(Before['Hydropower'], Before['Benefit'], c=Before['Outflow'], vmin=12, vmax=60, s=100, cmap='RdYlGn', edgecolors='black', alpha=0.5)
plot4 = axes[1].scatter(Before['Hydropower2'], Before['Benefit2'], c=Before['Outflow2'], vmin=12, vmax=60, s=100, cmap='RdYlGn', edgecolors='black')
quiver1 = axes[1].quiver(Before['Hydropower'],Before['Benefit'], v2, u2, alpha=0.3, angles='xy', scale_units='xy', scale=1, width=0.006)


# plt.grid()
# plt.xlabel('Reliability', fontsize=18)
# plt.ylabel('Resilience', fontsize=18)
# plt.tick_params(axis='x', labelsize=15)
# plt.tick_params(axis='y', labelsize=15)
fig.colorbar(plot2, ax=axes[0])
fig.colorbar(plot4, ax=axes[1])
axes[0].set_title(label='(a)', loc='left', size=16)
axes[1].set_title(label='(b)', loc='left', size=16)
axes[0].set_ylabel(r'Ag. Resilience', size=16)
axes[0].set_ylim(bottom=0, top=1.05)
axes[1].set_ylabel(r'Agricultural Benefits [MM USD]', size=16)
axes[0].set_xlabel(r'Ag. Reliability', size=16)
axes[0].set_xlim(left=0.8, right=1.01)
axes[1].set_xlabel(r'Hydropower Benefits [MM USD]', size=16)
axes[0].tick_params(axis='both', which='major', labelsize=14)
axes[1].tick_params(axis='both', which='major', labelsize=14)


plt.figtext(0.85, 0.14, r'System Outflow $[m^3/s]$', fontsize=16, rotation=-90)
plt.figtext(0.85, 0.6, r'Ag. Vulnerability $[m^3/s]$', fontsize=16, rotation=-90)
plt.show()
