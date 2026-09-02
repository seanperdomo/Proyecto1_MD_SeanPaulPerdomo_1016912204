import numpy as np
import sqlite3
import pandas as pd

# Se lee el CSV con Pandas
df = pd.read_csv('masasyradios.csv')

# Se eliminan las filas que no tienen datos
df = df.dropna()

# Se crea la base de datos local
conn = sqlite3.connect('db_masas_y_radios.db')
df.to_sql('planetas', conn, if_exists='replace', index=False)
conn.close()
