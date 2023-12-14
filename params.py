# Librerias ---------------------------------------- 

import platform 
from functions.crear_formatos_fecha import *

# Systema operativo ---------------------------------------- 

sistema_operativo = platform.system()

# Entrenamiento o ejecucion ---------------------------------------- 

bool_entrtenamiento = False

# Fecha por defecto ---------------------------------------- 

periodo_YYYYMM_por_defecto = "202311"
periodo_YYYYMM, anio_mes_dia_formato_ini_date, anio_mes_dia_formato_ini, anio_mes_dia_formato_fin = crear_formatos_fecha(periodo_YYYYMM_por_defecto)