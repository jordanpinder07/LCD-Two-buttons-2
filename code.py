# Write your code here :-)
# code-lcd-i2c
# Author: Eric Z. Ayers <ericzundel@gmail.com>
"""Simple test for 16x2 character lcd with an I2C LCD backpack."""
import board
import digitalio
import time
import time
import board
import busio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

# Write your code here :-)
# code-lcd-i2c
# Author: Eric Z. Ayers <ericzundel@gmail.com>
"""Simple test for 16x2 character lcd with an I2C LCD backpack."""
import board
import digitalio
import time
import time
import board
import busio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

score_button = digitalio.DigitalInOut(board.GP10)
score_button.direction = digitalio.Direction.INPUT
score_button.pull = digitalio.Pull.UP

score_button.value

print(score_button.value)


score_button2 = digitalio.DigitalInOut(board.GP6)
score_button2.direction = digitalio.Direction.INPUT
score_button2.pull = digitalio.Pull.UP

score_button2.value

print(score_button2.value)

# Initialize the score variable
score = 0

# Initialize I2C bus.
# The Raspberry Pi pico has a number of pin pairs that can be used for I2C.
# One pin is SCL (clock) and the other is SDA (data).  See
# a pin diagram at https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf
i2c = busio.I2C(board.GP1, board.GP0)

# Talk to the LCD at I2C address 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=20)
lcd.set_backlight(True)

while True:
    print ("Button value:")
    print(score_button.value)
    if score_button.value == False:
        score = score + 50
        print("Button is pressed")
        time.sleep(0.2)
    else:
        print("Button not pressed")
        time.sleep(0.5)

    print ("Button2 value:")
    print(score_button2.value)
    if score_button2.value == False:
        score = score + 50
        print("Button2 is pressed")
        time.sleep(0.2)
    else:
        print("Button2 not pressed")
        time.sleep(0.5)

        print("refreshing LCD")
    lcd.clear()
    # Start at the first line, fifth column (numbering from zero).
    lcd.set_cursor_pos(0, 1)
    lcd.print("Pinball cowboy")
    # Start at the first line, fifth column (numbering from zero).
    lcd.set_cursor_pos(1, 2)
    lcd.print("Score: ")
    lcd.print(str(score))


