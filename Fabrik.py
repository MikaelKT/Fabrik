import revpimodio2
import time

revpi = revpimodio2.RevPiModIO(autorefresh = True)

def turnalloff():
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

revpi.handlesignalend(turnalloff)
revpi.mainloop(blocking=False)
revpi.io.O_10.value = 1

while revpi.io.I_2.value == 1:
    pass
revpi.io.O_5.value = 1
revpi.io.O_13.value = 1

while revpi.io.I_5.value == 0:
    pass
revpi.io.O_5.value = 0

revpi.io.O_13.value = 0

revpi.io.O_9.value = 1
time.sleep(4)
revpi.io.O_9.value = 0

revpi.io.O_13.value = 1

revpi.io.O_6.value = 1
while revpi.io.I_4.value == 0:
    pass
revpi.io.O_6.value = 0
revpi.io.O_13.value = 0

revpi.io.O_7.value = 1
while revpi.io.I_3.value == 0:
    pass
revpi.io.O_7.value = 0

revpi.io.O_12.value = 1
time.sleep(1)
revpi.io.O_11.value = 1
time.sleep(1)
revpi.io.O_12.value = 0

revpi.io.O_8.value = 1
while revpi.io.I_6.value == 0:
    pass
revpi.io.O_8.value = 0

revpi.io.O_12.value = 1
time.sleep(1)
revpi.io.O_11.value = 0
revpi.io.O_12.value = 0
time.sleep(1)
revpi.io.O_1.value = 1
while revpi.io.I_7.value == 0:
    pass
revpi.io.O_1.value = 0

revpi.io.O_4.value = 1
time.sleep(4)
revpi.io.O_4.value = 0

revpi.io.O_1.value = 1
while revpi.io.I_9.value == 0:
    pass
revpi.io.O_1.value = 0

revpi.io.O_14.value = 1
time.sleep(0.5)
revpi.io.O_14.value = 0

revpi.io.O_10.value = 0

revpi.io.O_3.value = 1
while revpi.io.I_8.value == 1:
    pass
revpi.io.O_3.value = 0

revpi.io.O_2.value = 1
while revpi.io.I_10.value == 0:
    pass
revpi.io.O_2.value = 0