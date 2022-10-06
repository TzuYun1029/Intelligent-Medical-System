import time
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import RPi.GPIO as GPIO
import time
import Adafruit_SSD1306

GPIO_TRIGGER = 23
GPIO_ECHO = 24
disp = Adafruit_SSD1306.SSD1306_128_32(rst = 0)


def ultrasonic():
    #GPIO Mode (BOARD / BCM)
    GPIO.setmode(GPIO.BCM)

    #set GPIO Pins

    #set GPIO direction (IN / OUT)
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance


def display_text(text, *args):

    if len(args) < 2:
        FONT_SIZE = 15
    elif len(args) == 2:
        FONT_SIZE = 10
    else:
        FONT_SIZE = 8

    width = disp.width
    height = disp.height

    # 1 bit pixel
    image = Image.new('1', (width, height))
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("./ARIALUNI.TTF", FONT_SIZE)

    draw.rectangle((0, 0, width, height), outline = 0, fill = 0)
    draw.text((0, 0), text, font = font, fill = 255)

    if len(args) > 0:
        for i, item in enumerate(args):
            draw.text((0, (i + 1) * FONT_SIZE-1), item, font = font, fill = 255)

    disp.image(image)
    disp.display()



if __name__ == "__main__":

    ultrasonic()
    disp.begin()
    try:
        while True:
            output = "     " + str(round(distance(), 1))
            display_text('Distance', output)
            # print ("Measured Distance = %.1f cm" % dist)
            time.sleep(0.2)

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        disp.clear()
        disp.display()
        GPIO.cleanup()




    

