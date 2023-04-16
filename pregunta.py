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

    tabla = pd.read_fwf(        "clusters_report.txt", widths = [9, 16, 16, 80], header = None,
        names = ["cluster","cantidad_de_palabras_clave","porcentaje_de_palabras_clave", "-"],
        skip_blank_lines = False, converters = {"porcentaje_de_palabras_clave": 
        lambda x: x.rstrip(" %").replace(",",".")}).drop([0,1,2,3], axis=0)

    colum4 = tabla["-"]
    tabla = tabla[tabla["cluster"].notna()].drop("-", axis=1)
    tabla = tabla.astype({ "cluster": int, "cantidad_de_palabras_clave": int, "porcentaje_de_palabras_clave": float})

    c4Pro = []
    text = ""
    for lin in colum4:
        if isinstance(lin, str): text += lin+" "
        else:
            text = ", ".join([" ".join(x.split()) for x in text.split(",")])
            c4Pro.append(text.rstrip("."))
            text = ""
            continue

    tabla["principales_palabras_clave"] = c4Pro

    return tabla

