import random
import numpy
from matplotlib import pyplot
import pandas as pd

Total = pd.read_excel('Results/Histograma.xls',sheet_name='Histogram', usecols='A:R')
bins = numpy.linspace(2020, 2060, 41)
bins2 = numpy.linspace(0, 1, 40)
bins3 = numpy.linspace(170000000, 630000000, 40)
bins4 = numpy.linspace(0.6, 0.8, 40)

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

fig, axs = pyplot.subplots(6, tight_layout=True)
# fig.suptitle('Variable Frequency Histogram', fontsize=25)
# We can set the number of bins with the `bins` kwarg
axs[0].hist(y1, bins, alpha=0.5, label='Average Flow')
axs[0].hist(x1, bins, alpha=0.5, label='Lowest Flow')
axs[0].hist(z1, bins, alpha=0.5, label='Highest Flow')
axs.flat[0].set_title('Legume Replacement Starting Year')
# axs.flat[0].set_title('(a)', loc='left')
axs[1].hist(y2, bins, alpha=0.5, label='Average Flow')
axs[1].hist(x2, bins, alpha=0.5, label='Lowest Flow')
axs[1].hist(z2, bins, alpha=0.5, label='Highest Flow')
axs.flat[1].set_title('Cereal Replacement Starting Year')
# axs.flat[1].set_title('(b)', loc='left')
axs[2].hist(y3, bins4, alpha=0.5, label='Average Flow')
axs[2].hist(x3, bins4, alpha=0.5, label='Lowest Flow')
axs[2].hist(z3, bins4, alpha=0.5, label='Highest Flow')
# axs[1].set_ylim(0, 200)
axs.flat[2].set_title(r'$\alpha$ Parameter (Hedging Coefficient)')
# axs.flat[2].set_title('(c)', loc='left')
axs[3].hist(y4, bins3, alpha=0.5, label='Average Flow')
axs[3].hist(x4, bins3, alpha=0.5, label='Lowest Flow')
axs[3].hist(z4, bins3, alpha=0.5, label='Highest Flow')
# axs[3].set_ylim(0, 50)
axs.flat[3].set_title(r'$\beta$ Parameter (Hedging Zone)')
# axs.flat[3].set_title('(d)', loc='left')
axs[4].hist(y5, bins2, alpha=0.5, label='Average Flow')
axs[4].hist(x5, bins2, alpha=0.5, label='Lowest Flow')
axs[4].hist(z5, bins2, alpha=0.5, label='Highest Flow')
axs.flat[4].set_title(r'Legume Replacement Fraction')
# axs.flat[4].set_title('(e)', loc='left')
axs[5].hist(y6, bins2, alpha=0.5, label='Average Flow')
axs[5].hist(x6, bins2, alpha=0.5, label='Lowest Flow')
axs[5].hist(z6, bins2, alpha=0.5, label='Highest Flow')
axs.flat[5].set_title(r'Cereal Replacement Fraction')
# axs.flat[5].set_title('(f)', loc='left')
# pyplot.legend(loc='upper right', fontsize=11)
# pyplot.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=11)
pyplot.legend(loc='center left', bbox_to_anchor=(0.75, 10), fontsize=11)
pyplot.ylabel('Frequency', fontsize=15, position='[5, 3, 3]')



pyplot.show()