import rotatescreen
import time

screen = rotatescreen.get_primary_display()
for i in range(2):
    for j in range(5):
        angle = j * 90 % 360
        screen.rotate_to(angle)
        time.sleep(1)