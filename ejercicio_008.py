'''
Saúl Gómez García
Ejercicio #8
Curso Básico de Python
'''
import pandas as pd

notas = {'Juan':9,
         'Maria':6.5,
         'Pedro': 4,
         'Carmen': 8.5,
         'Luis':5}

def PandasDF(x):
    df = pd.DataFrame(x.items(), columns=["Nombre", "Nota"])
    aprobados = df.loc[df["Nota"]>=6].sort_values("Nota", ascending=False).set_index("Nombre")
    return aprobados

print(PandasDF(notas))

