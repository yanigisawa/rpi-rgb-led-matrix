#!/usr/bin/env python
from samplebase import SampleBase
import time

class Pixel():
    def __init__(self, *args):
        self.x = args[0]
        self.y = args[1]
        self.red = args[2]
        self.green = args[3]
        self.blue = args[4]

class Mario(SampleBase):
    red = (155, 0, 0)
    yellow = (25, 25, 0)
    flesh = (155, 155, 0)
    brown = (32, 5, 0)
    blue = (0, 0, 155)

    def __init__(self, *args, **kwargs):
        super(Mario, self).__init__(*args, **kwargs)

    def clearScreen(self):
        for i in range(0, 32):
            for j in range(0, 16):
                self.canvas.SetPixel(i, j, 0, 0, 0)

    def run(self):
        x, y, step = 0, 0, 1
        self.canvas = self.matrix.CreateFrameCanvas()
        while True:
            #     offset_canvas.SetPixel(offset_canvas.height - 1 - x, x, 255, 0, 255)

            self.clearScreen()
            self.draw(self.getStanding(x, y))
            # self.draw(self.getJumping(x, y))

            time.sleep(0.2)
            x += step
            if x > 20 or x < 0:
                step *= -1

            self.canvas = self.matrix.SwapOnVSync(self.canvas)

    def draw(self, pixels):
        for p in pixels:
            self.canvas.SetPixel(p.x, p.y, p.red, p.green, p.blue)

    def getJumping(self, x, y):
        pixels = []
        pixels.append(Pixel(x + 4,  y + 0, *self.red))
        pixels.append(Pixel(x + 5,  y + 0, *self.red))
        pixels.append(Pixel(x + 6,  y + 0, *self.red))
        pixels.append(Pixel(x + 7,  y + 0, *self.red))
        pixels.append(Pixel(x + 8,  y + 0, *self.red))
        pixels.append(Pixel(x + 10,  y + 0, *self.flesh) )
        pixels.append(Pixel(x + 11,  y + 0, *self.flesh) )
        pixels.append(Pixel(x + 12,  y + 0, *self.flesh) )

        pixels.append(Pixel(x + 3,  y + 1, *self.red))
        pixels.append(Pixel(x + 4,  y + 1, *self.red))
        pixels.append(Pixel(x + 5,  y + 1, *self.red))
        pixels.append(Pixel(x + 6,  y + 1, *self.red))
        pixels.append(Pixel(x + 7,  y + 1, *self.red))
        pixels.append(Pixel(x + 8,  y + 1, *self.red))
        pixels.append(Pixel(x + 9,  y + 1, *self.red))
        pixels.append(Pixel(x + 10, y + 1, *self.red))
        pixels.append(Pixel(x + 11, y + 1, *self.red))

        # Head / Hair)
        pixels.append(Pixel(x + 3,  y + 2, *self.brown))
        pixels.append(Pixel(x + 4,  y + 2, *self.brown))
        pixels.append(Pixel(x + 5,  y + 2, *self.brown))
        # Skin)
        pixels.append(Pixel(x + 6,  y + 2, *self.flesh) )
        pixels.append(Pixel(x + 7,  y + 2, *self.flesh) )
        pixels.append(Pixel(x + 8,  y + 2, *self.brown))
        pixels.append(Pixel(x + 9,  y + 2, *self.flesh))

        pixels.append(Pixel(x + 2,  y + 3, *self.brown))
        pixels.append(Pixel(x + 3,  y + 3, *self.flesh))
        pixels.append(Pixel(x + 4,  y + 3, *self.brown))
        pixels.append(Pixel(x + 5,  y + 3, *self.flesh) )
        pixels.append(Pixel(x + 6,  y + 3, *self.flesh) )
        pixels.append(Pixel(x + 7,  y + 3, *self.flesh) )
        pixels.append(Pixel(x + 8,  y + 3, *self.brown))
        pixels.append(Pixel(x + 9,  y + 3, *self.flesh))
        pixels.append(Pixel(x + 10, y +  3, *self.flesh))
        pixels.append(Pixel(x + 11, y +  3,*self.flesh))


        pixels.append(Pixel(x + 2,  y + 4, *self.brown))
        pixels.append(Pixel(x + 3,  y + 4, *self.flesh))
        pixels.append(Pixel(x + 4,  y + 4, *self.brown))
        pixels.append(Pixel(x + 5,  y + 4, *self.brown))
        pixels.append(Pixel(x + 6,  y + 4, *self.flesh))
        pixels.append(Pixel(x + 7,  y + 4, *self.flesh))
        pixels.append(Pixel(x + 8,  y + 4, *self.flesh))
        pixels.append(Pixel(x + 9,  y + 4, *self.brown))
        pixels.append(Pixel(x + 10, y +  4, *self.flesh))
        pixels.append(Pixel(x + 11, y +  4, *self.flesh))
        pixels.append(Pixel(x + 12, y +  4, *self.flesh))


        pixels.append(Pixel(x + 2,  y + 5, *self.brown))
        pixels.append(Pixel(x + 3,  y + 5, *self.brown))
        pixels.append(Pixel(x + 4,  y + 5, *self.flesh))
        pixels.append(Pixel(x + 5,  y + 5, *self.flesh))
        pixels.append(Pixel(x + 6,  y + 5, *self.flesh))
        pixels.append(Pixel(x + 7,  y + 5, *self.flesh))
        pixels.append(Pixel(x + 8,  y + 5, *self.brown))
        pixels.append(Pixel(x + 9,  y + 5, *self.brown))
        pixels.append(Pixel(x + 10, y +  5, *self.brown))
        pixels.append(Pixel(x + 11, y +  5, *self.brown))


        pixels.append(Pixel(x + 3, y + 6, *self.flesh))
        pixels.append(Pixel(x + 4, y + 6, *self.flesh))
        pixels.append(Pixel(x + 5, y + 6, *self.flesh))
        pixels.append(Pixel(x + 6, y + 6, *self.flesh))
        pixels.append(Pixel(x + 7, y + 6, *self.flesh))
        pixels.append(Pixel(x + 8, y + 6, *self.flesh))
        pixels.append(Pixel(x + 9, y + 6, *self.flesh))


        # Body)
        pixels.append(Pixel(x + 2, y + 7, *self.red))
        pixels.append(Pixel(x + 3, y + 7, *self.red))
        pixels.append(Pixel(x + 4, y + 7, *self.blue))
        pixels.append(Pixel(x + 5, y + 7, *self.red))
        pixels.append(Pixel(x + 6, y + 7, *self.red))
        pixels.append(Pixel(x + 7, y + 7, *self.red))
        pixels.append(Pixel(x + 8, y + 7, *self.red))


        pixels.append(Pixel(x + 1, y + 8, *self.red))
        pixels.append(Pixel(x + 2, y + 8, *self.red))
        pixels.append(Pixel(x + 3, y + 8, *self.red))
        pixels.append(Pixel(x + 4, y + 8, *self.blue))
        pixels.append(Pixel(x + 5, y + 8, *self.red))
        pixels.append(Pixel(x + 6, y + 8, *self.red))
        pixels.append(Pixel(x + 7, y + 8, *self.blue))
        pixels.append(Pixel(x + 8, y + 8, *self.red))
        pixels.append(Pixel(x + 9, y + 8, *self.red))
        pixels.append(Pixel(x + 10, y + 8, *self.red))


        pixels.append(Pixel(x + 0, y + 9, *self.red))
        pixels.append(Pixel(x + 1, y + 9, *self.red))
        pixels.append(Pixel(x + 2, y + 9, *self.red))
        pixels.append(Pixel(x + 3, y + 9, *self.red))
        pixels.append(Pixel(x + 4, y + 9, *self.blue))
        pixels.append(Pixel(x + 5, y + 9, *self.blue))
        pixels.append(Pixel(x + 6, y + 9, *self.blue))
        pixels.append(Pixel(x + 7, y + 9, *self.blue))
        pixels.append(Pixel(x + 8, y + 9, *self.red))
        pixels.append(Pixel(x + 9, y + 9, *self.red))
        pixels.append(Pixel(x + 10, y + 9, *self.red))
        pixels.append(Pixel(x + 11, y + 9, *self.red))


        pixels.append(Pixel(x + 0, y + 10, *self.flesh))
        pixels.append(Pixel(x + 1, y + 10, *self.flesh))
        pixels.append(Pixel(x + 2, y + 10, *self.red))
        pixels.append(Pixel(x + 3, y + 10, *self.blue))
        pixels.append(Pixel(x + 4, y + 10, *self.yellow))
        pixels.append(Pixel(x + 5, y + 10, *self.blue))
        pixels.append(Pixel(x + 6, y + 10, *self.blue))
        pixels.append(Pixel(x + 7, y + 10, *self.yellow))
        pixels.append(Pixel(x + 8, y + 10, *self.blue))
        pixels.append(Pixel(x + 9, y + 10, *self.red))
        pixels.append(Pixel(x + 10, y + 10, *self.flesh))
        pixels.append(Pixel(x + 11, y + 10, *self.flesh))


        pixels.append(Pixel(x + 0, y + 11, *self.flesh))
        pixels.append(Pixel(x + 1, y + 11, *self.flesh))
        pixels.append(Pixel(x + 2, y + 11, *self.flesh))
        pixels.append(Pixel(x + 3, y + 11, *self.blue))
        pixels.append(Pixel(x + 4, y + 11, *self.blue))
        pixels.append(Pixel(x + 5, y + 11, *self.blue))
        pixels.append(Pixel(x + 6, y + 11, *self.blue))
        pixels.append(Pixel(x + 7, y + 11, *self.blue))
        pixels.append(Pixel(x + 8, y + 11, *self.blue))
        pixels.append(Pixel(x + 9, y + 11, *self.flesh))
        pixels.append(Pixel(x + 10, y + 11, *self.flesh))
        pixels.append(Pixel(x + 11, y + 11, *self.flesh))


        pixels.append(Pixel(x + 0, y + 12, *self.flesh))
        pixels.append(Pixel(x + 1, y + 12, *self.flesh))
        pixels.append(Pixel(x + 2, y + 12, *self.blue))
        pixels.append(Pixel(x + 3, y + 12, *self.blue))
        pixels.append(Pixel(x + 4, y + 12, *self.blue))
        pixels.append(Pixel(x + 5, y + 12, *self.blue))
        pixels.append(Pixel(x + 6, y + 12, *self.blue))
        pixels.append(Pixel(x + 7, y + 12, *self.blue))
        pixels.append(Pixel(x + 8, y + 12, *self.blue))
        pixels.append(Pixel(x + 9, y + 12, *self.blue))
        pixels.append(Pixel(x + 10, y + 12, *self.flesh))
        pixels.append(Pixel(x + 11, y + 12, *self.flesh))


        pixels.append(Pixel(x + 2, y + 13, *self.blue))
        pixels.append(Pixel(x + 3, y + 13, *self.blue))
        pixels.append(Pixel(x + 4, y + 13, *self.blue))
        pixels.append(Pixel(x + 7, y + 13, *self.blue))
        pixels.append(Pixel(x + 8, y + 13, *self.blue))
        pixels.append(Pixel(x + 9, y + 13, *self.blue))


        # Feet
        pixels.append(Pixel(x + 1,  y + 14, *self.brown))
        pixels.append(Pixel(x + 2,  y + 14, *self.brown))
        pixels.append(Pixel(x + 3,  y + 14, *self.brown))
        pixels.append(Pixel(x + 8,  y + 14, *self.brown))
        pixels.append(Pixel(x + 9,  y + 14, *self.brown))
        pixels.append(Pixel(x + 10,  y + 14, *self.brown))


        pixels.append(Pixel(x + 0,  y + 15, *self.brown))
        pixels.append(Pixel(x + 1,  y + 15, *self.brown))
        pixels.append(Pixel(x + 2,  y + 15, *self.brown))
        pixels.append(Pixel(x + 3,  y + 15, *self.brown))
        pixels.append(Pixel(x + 8,  y + 15, *self.brown))
        pixels.append(Pixel(x + 9,  y + 15, *self.brown))
        pixels.append(Pixel(x + 10,  y + 15, *self.brown))
        pixels.append(Pixel(x + 11,  y + 15, *self.brown))

        return pixels

    def getStanding(self, x, y):
        pixels = []
        pixels.append(Pixel(x + 4,  y + 0, *self.red))
        pixels.append(Pixel(x + 5,  y + 0, *self.red))
        pixels.append(Pixel(x + 6,  y + 0, *self.red))
        pixels.append(Pixel(x + 7,  y + 0, *self.red))
        pixels.append(Pixel(x + 8,  y + 0, *self.red))

        pixels.append(Pixel(x + 3,  y + 1, *self.red))
        pixels.append(Pixel(x + 4,  y + 1, *self.red))
        pixels.append(Pixel(x + 5,  y + 1, *self.red))
        pixels.append(Pixel(x + 6,  y + 1, *self.red))
        pixels.append(Pixel(x + 7,  y + 1, *self.red))
        pixels.append(Pixel(x + 8,  y + 1, *self.red))
        pixels.append(Pixel(x + 9,  y + 1, *self.red))
        pixels.append(Pixel(x + 10, y + 1, *self.red))
        pixels.append(Pixel(x + 11, y + 1, *self.red))

        # Head / Hair)
        pixels.append(Pixel(x + 3,  y + 2, *self.brown))
        pixels.append(Pixel(x + 4,  y + 2, *self.brown))
        pixels.append(Pixel(x + 5,  y + 2, *self.brown))
        # Skin)
        pixels.append(Pixel(x + 6,  y + 2, *self.flesh) )
        pixels.append(Pixel(x + 7,  y + 2, *self.flesh) )
        pixels.append(Pixel(x + 8,  y + 2, *self.brown))
        pixels.append(Pixel(x + 9,  y + 2, *self.flesh))

        pixels.append(Pixel(x + 2,  y + 3, *self.brown))
        pixels.append(Pixel(x + 3,  y + 3, *self.flesh))
        pixels.append(Pixel(x + 4,  y + 3, *self.brown))
        pixels.append(Pixel(x + 5,  y + 3, *self.flesh) )
        pixels.append(Pixel(x + 6,  y + 3, *self.flesh) )
        pixels.append(Pixel(x + 7,  y + 3, *self.flesh) )
        pixels.append(Pixel(x + 8,  y + 3, *self.brown))
        pixels.append(Pixel(x + 9,  y + 3, *self.flesh))
        pixels.append(Pixel(x + 10, y +  3, *self.flesh))
        pixels.append(Pixel(x + 11, y +  3,*self.flesh))


        pixels.append(Pixel(x + 2,  y + 4, *self.brown))
        pixels.append(Pixel(x + 3,  y + 4, *self.flesh))
        pixels.append(Pixel(x + 4,  y + 4, *self.brown))
        pixels.append(Pixel(x + 5,  y + 4, *self.brown))
        pixels.append(Pixel(x + 6,  y + 4, *self.flesh))
        pixels.append(Pixel(x + 7,  y + 4, *self.flesh))
        pixels.append(Pixel(x + 8,  y + 4, *self.flesh))
        pixels.append(Pixel(x + 9,  y + 4, *self.brown))
        pixels.append(Pixel(x + 10, y +  4, *self.flesh))
        pixels.append(Pixel(x + 11, y +  4, *self.flesh))
        pixels.append(Pixel(x + 12, y +  4, *self.flesh))


        pixels.append(Pixel(x + 2,  y + 5, *self.brown))
        pixels.append(Pixel(x + 3,  y + 5, *self.brown))
        pixels.append(Pixel(x + 4,  y + 5, *self.flesh))
        pixels.append(Pixel(x + 5,  y + 5, *self.flesh))
        pixels.append(Pixel(x + 6,  y + 5, *self.flesh))
        pixels.append(Pixel(x + 7,  y + 5, *self.flesh))
        pixels.append(Pixel(x + 8,  y + 5, *self.brown))
        pixels.append(Pixel(x + 9,  y + 5, *self.brown))
        pixels.append(Pixel(x + 10, y +  5, *self.brown))
        pixels.append(Pixel(x + 11, y +  5, *self.brown))


        pixels.append(Pixel(x + 3, y + 6, *self.flesh))
        pixels.append(Pixel(x + 4, y + 6, *self.flesh))
        pixels.append(Pixel(x + 5, y + 6, *self.flesh))
        pixels.append(Pixel(x + 6, y + 6, *self.flesh))
        pixels.append(Pixel(x + 7, y + 6, *self.flesh))
        pixels.append(Pixel(x + 8, y + 6, *self.flesh))
        pixels.append(Pixel(x + 9, y + 6, *self.flesh))


        # Body)
        pixels.append(Pixel(x + 2, y + 7, *self.red))
        pixels.append(Pixel(x + 3, y + 7, *self.red))
        pixels.append(Pixel(x + 4, y + 7, *self.blue))
        pixels.append(Pixel(x + 5, y + 7, *self.red))
        pixels.append(Pixel(x + 6, y + 7, *self.red))
        pixels.append(Pixel(x + 7, y + 7, *self.red))
        pixels.append(Pixel(x + 8, y + 7, *self.red))


        pixels.append(Pixel(x + 1, y + 8, *self.red))
        pixels.append(Pixel(x + 2, y + 8, *self.red))
        pixels.append(Pixel(x + 3, y + 8, *self.red))
        pixels.append(Pixel(x + 4, y + 8, *self.blue))
        pixels.append(Pixel(x + 5, y + 8, *self.red))
        pixels.append(Pixel(x + 6, y + 8, *self.red))
        pixels.append(Pixel(x + 7, y + 8, *self.blue))
        pixels.append(Pixel(x + 8, y + 8, *self.red))
        pixels.append(Pixel(x + 9, y + 8, *self.red))
        pixels.append(Pixel(x + 10, y + 8, *self.red))


        pixels.append(Pixel(x + 0, y + 9, *self.red))
        pixels.append(Pixel(x + 1, y + 9, *self.red))
        pixels.append(Pixel(x + 2, y + 9, *self.red))
        pixels.append(Pixel(x + 3, y + 9, *self.red))
        pixels.append(Pixel(x + 4, y + 9, *self.blue))
        pixels.append(Pixel(x + 5, y + 9, *self.blue))
        pixels.append(Pixel(x + 6, y + 9, *self.blue))
        pixels.append(Pixel(x + 7, y + 9, *self.blue))
        pixels.append(Pixel(x + 8, y + 9, *self.red))
        pixels.append(Pixel(x + 9, y + 9, *self.red))
        pixels.append(Pixel(x + 10, y + 9, *self.red))
        pixels.append(Pixel(x + 11, y + 9, *self.red))


        pixels.append(Pixel(x + 0, y + 10, *self.flesh))
        pixels.append(Pixel(x + 1, y + 10, *self.flesh))
        pixels.append(Pixel(x + 2, y + 10, *self.red))
        pixels.append(Pixel(x + 3, y + 10, *self.blue))
        pixels.append(Pixel(x + 4, y + 10, *self.yellow))
        pixels.append(Pixel(x + 5, y + 10, *self.blue))
        pixels.append(Pixel(x + 6, y + 10, *self.blue))
        pixels.append(Pixel(x + 7, y + 10, *self.yellow))
        pixels.append(Pixel(x + 8, y + 10, *self.blue))
        pixels.append(Pixel(x + 9, y + 10, *self.red))
        pixels.append(Pixel(x + 10, y + 10, *self.flesh))
        pixels.append(Pixel(x + 11, y + 10, *self.flesh))


        pixels.append(Pixel(x + 0, y + 11, *self.flesh))
        pixels.append(Pixel(x + 1, y + 11, *self.flesh))
        pixels.append(Pixel(x + 2, y + 11, *self.flesh))
        pixels.append(Pixel(x + 3, y + 11, *self.blue))
        pixels.append(Pixel(x + 4, y + 11, *self.blue))
        pixels.append(Pixel(x + 5, y + 11, *self.blue))
        pixels.append(Pixel(x + 6, y + 11, *self.blue))
        pixels.append(Pixel(x + 7, y + 11, *self.blue))
        pixels.append(Pixel(x + 8, y + 11, *self.blue))
        pixels.append(Pixel(x + 9, y + 11, *self.flesh))
        pixels.append(Pixel(x + 10, y + 11, *self.flesh))
        pixels.append(Pixel(x + 11, y + 11, *self.flesh))


        pixels.append(Pixel(x + 0, y + 12, *self.flesh))
        pixels.append(Pixel(x + 1, y + 12, *self.flesh))
        pixels.append(Pixel(x + 2, y + 12, *self.blue))
        pixels.append(Pixel(x + 3, y + 12, *self.blue))
        pixels.append(Pixel(x + 4, y + 12, *self.blue))
        pixels.append(Pixel(x + 5, y + 12, *self.blue))
        pixels.append(Pixel(x + 6, y + 12, *self.blue))
        pixels.append(Pixel(x + 7, y + 12, *self.blue))
        pixels.append(Pixel(x + 8, y + 12, *self.blue))
        pixels.append(Pixel(x + 9, y + 12, *self.blue))
        pixels.append(Pixel(x + 10, y + 12, *self.flesh))
        pixels.append(Pixel(x + 11, y + 12, *self.flesh))


        pixels.append(Pixel(x + 2, y + 13, *self.blue))
        pixels.append(Pixel(x + 3, y + 13, *self.blue))
        pixels.append(Pixel(x + 4, y + 13, *self.blue))
        pixels.append(Pixel(x + 7, y + 13, *self.blue))
        pixels.append(Pixel(x + 8, y + 13, *self.blue))
        pixels.append(Pixel(x + 9, y + 13, *self.blue))


        # Feet)
        pixels.append(Pixel(x + 1,  y + 14, *self.brown))
        pixels.append(Pixel(x + 2,  y + 14, *self.brown))
        pixels.append(Pixel(x + 3,  y + 14, *self.brown))
        pixels.append(Pixel(x + 8,  y + 14, *self.brown))
        pixels.append(Pixel(x + 9,  y + 14, *self.brown))
        pixels.append(Pixel(x + 10,  y + 14, *self.brown))


        pixels.append(Pixel(x + 0,  y + 15, *self.brown))
        pixels.append(Pixel(x + 1,  y + 15, *self.brown))
        pixels.append(Pixel(x + 2,  y + 15, *self.brown))
        pixels.append(Pixel(x + 3,  y + 15, *self.brown))
        pixels.append(Pixel(x + 8,  y + 15, *self.brown))
        pixels.append(Pixel(x + 9,  y + 15, *self.brown))
        pixels.append(Pixel(x + 10,  y + 15, *self.brown))
        pixels.append(Pixel(x + 11,  y + 15, *self.brown))
        return pixels
            


# Main function
if __name__ == "__main__":
    mario = Mario()
    if (not mario.process()):
        mario.print_help()
