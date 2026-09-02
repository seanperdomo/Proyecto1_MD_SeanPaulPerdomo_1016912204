QUERY="SELECT+pl_name,pl_rade,pl_bmasse+FROM+ps"
URL="https://exoplanetarchive.ipac.caltech.edu/TAP/sync?format=csv&query=${QUERY}"
wget -q -O masasyradios.csv "$URL"
