# Maule Basin Model

This readme has the objective of giving any user the capability for reproducing the data of the Maule Basin results for multi-objective optimization and modelling of the 
whole basin.

## Description

This repository includes a vast amount of files, each of them complemented the realization of the research that generated a Pareto frontier of solutions that balance objectives of financial, energetic and ecosystem nature. The logical investigative process included the following steps:
1. The use of a WEAP model of the Maule basin as the baseline to create a Pywr equivalent model.
2. The calibration of the resulting model with the WEAP model in order to validate statistical accuracy.
3. The use of different climate scenarios over the WEAP model to generate different inflows as inputs to the Pywr model (as the latter is unable to employ runoff, non-linear equations from temperature and precipitation).
4. The use of a multi-objective evolutionary algorithm (MOEA) to generate a Pareto Frontier of different climate change adaptation strategies over the Pywr model.
5. The visualization of results.

## Running the model

### Dependencies
To be able to reproduce the results and/or use the model, the following dependencies are required:
* Python
* Jupyter
* Pywr, which has the following required dependencies:
  * Cython
  * Numpy
  * NetworkX
  * Pandas
  * Packaging
  * GLPK and/or lpsolve
* Matplotlib
* (Optional): QGIS (for editable map)


### Key Files
The following files and folder names show the description of relevant documentation in order to understand the model behaviour and reproducibility
* *Model_PreStrategy.json* and *Model_PostStrategy*: Files that contains the .json model to represent the Maule Basin, before and after the inclusion of adaptation strategies, respectively. These models, however, needs an external python code in order to run.
* *WEAP Model/WEAP_Maule_Laja*: Folder that contains the WEAP model that was used to get the input base data (inflows) to the pywr model. This model must be used if the climatic scenario is desired to be changed or modified.
* *Tesis*: Folder that contains everything necessary to run the model without needing the WEAP operation or the .json model execution, as it has every scenario output and input file.
* *Tesis_MSc.ipynb*: Notebook file to conduct the multi-objective optimization of the *json* model. It has 4 main cells, and the author used Google Colab to run it.
* *Parallel Axis.ipynb* and *Parallel Axis2.ipynb*: Notebook files to generate the Parallel Axis outputs, based on the results of the multi-objective optimization (*Average_Results.xls* and *Comparative_Results.xls*, respectively). The author used Google Colab to run it.
* *Maule_parameters.py*: Custom created parameters for the *.json* model, as the recorders of this particular study required additional features. They must be imported locally.
* *MauleRun.py*: File to run the pywr (.json) model, and store the desired recorders. 


### Recreating Results

1. **Running Json Model**
      * Consider that to run the json Model, you need all installed dependencies specified in the respective section.
      * Open the *MauleRun.py*, and run it.
      * You can change the input file, in order to run the model with or without adaptation strategies.
    ```
    my_model = Model.load('Model_PreStrategy.json')
    ```
      * A recorder file is produced and stored in the *Recorders* folder. 

2. **Multi-Objective Optimization**
      * As processing takes time and consumes a considerable amount of CPU, the use of a computer cluster or a cloud based CPU/GPU like Google Colab in order to run the multi-objective optimization is strongly adviced. 14 Scenarios were run with the multi-optimization algorythm in this case, each one by separate.
      * Open the file Tesis MSc.ipynb , which includes the multi-optimization model. The author used Google Colab to run it. 
      * Run the first three cells in order to install numpy, mount the local drive (the folder named *Tesis* contains everything this route needs) and install the multi-objective optimization package (platypus) and pywr.
      * Open the File Directory before executing cell 4, as it is necessary to change one threshold in order to run the model. Use the following directory: usr/local/lib/python3.7/dist-packages/pywr/parameters/parameters.py, and change line 116 for the following
    ```
    default_interp_kwargs = dict(kind="linear", bounds_error=False)
    ```
    The bounds error configuration was switched to False. 
      * Run cell 4 (this process depends on the level of CPU, it might take several hours/days depending on the performance)
      * Congratulations! You ran one of 14 possible scenarios. In this case, the "S14" in the output file name indicates scenario 14. If you want to change scenario, go to the *PruebaMauleFinal_ConMedidas.json* and for each of the 20 "type": "dataframe" parameters found, change the column name to any other of the 14 in the input files.
    ```
    "name": "Caudal_Armerillo",
            "type": "catchment",
            "flow": {
                "type": "dataframe",
                "url": "Inputs/Q105.csv",
                "index_col": "Date",    
                "parse_dates": true,
                "column": "UKMO2"
            }
    ```

3. **Generate Visual Results**: The following files were used to generate visual results from every stage of the model
      * *GISMap*: Folder that contains every file to generate the GIS Map of the study zone in Figure 1. QGIS foftware required for opening.
      * *Scenarios.py*: Generates Figure 2, the impact of different climate change scenarios over Armerillo's Station monthly projected flow between 2020 and 2060.
      * *Embalses2.py*: Generates Figure 3, the model calibration by reservoir levels comparison. 
      * *Performance.py*: Generates Figure 6, the Climate Change projected impacts over system performance.
      * *PYWRTest.py*: Generates Figure 7, the performance results of different recorders considering three base scenarios: low, medium and high inflow levels. 
      * *Performance_Evolution.py*: Generates Figure 8, the evolution of performance indicators of agricultural and environmental performance after implementing adaptation strategies.
      * *Histogram.py*: Generates Figure 9, the frequency histogram of input variables. The 3-d stacked histograms were added manually from file *Histogram3d.py*.
      * *Variables_Scatter.py*: Generates Figure 10, the portfolio of hedging variables over two agricultural system performance indicators.
      * *Parallel Axis.ipynb* and *Parallel Axis2.ipynb*: These notebook files generate both parallel axis graphs (Figure 11), that include every objective and the different portfolios of solutions.
## Author

Contributor name and contact info

Vicente Jander 
[@VicenteJander](https://www.linkedin.com/in/vicente-jander-palma-a7a832117/)

## Version History

* 0.1
    * Initial Release

## Acknowledgments

Inspiration, code snippets, etc.
* [Pywr](https://github.com/pywr/pywr)
* [WEAP](https://www.weap21.org/)
