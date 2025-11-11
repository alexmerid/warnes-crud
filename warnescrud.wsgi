import sys
import os

from config import RUTA_APP
# RUTA_APP = '/media/alexander/Unidad_D/Warnes/warnes-crud/'

sys.path.insert(0, RUTA_APP)
os.environ['PYTHONPATH'] = RUTA_APP

from app import app as application