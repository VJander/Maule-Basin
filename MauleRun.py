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

my_model = Model.load('Model_PreStrategy.json')
run = my_model.run()
print(run)

df = my_model.to_dataframe()
df.to_csv('Recorders/Recorders_SX.csv')    

