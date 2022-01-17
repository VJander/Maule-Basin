import pywr
from pywr.model import Model
from pywr.notebook import draw_graph
from pywr.recorders import TablesRecorder
from pywr.core import Model
from pywr.recorders import Recorder
from pywr.recorders._recorders import NodeRecorder
from pywr.recorders.events import EventRecorder
from Maule_parameters import *
import tables
import pandas as pd
import numpy as np
import scipy as scipy
import json
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import warnings
warnings.filterwarnings('ignore', category=tables.NaturalNameWarning)
#matplotlib inline

# def rsquared(x, y):
#     """ Return R^2 where x and y are array-like."""

#     slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x, y)
#     return r_value**2

my_model = Model.load('PruebaMauleFinal_SinMedidas.json')
run = my_model.run()
print(run)

# Actual = pd.read_csv("Calibration/Embalses.csv")
# Futuro = pd.read_csv("output_flow.csv")

# dfactual = pd.DataFrame(Actual, columns = ["LagunaMaule","LagunaInvernada","EmbalseMelado","EmbalseColbun","EmbalseMachicura","Residual"])
# dffuturo = pd.DataFrame(Futuro, columns = ["LagunaMaule","LagunaInvernada","EmbalseMelado","EmbalseColbun","EmbalseMachicura","residual"])

# dffuturo = dffuturo.apply(pd.to_numeric, errors='coerce')
# dfactual = dfactual.apply(pd.to_numeric, errors='coerce')

# dfactual["CalMaule"] = 1-((((dfactual["LagunaMaule"]-dffuturo["LagunaMaule"])**2)**0.5)/dfactual["LagunaMaule"])
# dfactual["CalInvernada"] = 1-((((dfactual["LagunaInvernada"]-dffuturo["LagunaInvernada"])**2)**0.5)/dfactual["LagunaInvernada"])
# dfactual["CalMelado"] = 1-((((dfactual["EmbalseMelado"]-dffuturo["EmbalseMelado"])**2)**0.5)/dfactual["EmbalseMelado"])
# dfactual["CalColbun"] = 1-((((dfactual["EmbalseColbun"]-dffuturo["EmbalseColbun"])**2)**0.5)/dfactual["EmbalseColbun"])
# dfactual["CalMachicura"] = 1-((((dfactual["EmbalseMachicura"]-dffuturo["EmbalseMachicura"])**2)**0.5)/dfactual["EmbalseMachicura"])

# R2Maule = rsquared(Actual["LagunaMaule"],Futuro["LagunaMaule"])
# R2LI = rsquared(Actual["LagunaInvernada"],Futuro["LagunaInvernada"])
# R2Melado = rsquared(Actual["EmbalseMelado"],Futuro["EmbalseMelado"])
# R2Colbun = rsquared(Actual["EmbalseColbun"],Futuro["EmbalseColbun"])
# R2Machicura = rsquared(Actual["EmbalseMachicura"],Futuro["EmbalseMachicura"])

# print("Laguna Maule tiene "+str(round(dfactual["CalMaule"].mean()*100,2))+str(" % ")+"de ajuste y un coeficiente R2 de "+str(R2Maule))
# print("Laguna Invernada tiene "+str(round(dfactual["CalInvernada"].mean()*100,2))+str(" % ")+"de ajuste y un coeficiente R2 de "+str(R2LI))
# print("Embalse Melado tiene "+str(round(dfactual["CalMelado"].mean()*100,2))+str(" % ")+"de ajuste y un coeficiente R2 de "+str(R2Melado))
# print("Embalse Colbun tiene "+str(round(dfactual["CalColbun"].mean()*100,2))+str(" % ")+"de ajuste y un coeficiente R2 de "+str(R2Colbun))
# print("Embalse Machicura tiene "+str(round(dfactual["CalMachicura"].mean()*100,2))+str(" % ")+"de ajuste y un coeficiente R2 de "+str(R2Machicura))

#print(np.array(my_model.recorders["deficit_recorder"].values()))

df = my_model.to_dataframe()
df.to_csv('Recorders/Recorders_S14_SinMedidas.csv')    

#print(df.head())

# from matplotlib import pyplot as plt
# df["CentralCipreses_MWH"].plot(subplots=True)
# plt.show()

