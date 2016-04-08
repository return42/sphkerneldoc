
.. _API-regulator-get-hardware-vsel-register:

====================================
regulator_get_hardware_vsel_register
====================================

*man regulator_get_hardware_vsel_register(9)*

*4.6.0-rc1*

get the HW voltage selector register


Synopsis
========

.. c:function:: int regulator_get_hardware_vsel_register( struct regulator * regulator, unsigned * vsel_reg, unsigned * vsel_mask )

Arguments
=========

``regulator``
    regulator source

``vsel_reg``
    voltage selector register, output parameter

``vsel_mask``
    mask for voltage selector bitfield, output parameter


Description
===========

Returns the hardware register offset and bitmask used for setting the regulator voltage. This might be useful when configuring voltage-scaling hardware or firmware that can make
I2C requests behind the kernel's back, for example.

On success, the output parameters ``vsel_reg`` and ``vsel_mask`` are filled in and 0 is returned, otherwise a negative errno is returned.
