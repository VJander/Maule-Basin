"""
Code to run the multi-objective model for Maule basin. Parameters that are variables are two: crop areas 
for cereals and legumes, replacing them with fruits and vineyards, and also the values for the new hedging curve
(both storage and buffer coefficient).
The platypus optimization library is used. 
"""
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import platypus
from pywr.optimisation.platypus import PlatypusWrapper
from matplotlib import pyplot as plt

# Load the Model
def get_model_data():
    with open('Model.json') as fh:
        data = json.load(fh)
    return data

# Define platypus algorithm, and variable storing
def platypus_main():
    wrapper = PlatypusWrapper(get_model_data())
    with platypus.ProcessPoolEvaluator() as evaluator:
        algorithm = platypus.NSGAIII(wrapper.problem, population_size=50, evaluator=evaluator, divisions_outer=6)
        algorithm.run(1)

    objective_names = []
    objective_directions = []
    for o in wrapper.model_objectives:
        direction = 'MIN' if o.is_objective == 'minimise' else 'MAX'        
        n = 'MO_{}_{}'.format(direction, o.name.replace('_', ' '))
        objective_names.append(n)
        objective_directions.append(1 if o.is_objective == 'minimise' else -1)
    objective_directions = np.array(objective_directions)
    objectives = pd.DataFrame([s.objectives[:]*objective_directions for s in algorithm.result], columns=objective_names)
    variables = pd.DataFrame([s.variables[:] for s in algorithm.result],
                    columns=['VAR_{}'.format(p.name.replace('_', ' ')) for p in wrapper.model_variables])
    recorders = pd.DataFrame([s.objectives[:] for s in algorithm.result],
                    columns=['REC_{}'.format(p.name.replace('_', ' ')) for p in wrapper.model_objectives])

    df = pd.concat([objectives, variables,recorders], axis=1)
    df.index.name = 'ID'
    df.to_csv('Maule Results.csv')  
    
    # from pandas.plotting import scatter_matrix
    # scatter_matrix(objectives)
    # plt.savefig('Two Reservoir Objectives.pdf', format='pdf')
    # plt.show()

# Use platypus created function
if __name__ == '__main__':
    platypus_main()

# Print to verify it runs
print("Success!")
