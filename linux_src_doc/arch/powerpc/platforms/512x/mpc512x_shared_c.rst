.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/platforms/512x/mpc512x_shared.c

.. _`mpc512x_cs_config`:

mpc512x_cs_config
=================

.. c:function:: int mpc512x_cs_config(unsigned int cs, u32 val)

    Setup chip select configuration

    :param cs:
        chip select number
    :type cs: unsigned int

    :param val:
        chip select configuration value
    :type val: u32

.. _`mpc512x_cs_config.description`:

Description
-----------

Perform chip select configuration for devices on LocalPlus Bus.
Intended to dynamically reconfigure the chip select parameters
for configurable devices on the bus.

.. This file was automatic generated / don't edit.

