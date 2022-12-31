import datetime
import csv
import json
import pandas as pd
from pandas import Series, DataFrame


date = datetime.datetime.now().date()
#print("Hola, Bienvenido a mi automatizacion! Hoy es: ",date)


colegio_mate = pd.read_csv("students-mat2.csv")
print(colegio_mate)
try:
    colegio_mate.drop([1],axis=1)
    print('----------------------------')
    print(colegio_mate)
except:
    print("Algo salio mal...")

