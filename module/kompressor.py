from eigenschaften.Strom import Strom
from eigenschaften.Revpi import revpi

def ist_kompressor_an():
    return True if revpi.io.O_10.value == 1 else False

def schalte_kompressor(strom):
    if strom == Strom.AN and ist_kompressor_an() == False:
        revpi.io.O_10.value = 1
    elif strom == Strom.AUS and ist_kompressor_an() == True:
        revpi.io.O_10.value = 0