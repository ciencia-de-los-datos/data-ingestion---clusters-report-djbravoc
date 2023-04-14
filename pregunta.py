"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def ingest_data():
    tabla = pd.read_fwf("clusters_report.txt", skiprows=4, names=['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave']) 
    tabla.fillna(method="ffill", inplace=True)
    tabla = tabla.groupby(['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave'])['principales_palabras_clave'].apply(' '.join).reset_index() 
    tabla["cantidad_de_palabras_clave"] = tabla["cantidad_de_palabras_clave"].astype(int)
    tabla["porcentaje_de_palabras_clave"] = tabla["porcentaje_de_palabras_clave"].str.replace("%", "").str.replace(",", ".")
    tabla["porcentaje_de_palabras_clave"] = tabla["porcentaje_de_palabras_clave"].astype(float)
    tabla["principales_palabras_clave"] = tabla["principales_palabras_clave"].str.replace("\s+"," ", regex=True).str.replace(",+", ",", regex=True).str.rstrip(".")
    
    
    return tabla
