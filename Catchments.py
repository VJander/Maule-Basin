### Codigo Exportacion Catchments para PYWR - Autor: Vicente Jander ###

import win32com.client as win32
import numpy as np
import time

#Parametros de entrada#
n=1000 #Cantidad de Iteraciones a realizar#

# Iniciamos entonces la API de WEAP con early binding:
# WEAP = win32.gencache.EnsureDispatch("WEAP.WEAPApplication")
WEAP = win32.Dispatch("WEAP.WEAPApplication")
time.sleep(15)

dir(WEAP)

# Para definir que mensajes queremos ver de WEAP (1:solo errores, 4: todos los mensajes):
WEAP.Verbose

# Para definir si es visible o no WEAP:
WEAP.Visible = True

# Definimos el area (modelo) sobre el cual trabajaremos:
WEAP.ActiveArea = "WEAP_Maule_Laja"

#Se genera una secuencia donde los parametros de entrada varian
#a medida que se itera la simulacion, se define variacion para
#crecimiento de poblacion, consumo, consumo agricola, areas y caudales.
    
WEAP.Calculate()

LI = "LI"
WEAP.LoadFavorite(LI)

#Se exportan los resultados en formato excel 
Invernada = r"C:\Users\USER\Desktop\T1\Tesis\LI.csv" 
WEAP.ExportResults(Invernada,False,True,True)

Puelche = "Puelche"
WEAP.LoadFavorite(Puelche)

#Se exportan los resultados en formato excel 
RioPuelche = r"C:\Users\USER\Desktop\T1\Tesis\Puelche.csv" 
WEAP.ExportResults(RioPuelche,False,True,True)

LagunaMauleArriba = "LagunaMauleArriba"
WEAP.LoadFavorite(LagunaMauleArriba)

#Se exportan los resultados en formato excel 
AArrMaule = r"C:\Users\USER\Desktop\T1\Tesis\LagunaMauleArriba.csv" 
WEAP.ExportResults(AArrMaule,False,True,True)

LagunaMauleAbajo = "LagunaMauleAbajo"
WEAP.LoadFavorite(LagunaMauleAbajo)

#Se exportan los resultados en formato excel 
AAbMaule = r"C:\Users\USER\Desktop\T1\Tesis\LagunaMauleAbajo.csv" 
WEAP.ExportResults(AAbMaule,False,True,True)

BocatomaCentrales = "BocatomaCentrales"
WEAP.LoadFavorite(BocatomaCentrales)

#Se exportan los resultados en formato excel 
BTCentrales = r"C:\Users\USER\Desktop\T1\Tesis\BocatomaCentrales.csv" 
WEAP.ExportResults(BTCentrales,False,True,True)

AALI1 = "AALI1"
WEAP.LoadFavorite(AALI1)

#Se exportan los resultados en formato excel 
AAInvernada1 = r"C:\Users\USER\Desktop\T1\Tesis\AALI1.csv" 
WEAP.ExportResults(AAInvernada1,False,True,True)

AALI2 = "AALI2"
WEAP.LoadFavorite(AALI2)

#Se exportan los resultados en formato excel 
AAInvernada2 = r"C:\Users\USER\Desktop\T1\Tesis\AALI2.csv" 
WEAP.ExportResults(AAInvernada2,False,True,True)

Colorado = "Colorado"
WEAP.LoadFavorite(Colorado)

#Se exportan los resultados en formato excel 
RioColorado = r"C:\Users\USER\Desktop\T1\Tesis\Colorado.csv" 
WEAP.ExportResults(RioColorado,False,True,True)

LasGarzas = "LasGarzas"
WEAP.LoadFavorite(LasGarzas)

#Se exportan los resultados en formato excel 
RioLasGarzas = r"C:\Users\USER\Desktop\T1\Tesis\LasGarzas.csv" 
WEAP.ExportResults(RioLasGarzas,False,True,True)

MauleAntesdeColbun = "MauleAntesdeColbun"
WEAP.LoadFavorite(MauleAntesdeColbun)

#Se exportan los resultados en formato excel 
MADC = r"C:\Users\USER\Desktop\T1\Tesis\MauleAntesdeColbun.csv" 
WEAP.ExportResults(MADC,False,True,True)

Claro = "Claro"
WEAP.LoadFavorite(Claro)

#Se exportan los resultados en formato excel 
RioClaro = r"C:\Users\USER\Desktop\T1\Tesis\Claro.csv" 
WEAP.ExportResults(RioClaro,False,True,True)

MauleAntesdeColbun2 = "MauleAntesdeColbun2"
WEAP.LoadFavorite(MauleAntesdeColbun2)

#Se exportan los resultados en formato excel 
MADC2 = r"C:\Users\USER\Desktop\T1\Tesis\MauleAntesdeColbun2.csv" 
WEAP.ExportResults(MADC2,False,True,True)

MeladoAlto = "MeladoAlto"
WEAP.LoadFavorite(MeladoAlto)

#Se exportan los resultados en formato excel 
MAlto = r"C:\Users\USER\Desktop\T1\Tesis\MeladoAlto.csv" 
WEAP.ExportResults(MAlto,False,True,True)

Melado = "Melado"
WEAP.LoadFavorite(Melado)

#Se exportan los resultados en formato excel 
Mel = r"C:\Users\USER\Desktop\T1\Tesis\Melado.csv" 
WEAP.ExportResults(Mel,False,True,True)

Melado2 = "Melado2"
WEAP.LoadFavorite(Melado2)

#Se exportan los resultados en formato excel 
Mel2 = r"C:\Users\USER\Desktop\T1\Tesis\Melado2.csv" 
WEAP.ExportResults(Mel2,False,True,True)

Caudal105 = "Q105"
WEAP.LoadFavorite(Caudal105)

#Se exportan los resultados en formato excel 
Res105 = r"C:\Users\USER\Desktop\T1\Tesis\Q105.csv" 
WEAP.ExportResults(Res105,False,True,True)

EntradaColbun = "EntradaColbun"
WEAP.LoadFavorite(EntradaColbun)

#Se exportan los resultados en formato excel 
InColb = r"C:\Users\USER\Desktop\T1\Tesis\EntradaColbun.csv" 
WEAP.ExportResults(InColb,False,True,True)










