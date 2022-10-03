import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("seaborn")

fig, axes = plt.subplots(nrows=2, ncols=1)


Total = pd.read_excel('Escenarios/Scenario_Performance.xls',sheet_name='Scenario_Performance', usecols='A:Z')
size = Total['Vulnerability'].to_numpy()
s = [s**1.5 for s in size]
size2 = Total['Outflow'].to_numpy()
s2 = [s**1.5 for s in size2]
plot1 = axes[0].scatter(Total['Reliability'], Total['Resilience'], c=Total['CaudalArmerillo'], s=s, cmap='RdYlGn', edgecolors='black')
plot2 = axes[0].scatter(Total['ReliabilityFake'], Total['ResilienceFake'], facecolors='none', s=Total['Minimo'], cmap='RdYlGn', edgecolors='black', label=25, linewidths=2)
plot3 = axes[0].scatter(Total['ReliabilityFake'], Total['ResilienceFake'], facecolors='none', s=Total['Maximo'], cmap='RdYlGn', edgecolors='black', label=66, linewidths=2)

plot3 = axes[1].scatter(Total['Hydrobenefit'], Total['AgriBenefit'], c=Total['CaudalArmerillo'], s=s2, cmap='RdYlGn', edgecolors='black')
plot4 = axes[1].scatter(Total['HydrobenefitFake'], Total['AgriBenefitFake'], facecolors='none', s=Total['Minimo2'], cmap='RdYlGn', edgecolors='black', label=13, linewidths=2)
plot5 = axes[1].scatter(Total['HydrobenefitFake'], Total['AgriBenefitFake'], facecolors='none', s=Total['Maximo2'], cmap='RdYlGn', edgecolors='black', label=33, linewidths=2)

fig.colorbar(plot1, ax=axes[0:2])
axes[0].set_title(label='(a)', loc='right', size=16)
axes[1].set_title(label='(b)', loc='right', size=16)
axes[0].set_ylabel(r'Ag. Resilience', size=16)
axes[1].set_ylabel(r'Total Agricultural Benefits [MM USD]', size=16)
axes[0].set_xlabel(r'Ag. Reliability', size=16)
axes[0].set_xlim(left=0.82, right=1)
axes[1].set_xlim(left=6500, right=9600)
axes[1].set_ylim(bottom=1900, top=2700)
axes[1].set_xlabel(r'Total Hydropower Benefits [MM USD]', size=16)
axes[0].tick_params(axis='both', which='major', labelsize=14)
axes[1].tick_params(axis='both', which='major', labelsize=14)

plt.figtext(0.85, 0.25, r'Average Annual Flow at Armerillo Station $[m^3/s]$', fontsize=16, rotation=-90)
axes[0].legend(loc= 'upper left', frameon=True, framealpha=0.5, facecolor='white', edgecolor='black', title=r'Ag. Vulnerability $[m^3/s]$', fontsize= 14, title_fontsize=16, labelspacing=1.5)
axes[1].legend(loc= 'upper left', frameon=True, framealpha=0.5, facecolor='white', edgecolor='black', title=r'Monthly Outflow $[m^3/s]$', fontsize= 14, title_fontsize=16, labelspacing=1.5)


# plt.title('System Performance Under Climate Change Scenarios', fontsize=20)
# plt.grid()
# plt.legend(loc= 'upper left', bbox_to_anchor=(0.6, 0.5), title=r'Ag. Vulnerability $[m^3/s]$', fontsize= 16, title_fontsize=18, labelspacing=1.5)
# plt.xlabel('Ag. Reliability', fontsize=18)
# plt.ylabel('Ag. Resilience', fontsize=18)
# plt.tick_params(axis='x', labelsize=15)
# plt.tick_params(axis='y', labelsize=15)
# plt.colorbar()
# plt.figtext(0.86, 0.3, r'Average Annual Flow at Armerillo Station $[m^3/s]$', fontsize=18, rotation=-90)
plt.show()
