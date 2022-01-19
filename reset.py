import revpimodio2

revpi = revpimodio2.RevPiModIO(autorefresh = True)

def turn_all_off():
    revpi.io.O_1.value = 0
    revpi.io.O_2.value = 0
    revpi.io.O_3.value = 0
    revpi.io.O_4.value = 0
    revpi.io.O_5.value = 0
    revpi.io.O_6.value = 0
    revpi.io.O_7.value = 0
    revpi.io.O_8.value = 0
    revpi.io.O_9.value = 0
    revpi.io.O_10.value = 0
    revpi.io.O_11.value = 0
    revpi.io.O_12.value = 0
    revpi.io.O_13.value = 0
    revpi.io.O_14.value = 0

revpi.handlesignalend(turn_all_off)
revpi.mainloop(blocking=False)
revpi.io.O_10.value = 1

revpi.io.O_13.value = 1
revpi.io.O_6.value = 1

revpi.io.O_8.value = 1
while revpi.io.I_6.value == 0:
    pass
revpi.io.O_8.value = 0



revpi.io.O_2.value = 1
while revpi.io.I_10.value == 0:
    pass
revpi.io.O_2.value = 0




revpi.mainloop(blocking=Fals)