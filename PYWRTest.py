import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("seaborn")

#fig, (Maule, LI) = plt.subplots(2)
#fig.suptitle('Adjustment in reservoirs between the PYWR model, WEAP and Historical Data')

fig, axes = plt.subplots(6)
# fig.suptitle('PYWR Results for Three Scenarios at Different Adaption Levels', fontsize=19)

Deficit = pd.read_excel('Escenarios/PruebaTresEscenarios.xls',sheet_name='Deficit', usecols='A:F')
plot1 = Deficit.plot(x= 'Datetime', y= ['Average','High', 'Low'], figsize=(15, 5), ax=axes[0], ylabel='Deficit \n [Hm$^3$]', grid=True)
# plot11 = Deficit.plot(x= 'Datetime', y=['Average w/s'], ax=axes[0], alpha=0.3, color='blue')
# plot12 = Deficit.plot(x= 'Datetime', y=['Low w/s'], ax=axes[0], alpha=0.3, color='red')
plot1.legend_.remove()
plot1.set_title(label='(a)',loc='left')


Outflow = pd.read_excel('Escenarios/PruebaTresEscenarios.xls',sheet_name='Outflow', usecols='A:F')
plot2 = Outflow.plot(x= 'Datetime', y= ['Average','High', 'Low'], figsize=(15, 5), ax=axes[1], ylabel='Flow \n [m$^3$/s]' , grid=True)
# plot21 = Outflow.plot(x= 'Datetime', y=['Average w/s'], ax=axes[1], alpha=0.3, color='blue')
# plot22 = Outflow.plot(x= 'Datetime', y=['Low w/s'], ax=axes[1], alpha=0.3, color='red')
plot2.legend_.remove()
plot2.set_title(label='(b)',loc='left')
# plt.ylabel(r'Accumulated Deficit [Hm$^3$]')

Hydropower = pd.read_excel('Escenarios/PruebaTresEscenarios.xls',sheet_name='Hydropower', usecols='A:F')
plot3 = Hydropower.plot(x= 'Datetime', y= ['Average','High', 'Low'], figsize=(15, 5), ax=axes[2], ylabel='Generation \n [GWh]', grid=True)
# plot31 = Hydropower.plot(x= 'Datetime', y=['Average w/s'], ax=axes[2], alpha=0.3, color='blue')
# plot32 = Hydropower.plot(x= 'Datetime', y=['Low w/s'], ax=axes[2], alpha=0.3, color='red')
plot3.legend_.remove()
plot3.set_title(label='(c)',loc='left')

Benefits_Crops = pd.read_excel('Escenarios/PruebaTresEscenarios.xls',sheet_name='Benefit_Crop', usecols='A:O')
plot5 = Benefits_Crops.plot(x= 'Datetime', y= ['Average','High', 'Low'], figsize=(15, 5), ax=axes[3], ylabel='Benefits \n [MM USD]', grid=True)
# plot31 = Benefits.plot(x= 'Datetime', y=['Average w/s'], ax=axes[3], alpha=0.3, color='blue')
# plot32 = Benefits.plot(x= 'Datetime', y=['Low w/s'], ax=axes[3], alpha=0.3, color='red')
plot5.legend_.remove()
plot5.set_title(label='(d)',loc='left')

Benefits_Hydropower = pd.read_excel('Escenarios/PruebaTresEscenarios.xls',sheet_name='Benefit_Hydropower', usecols='A:O')
plot6 = Benefits_Hydropower.plot(x= 'Datetime', y= ['Average','High', 'Low'], figsize=(15, 5), ax=axes[4], grid=True)
# plot31 = Benefits.plot(x= 'Datetime', y=['Average w/s'], ax=axes[3], alpha=0.3, color='blue')
# plot32 = Benefits.plot(x= 'Datetime', y=['Low w/s'], ax=axes[3], alpha=0.3, color='red')
plot6.legend_.remove()
plot6.set_title(label='(e)',loc='left')

Crop = pd.read_excel('Escenarios/PruebaTresEscenarios.xls',sheet_name='ReplacedFraction', usecols='A:F')
plot7 = Crop.plot(x= 'Datetime', y= ['Average','High', 'Low'], figsize=(15, 5), ax=axes[5], ylabel='Fraction', grid=True)
# plot31 = Crop.plot(x= 'Datetime', y=['Average w/s'], ax=axes[4], alpha=0.3, color='blue')
# plot32 = Crop.plot(x= 'Datetime', y=['Low w/s'], ax=axes[4], alpha=0.3, color='red')
plot7.set_title(label='(f)',loc='left')

# plt.ylabel(r'Storage Level $[m^3]$', fontsize=25, position=[3, 3, 3])
plt.xlabel('Year', fontsize=18, loc='center')
plt.tick_params(axis='x', labelsize=13)
# plt.tick_params(axis='y', labelsize=13)

for ax in axes:
    ax.label_outer()

plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=15)
axes[3].yaxis.set_label_coords(-0.055, -0.1)

plt.show()