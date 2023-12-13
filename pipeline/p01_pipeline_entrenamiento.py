# Librerias ----------------------------------------

import os, sys
import argparse

# Preproceso ---------------------------------------- 

os.system(f"preprocessing/a01_preproceso.py")

os.system(f"preprocessing/a02_escalador.py")

os.system(f"preprocessing/a03_split_train_test.py")

# Modelo ---------------------------------------- 

os.system(f"models/b01_creacion_de_modelos.py")
