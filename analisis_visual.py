import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Se crea la conexion

conn = sqlite3.connect('db_masas_y_radios.db')

# Se hace una consulta para escoger todos los datos

cons = "SELECT * FROM planetas"

# Se lee la base de datos con Pandas

df = pd.read_sql_query(cons, conn)
conn.close()

# Se grafican los datos y se guardan localmente

plt.plot(df['pl_rade'],df['pl_bmasse'],'o')
plt.xlabel(r'$R_\oplus$')
plt.ylabel(r'$M_\oplus$')
plt.grid(True)
plt.title("Masa vs. Radio")
plt.savefig('resultado.png')


