#!/usr/bin/env python
from samplebase import SampleBase


class Mario(SampleBase):
    def __init__(self, *args, **kwargs):
        super(Mario, self).__init__(*args, **kwargs)

    def run(self):
        c = self.matrix.CreateFrameCanvas()
        while True:
            #     offset_canvas.SetPixel(offset_canvas.height - 1 - x, x, 255, 0, 255)
            # Hat
            c.SetPixel(4, 0, 255, 0, 0)
            c.SetPixel(5, 0, 255, 0, 0)
            c.SetPixel(6, 0, 255, 0, 0)
            c.SetPixel(7, 0, 255, 0, 0)
            c.SetPixel(8, 0, 255, 0, 0)

            c.SetPixel(3, 1, 255, 0, 0)
            c.SetPixel(4, 1, 255, 0, 0)
            c.SetPixel(5, 1, 255, 0, 0)
            c.SetPixel(6, 1, 255, 0, 0)
            c.SetPixel(7, 1, 255, 0, 0)
            c.SetPixel(8, 1, 255, 0, 0)
            c.SetPixel(9, 1, 255, 0, 0)
            c.SetPixel(10,1, 255, 0, 0)
            c.SetPixel(11,1, 255, 0, 0)

            # Head / Hair
            c.SetPixel(3, 2, 139, 40, 40)
            c.SetPixel(4, 2, 139, 40, 40)
            c.SetPixel(5, 2, 139, 40, 40)
            # Skin
            c.SetPixel(6, 2, 255, 255, 0) 
            c.SetPixel(7, 2, 255, 255, 0) 
            c.SetPixel(8, 2, 139, 40, 40)
            c.SetPixel(9, 2, 255, 255, 0) 

            c.SetPixel(2, 3, 139, 40, 40)
            c.SetPixel(3, 3, 255, 255, 0) 
            c.SetPixel(4, 3, 139, 40, 40)
            c.SetPixel(4, 3, 255, 255, 0) 
            c.SetPixel(5, 3, 255, 255, 0) 
            c.SetPixel(6, 3, 255, 255, 0) 
            c.SetPixel(7, 3, 139, 40, 40)
            c.SetPixel(8, 3, 255, 255, 0) 
            c.SetPixel(9, 3, 255, 255, 0) 
            c.SetPixel(10, 3, 255, 255, 0) 



            c.SetPixel(3, 4, 255, 255, 0) 









            c = self.matrix.SwapOnVSync(c)
            


# Main function
if __name__ == "__main__":
    mario = Mario()
    if (not mario.process()):
        mario.print_help()
