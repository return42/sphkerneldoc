.. -*- coding: utf-8; mode: rst -*-

================
mpc512x_shared.c
================


.. _`mpc512x_cs_config`:

mpc512x_cs_config
=================

.. c:function:: int mpc512x_cs_config (unsigned int cs, u32 val)

    Setup chip select configuration

    :param unsigned int cs:
        chip select number

    :param u32 val:
        chip select configuration value



.. _`mpc512x_cs_config.description`:

Description
-----------

Perform chip select configuration for devices on LocalPlus Bus.
Intended to dynamically reconfigure the chip select parameters
for configurable devices on the bus.

