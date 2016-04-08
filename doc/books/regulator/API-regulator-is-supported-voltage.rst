
.. _API-regulator-is-supported-voltage:

==============================
regulator_is_supported_voltage
==============================

*man regulator_is_supported_voltage(9)*

*4.6.0-rc1*

check if a voltage range can be supported


Synopsis
========

.. c:function:: int regulator_is_supported_voltage( struct regulator * regulator, int min_uV, int max_uV )

Arguments
=========

``regulator``
    Regulator to check.

``min_uV``
    Minimum required voltage in uV.

``max_uV``
    Maximum required voltage in uV.


Description
===========

Returns a boolean or a negative error code.
