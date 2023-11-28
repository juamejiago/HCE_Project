# Manejar fechas con la librería datetime
from datetime import datetime

dt_inicio = datetime(2023, 11, 14, 8, 25)
dt_final = datetime(2023, 11, 27, 8, 55)

# getting the timestamp
ts_inicio = datetime.timestamp(dt_inicio)
ts_final = datetime.timestamp(dt_final)
print(ts_inicio, ts_final)

