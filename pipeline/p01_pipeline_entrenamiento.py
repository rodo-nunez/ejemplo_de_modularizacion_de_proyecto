# Librerias ----------------------------------------

import os, sys
import argparse
sys.path.append(os.getcwd()) # Esto es para agregar al path la ruta de ejecución actual y poder importar respecto a la ruta del proyecto, desde donde se debe ejecutar el código
import params as params

# Argumentos por linea de comandos ---------------------------------------- 

parser = argparse.ArgumentParser()
parser.add_argument('--periodo', default=f'{params.periodo_YYYYMM}', help='periodo en formato YYYYMM')

try:
    args = parser.parse_args()
except argparse.ArgumentTypeError as e:
    print(f"Invalid argument: {e}")
    
# Definir extension de ejecutables ---------------------------------------- 

if params.sistema_operativo == 'Windows':
        extension_binarios = ".exe"
else:
        extension_binarios = ""

# Info ---------------------------------------- 

print(f"---------------------------------- \nComenzando proceso para periodo: {args.periodo}\n----------------------------------")

# Preproceso ---------------------------------------- 

os.system(f"python{extension_binarios} preprocessing/a01_preproceso.py")

os.system(f"python{extension_binarios} preprocessing/a02_escalador.py")

os.system(f"python{extension_binarios} preprocessing/a03_split_train_test.py")

# Modelo ---------------------------------------- 

os.system(f"python{extension_binarios} models/b01_creacion_de_modelos.py")
