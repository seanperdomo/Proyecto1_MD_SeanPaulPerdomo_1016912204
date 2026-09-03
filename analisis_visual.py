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

logrs = np.log10(df['pl_rade'])
logms = np.log10(df['pl_bmasse'])
x = np.linspace(np.log10(2), logrs.max(), 100)
y1 = 1 * np.ones_like(x)
y2 = logms.max() * np.ones_like(x)


plt.plot(logrs, logms, 'o', c='red', markersize=2)
plt.fill_between(x, y1, y2, color = 'orange', label='Región de gigantes gaseosos', alpha = 0.4)
plt.xlabel(r'$\log{R_\oplus}$')
plt.ylabel(r'$\log{M_\oplus}$')
plt.legend()
plt.grid(True)
plt.title("Masa vs. Radio")
plt.savefig('resultado.png')
