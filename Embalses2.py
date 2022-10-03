import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#fig, (Maule, LI) = plt.subplots(2)
#fig.suptitle('Adjustment in reservoirs between the PYWR model, WEAP and Historical Data')

fig, axes = plt.subplots(5)
# fig.suptitle('Comparison Between Reservoir Levels', fontsize=25)

Maule = pd.read_excel('Calibration/Ajuste.xls',sheet_name='Maule', usecols='F:I')
plot1 = Maule.plot(x= 'Datetime', y= ['WEAP', 'PYWR'], title='Maule Lagoon', figsize=(15, 5), ax=axes[0], grid=True)
plot1.legend_.remove()
plot1.set_title(label=r'$R^2=0.72$',loc='right')

LI = pd.read_excel('Calibration/Ajuste.xls',sheet_name='LI', usecols='C:E')
plot2 = LI.plot(x= 'Datetime', y= ['WEAP', 'PYWR'], title='Invernada Lagoon', figsize=(15, 5), ax=axes[1], grid=True)
plot2.legend_.remove()
plot2.set_title(label=r'$R^2=0.67$',loc='right')

Melado = pd.read_excel('Calibration/Ajuste.xls',sheet_name='Melado', usecols='C:F')
plot3 = Melado.plot(x= 'Datetime', y= ['WEAP', 'PYWR'], title='Melado Reservoir', figsize=(15, 5), ax=axes[2], grid=True)
plot3.legend_.remove()
plot3.set_title(label=r'$R^2=0.75$',loc='right')

Machicura = pd.read_excel('Calibration/Ajuste.xls',sheet_name='Machicura', usecols='E:G')
plot5 = Machicura.plot(x= 'Datetime', y= ['WEAP', 'PYWR'], title='Machicura Reservoir', figsize=(15, 5), ax=axes[3], grid=True)
plot5.legend_.remove()
plot5.set_title(label=r'$R^2=1$',loc='right')

Colbun = pd.read_excel('Calibration/Ajuste.xls',sheet_name='Colbun', usecols='D:G')
plot4 = Colbun.plot(x= 'Datetime', y= ['WEAP', 'PYWR'], title='Colbun Reservoir', figsize=(15, 5), ax=axes[4], grid=True)
plot4.set_title(label=r'$R^2=0.7$',loc='right')


plt.ylabel(r'Storage Level $[m^3]$', fontsize=18, position=[3, 3, 3])
plt.xlabel('Year', fontsize=18, loc='center')
plt.tick_params(axis='x', labelsize=14)
# plt.tick_params(axis='y', labelsize=14)

for ax in axes:
    ax.label_outer()

plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=15)

plt.show()



