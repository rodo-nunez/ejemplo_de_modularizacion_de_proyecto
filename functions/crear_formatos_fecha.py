import calendar
from datetime import datetime

def crear_formatos_fecha(periodo_YYYYMM):
    """
    Crea formatos de fecha a partir de un periodo en formato YYYYMM.

    Parameters:
    - periodo_YYYYMM (str): Periodo en formato YYYYMM.

    Returns:
    Tuple: Una tupla que contiene el periodo en formato YYYYMM, la fecha de inicio
    en formato YYYY-MM-DD, la fecha de inicio en formato YYYY-MM-DD y la fecha de fin
    en formato YYYY-MM-DD.

    Examples:
    >>> crear_formatos_fecha("202212")
    ('202212', datetime.date(2022, 12, 1), '2022-12-01', '2022-12-31')
    """
    anio = int(periodo_YYYYMM[0:4])
    mes = int(periodo_YYYYMM[4:6])

    cantidad_de_dias_del_mes = calendar.monthrange(anio, mes)[1]

    anio_mes_dia_formato_ini = f'{anio}-{mes}-01'
    anio_mes_dia_formato_fin = f'{anio}-{mes}-{cantidad_de_dias_del_mes}'
    formato_fecha_default = "%Y-%m-%d"

    anio_mes_dia_formato_ini_date = datetime.strptime(
        anio_mes_dia_formato_ini, formato_fecha_default).date()
    
    return periodo_YYYYMM, anio_mes_dia_formato_ini_date, anio_mes_dia_formato_ini, anio_mes_dia_formato_fin
