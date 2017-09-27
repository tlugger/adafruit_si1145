# Author: Joe Gutting
# With use of Adafruit SI1145 library for Arduino, Adafruit_GPIO.I2C & BMP Library by Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from nio.block.base import Block
from nio.properties import VersionPropertyd
from nio.signal.base import Signal


import SI1145.SI1145 as SI1145

class AdafruitSI1145(Block):

    def __init__(self):
            super().__init__()
            self.sensor = SI1145.SI1145()

    def process_signals(self, signals):
        for signal in signals:
            uv = self.sensor.readUV()
            uvIndex = uv / 100.0
            self.notify_signals([Signal({"vis": self.sensor.readVisible(),
                                     "ir": self.sensor.readIR(),
                                     "uv_index": uvIndex})])
