from eigenschaften.Richtung import Richtung
from eigenschaften.Strom import Strom
from eigenschaften.Revpi import revpi
import time

def ofentür(strom):
    revpi.io.O_13.value = strom.value

def ofen_rein(strom):
    revpi.io.O_5.value = strom.value

def ofen_raus(strom):
    revpi.io.O_6.value = strom.value

def brenner(strom):
    revpi.io.O_9.value = strom.value

def ist_ofen_drinn():
    return True if revpi.io.I_5.value == 1 and revpi.io.I_4.value == 0 else False

def ist_ofen_draußen():
    return True if revpi.io.I_4.value == 1 and revpi.io.I_5.value == 0 else False

def bewege_ofen(richtung):
    if richtung == Richtung.REIN and ist_ofen_drinn() == False:
        ofen_rein(Strom.AN)
        while ist_ofen_drinn() == False:
            pass
        ofen_rein(Strom.AN)
    elif richtung == Richtung.RAUS and ist_ofen_draußen() == False:
        ofen_raus(Strom.AN)
        while ist_ofen_draußen() == False:
            pass
        ofen_raus(Strom.AUS)

def warte_auf_block_gesetzt():
    while revpi.io.I_2.value == 1:
        pass

def block_brennen():
    ofentür(Strom.AUS)

    brenner(Strom.AN)
    time.sleep(4)
    brenner(Strom.AUS)

    ofentür(Strom.AN)