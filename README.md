AdafruitSI1145
==============
A block for reading data from the Adafruit SI1145 UV sensor through the Raspberry Pi I2C bus.

Follow the instructions [here](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c) for getting smbus and I2C set up before installing this block.
You will also need to install the SI1145.SI1145 package like so:
```
git clone https://github.com/THP-JOE/Python_SI1145.git
cd Python_SI1145
python3 setup.py install
```

Properties
----------
None

Inputs
------
- **default**:

Outputs
-------
- **default**: Signal with 'vis', 'ir', and 'uv_index' values read from the sensor.

Commands
--------
None
