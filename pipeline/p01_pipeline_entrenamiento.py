# Librerias ----------------------------------------

import os, sys
import argparse
import params as params

# Definir extension de ejecutables ---------------------------------------- 

if params.sistema_operativo == 'Windows':
        extension_binarios = ".exe"
else:
        extension_binarios = ""

# Preproceso ---------------------------------------- 

os.system(f"python{extension_binarios} preprocessing/a01_preproceso.py")

os.system(f"python{extension_binarios} preprocessing/a02_escalador.py")

os.system(f"python{extension_binarios} preprocessing/a03_split_train_test.py")

# Modelo ---------------------------------------- 

os.system(f"python{extension_binarios} models/b01_creacion_de_modelos.py")
