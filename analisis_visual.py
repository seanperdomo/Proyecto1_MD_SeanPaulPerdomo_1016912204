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

plt.plot(np.log(df['pl_rade']),np.log(df['pl_bmasse']),'o',markersize=2)
plt.plot([np.log(2), np.log(2)],[np.log(df['pl_bmasse']).min(), np.log(df['pl_bmasse']).max()],'--', c='orange', label='Límite de radio para gigantes gaseosos')
plt.plot([np.log(df['pl_rade']).min(), np.log(df['pl_rade']).max()], [1,1], '--', c='orange', label='Límite de masa para gigantes gaseosos')
plt.xlabel(r'$R_\oplus$')
plt.ylabel(r'$M_\oplus$')
plt.grid(True)
plt.title("Masa vs. Radio")
plt.savefig('resultado.png')


