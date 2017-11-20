# ADXL345 Python example
#
#

from adxl345 import ADXL345
import math


def Pomiar():
        adxl345 = ADXL345()
        return adxl345.getAxes(True)


### oblicza kat odchylanie na podstawie wartosci odczytanych z akcelerometru
def get_tilt():
        As = Pomiar()
        angle = math.atan2(As['x'], -1*As['z'])*(180/math.pi)
        return angle






