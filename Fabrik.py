from eigenschaften.Revpi import revpi
from eigenschaften.Richtung import Richtung
from eigenschaften.Strom import Strom
import time
from module.fließband import fließband_an, fließband
from module.kompressor import kompressor, schalte_kompressor, ist_kompressor_an
from module.ofen import bewege_ofen, block_brennen, brenner, ist_ofen_draußen, ofentür, warte_auf_block_gesetzt, ofen_rein, ofen_raus
from module.kran import bewege_kran, ist_kran_rechts, saugnapf, kran_links, kran_rechts, saugnapf_halterung
from module.drehteller import bewege_drehteller, drehteller_links, ist_drehteller_bei_start, bewege_drehteller_zum_kran, pusher, drehteller_rechts
from module.polierer import polierer




def turn_all_off():
    drehteller_rechts(Strom.AUS)
    drehteller_links(Strom.AUS)
    fließband(Strom.AUS)
    polierer(Strom.AUS)
    ofen_rein(Strom.AUS)
    ofen_raus(Strom.AUS)
    kran_links(Strom.AUS)
    kran_rechts(Strom.AUS)
    brenner(Strom.AUS)
    kompressor(Strom.AUS)
    saugnapf(Strom.AUS)
    saugnapf_halterung(Strom.AUS)
    ofentür(Strom.AUS)
    pusher(Strom.AUS)




def reset_all():
    schalte_kompressor(Strom.AN)
    if ist_ofen_draußen() == False:
        ofentür(Strom.AN)
        bewege_ofen(Richtung.RAUS)
        ofentür(Strom.AUS)
    bewege_kran(Richtung.RECHTS)
    if ist_drehteller_bei_start() == False:
        bewege_drehteller_zum_kran()
    if ist_ofen_draußen() == True and ist_drehteller_bei_start() == True and ist_kran_rechts() == True and ist_kompressor_an() == True:
        return True


revpi.handlesignalend(turn_all_off)
revpi.mainloop(blocking=False)



while True:
    
    if reset_all() == True:
        

        schalte_kompressor(Strom.AN)

        # 1 schritt = ofen
        warte_auf_block_gesetzt()
        ofentür(Strom.AN)
        bewege_ofen(Richtung.REIN)
        block_brennen()
        bewege_ofen(Richtung.RAUS)
        ofentür(Strom.AUS)
        
        # 2 schritt = transport Kran
        bewege_kran(Richtung.LINKS)
        saugnapf_halterung(Strom.AN)
        time.sleep(1)
        saugnapf(Strom.AN)
        time.sleep(1)
        saugnapf_halterung(Strom.AUS)
        bewege_kran(Richtung.RECHTS)
        saugnapf_halterung(Strom.AN)
        time.sleep(1)
        saugnapf(Strom.AUS)
        time.sleep(1)
        saugnapf_halterung(Strom.AUS)
        time.sleep(1)
        
        # 3 schritt = polierung
        bewege_drehteller(Richtung.RECHTS)
        polierer(Strom.AN)
        time.sleep(4)
        polierer(Strom.AUS)
        
        
        # schritt 4 = transport Teller
        bewege_drehteller(Richtung.RECHTS)
        pusher(Strom.AN)
        time.sleep(0.5)
        pusher(Strom.AUS)
        
        
        
        bewege_drehteller(Richtung.LINKS)
        bewege_drehteller(Richtung.LINKS)
        fließband_an(Richtung.RAUS)