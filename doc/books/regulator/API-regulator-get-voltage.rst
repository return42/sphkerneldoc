
.. _API-regulator-get-voltage:

=====================
regulator_get_voltage
=====================

*man regulator_get_voltage(9)*

*4.6.0-rc1*

get regulator output voltage


Synopsis
========

.. c:function:: int regulator_get_voltage( struct regulator * regulator )

Arguments
=========

``regulator``
    regulator source


Description
===========

This returns the current regulator voltage in uV.


NOTE
====

If the regulator is disabled it will return the voltage value. This function should not be used to determine regulator state.
