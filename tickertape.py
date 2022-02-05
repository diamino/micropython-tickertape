"""
MicroPython Ticker Tape (Lichtkrant) using a framebuffer subclassed display
https://github.com/diamino/micropython-tickertape

MIT License
Copyright (c) 2022 Diamino

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import time

class TickerTape:

    def __init__(self, display, num_segments, delay=0.1, inverse=False):
        self.display = display
        self.num_segments = num_segments
        self.delay = delay
        self.inverse = inverse
        self.text = "Hello World!"

    def start(self):
        while True:
            scrolltext = ((self.num_segments + 1) * ' ') + self.text
            for i in range(len(scrolltext)-1):
                self.display.fill(self.inverse)
                self.display.text(scrolltext[i:i+self.num_segments+2], 0 ,1, not self.inverse)
                self.display.show()
                for _ in range(8):
                    time.sleep(self.delay)
                    self.display.scroll(-1,0)
                    self.display.show()

def main():
    from machine import Pin, SPI
    import max7219

    NUM_SEGMENTS = 4

    spi = SPI(1, baudrate=10_000_000, polarity=0, phase=0)
    display = max7219.Matrix8x8(spi, cs=Pin(15), num=NUM_SEGMENTS, extended=True)
    display.brightness(0)
    
    tickertape = TickerTape(display, NUM_SEGMENTS)
    tickertape.start()

if __name__ == '__main__':
    main()
