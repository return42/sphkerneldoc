
.. _API-regulator-list-hardware-vsel:

============================
regulator_list_hardware_vsel
============================

*man regulator_list_hardware_vsel(9)*

*4.6.0-rc1*

get the HW-specific register value for a selector


Synopsis
========

.. c:function:: int regulator_list_hardware_vsel( struct regulator * regulator, unsigned selector )

Arguments
=========

``regulator``
    regulator source

``selector``
    identify voltage to list


Description
===========

Converts the selector to a hardware-specific voltage selector that can be directly written to the regulator registers. The address of the voltage register can be determined by
calling ``regulator_get_hardware_vsel_register``.

On error a negative errno is returned.
