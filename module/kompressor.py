from eigenschaften.Strom import Strom
from eigenschaften.Revpi import revpi

def kompressor(strom):
    revpi.io.O_10.value = strom.value

def ist_kompressor_an():
    return True if revpi.io.O_10.value == 1 else False

def schalte_kompressor(strom):
    if strom == Strom.AN and ist_kompressor_an() == False:
        kompressor(Strom.AN)
    elif strom == Strom.AUS and ist_kompressor_an():
        kompressor(Strom.AN)