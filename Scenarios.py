from matplotlib import rcParams, cycler
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
import pandas as pd


Total = pd.read_excel('Escenarios/Scenarios.xls', usecols='A:Q', index_col=0)
plot1 = plt.plot(Total[' "CCCMA ""CGCM3"" a"'], label='RCP8.5', alpha=0.5, linestyle='dashed', color='grey')
plot2 = plt.plot(Total[' "CCCMA ""CGCM3"" b"'], label='RCP6', alpha=0.5, color='grey')
plot3 = plt.plot(Total[' "GFDL ""CM2"" a"'], alpha=0.5, linestyle='dashed', color='grey')
plot4 = plt.plot(Total[' "GFDL ""CM2"" b"'], alpha=0.5, color='grey')
plot5 = plt.plot(Total[' "GISS ""AOM"" a"'], alpha=0.5, linestyle='dashed', color='grey')
plot6 = plt.plot(Total[' "GISS ""AOM"" b"'], alpha=0.5, color='grey')
plot7 = plt.plot(Total[' "MPI ""ECHAM5"" a"'], alpha=0.5, linestyle='dashed', color='grey')
plot8 = plt.plot(Total[' "MPI ""ECHAM5"" b"'], alpha=0.5, color='grey')
plot9 = plt.plot(Total[' "MRI ""CGCM2.3.2."" a"'], alpha=0.5, linestyle='dashed', color='grey')
plot10 = plt.plot(Total[' "MRI ""CGCM2.3.2."" b"'], alpha=0.5, color='grey')
plot11 = plt.plot(Total[' "NIES ""MIRO3.2."" a"'], alpha=0.5, linestyle='dashed', color='grey')
plot12 = plt.plot(Total[' "NIES ""MIRO3.2."" b"'], alpha=0.5, color='grey')
plot13 = plt.plot(Total[' "UKMO ""HADCM3"" a"'], alpha=0.5, linestyle='dashed', color='grey')
plot14 = plt.plot(Total[' "UKMO ""HADCM3"" b"'], alpha=0.5, color='grey')
plot15 = plt.plot(Total[' "historico mas futuro"'], label='Historical', color="black")



# N = 10
# data = (np.geomspace(1, 10, 100) + np.random.randn(N, 100)).T
# cmap = plt.cm.coolwarm
# rcParams['axes.prop_cycle'] = cycler(color=cmap(np.linspace(0, 1, N)))

# custom_lines = [Line2D([0], [0], color=cmap(0.), lw=4),
#                 Line2D([0], [0], color=cmap(.5), lw=4),
#                 Line2D([0], [0], color=cmap(1.), lw=4)]

# fig, ax = plt.subplots()
# lines = ax.plot(Total)
# ax.legend(custom_lines, ['Cold', 'Medium', 'Hot'])
plt.legend(loc= 'upper left', fontsize= 10)
ticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
plt.xticks(ticks, labels, fontsize=11)
# plt.title('Projected Average Flow in Armerillo Station', fontsize=15)
plt.xlabel('Month', fontsize=15)
plt.ylabel(r'Average Flow $[m^3/s]$', fontsize=15)
plt.ylim([0, 350])
plt.show()