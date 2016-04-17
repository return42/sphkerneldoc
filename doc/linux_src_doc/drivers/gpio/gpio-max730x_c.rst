.. -*- coding: utf-8; mode: rst -*-

==============
gpio-max730x.c
==============


.. _`pin_config_mask`:

PIN_CONFIG_MASK
===============

.. c:function:: PIN_CONFIG_MASK ()



.. _`pin_config_mask.description`:

Description
-----------

Copyright (C) 2008 Guennadi Liakhovetski, Pengutronix
Copyright (C) 2009 Wolfram Sang, Pengutronix

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License version 2 as
published by the Free Software Foundation.

The Maxim MAX7300/1 device is an I2C/SPI driven GPIO expander. There are
28 GPIOs. 8 of them can trigger an interrupt. See datasheet for more
details



.. _`pin_config_mask.note`:

Note
----

- DIN must be stable at the rising edge of clock.
- when writing:

  - always clock in 16 clocks at once
  - at DIN: D15 first, D0 last
  - D0..D7 = databyte, D8..D14 = commandbyte
  - D15 = low -> write command

- when reading

  - always clock in 16 clocks at once
  - at DIN: D15 first, D0 last
  - D0..D7 = dummy, D8..D14 = register address
  - D15 = high -> read command
  - raise CS and assert it again
  - always clock in 16 clocks at once
  - at DOUT: D15 first, D0 last
  - D0..D7 contains the data from the first cycle

The driver exports a standard gpiochip interface

