.. -*- coding: utf-8; mode: rst -*-

.. _intro:

************
Introduction
************

The main purpose of the Industrial I/O subsystem (IIO) is to provide
support for devices that in some sense perform either analog-to-digital
conversion (ADC) or digital-to-analog conversion (DAC) or both. The aim
is to fill the gap between the somewhat similar hwmon and input
subsystems. Hwmon is directed at low sample rate sensors used to monitor
and control the system itself, like fan speed control or temperature
measurement. Input is, as its name suggests, focused on human
interaction input devices (keyboard, mouse, touchscreen). In some cases
there is considerable overlap between these and IIO.

Devices that fall into this category include:

-  analog to digital converters (ADCs)
-  accelerometers
-  capacitance to digital converters (CDCs)
-  digital to analog converters (DACs)
-  gyroscopes
-  inertial measurement units (IMUs)
-  color and light sensors
-  magnetometers
-  pressure sensors
-  proximity sensors
-  temperature sensors

Usually these sensors are connected via SPI or I2C. A common use case of
the sensors devices is to have combined functionality (e.g. light plus
proximity sensor).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/dbxml2rst). The origin XML comes
.. from the linux kernel:
..
..   http://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git
.. ------------------------------------------------------------------------------
