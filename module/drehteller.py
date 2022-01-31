from eigenschaften.Richtung import Richtung
from eigenschaften.Strom import Strom
from eigenschaften.Revpi import revpi

def pusher(strom):
    revpi.io.O_14.value = strom.value

def drehteller_rechts(strom):
    revpi.io.O_1.value = strom.value

def drehteller_links(strom):
    revpi.io.O_2.value = strom.value

def ist_drehteller_bei_start():
    return True if revpi.io.I_10.value == Strom.AN.value and revpi.io.I_7.value == Strom.AUS.value and revpi.io.I_9.value == Strom.AUS.value else False

def ist_drehteller_bei_fließband():
    return True if revpi.io.I_9.value == Strom.AN.value and revpi.io.I_7.value == Strom.AUS.value else False

def ist_drehteller_bei_polierer():
    return True if revpi.io.I_7.value == Strom.AN.value and revpi.io.I_9.value == Strom.AUS.value else False

def bewege_drehteller_zum_polierer():
    if ist_drehteller_bei_fließband() == False:
        drehteller_rechts(Strom.AN)
        while ist_drehteller_bei_polierer() == False:
            pass
        drehteller_rechts(Strom.AUS)
    else:
        drehteller_links(Strom.AN)
        while ist_drehteller_bei_polierer() == False:
            pass
        drehteller_links(Strom.AUS)

def bewege_drehteller_zum_fließband():
    drehteller_rechts(Strom.AN)
    while ist_drehteller_bei_fließband() == False:
        pass
    drehteller_rechts(Strom.AUS)

def bewege_drehteller_zum_kran():
    drehteller_links(Strom.AN)
    while ist_drehteller_bei_start() == False:
        pass
    drehteller_links(Strom.AUS)



def bewege_drehteller(richtung):
    if ist_drehteller_bei_start() and richtung == Richtung.RECHTS:
        bewege_drehteller_zum_polierer()

    elif ist_drehteller_bei_polierer() and richtung == Richtung.RECHTS:
        bewege_drehteller_zum_fließband()
    
    elif ist_drehteller_bei_polierer() and richtung == Richtung.LINKS:
        bewege_drehteller_zum_kran()

    elif ist_drehteller_bei_fließband() and richtung == Richtung.LINKS:
        bewege_drehteller_zum_polierer()