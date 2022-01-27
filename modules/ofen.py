from enum import Enum
from threading import Thread
import revpimodio2
import time

class Richtung(Enum):
    LINKS = 1
    RECHTS = 2
    REIN = LINKS
    RAUS = RECHTS

class Strom(Enum):
    AN = 1
    AUS = 0

def ist_ofen_drinn():
    return True if revpi.io.I_5.value == 1 and revpi.io.I_4.value == 0 else False

def ist_ofen_draußen():
    return True if revpi.io.I_4.value == 1 and revpi.io.I_5.value == 0 else False

def bewege_ofen(richtung):
    if richtung == Richtung.REIN and ist_ofen_drinn() == False:
        revpi.io.O_5.value = 1
        while ist_ofen_drinn() == False:
            pass
        revpi.io.O_5.value = 0
    elif richtung == Richtung.RAUS and ist_ofen_draußen() == False:
        revpi.io.O_6.value = 1
        while ist_ofen_draußen() == False:
            pass
        revpi.io.O_6.value = 0

revpi = revpimodio2.RevPiModIO(autorefresh = True)