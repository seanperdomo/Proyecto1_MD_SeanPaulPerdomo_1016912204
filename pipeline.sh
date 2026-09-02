QUERY="SELECT+pl_rade,pl_bmasse+FROM+ps"
URL="https://exoplanetarchive.ipac.caltech.edu/TAP/sync?format=csv&query=${QUERY}"
wget -q -O masasyradios.csv "$URL"

cat << 'EOF' > constructor_db.py
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
EOF

python3 constructor_db.py

cat << 'EOF' > analisis_visual.py
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
EOF
