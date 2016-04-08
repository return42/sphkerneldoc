
.. _API-regulator-set-voltage-time-sel:

==============================
regulator_set_voltage_time_sel
==============================

*man regulator_set_voltage_time_sel(9)*

*4.6.0-rc1*

get raise/fall time


Synopsis
========

.. c:function:: int regulator_set_voltage_time_sel( struct regulator_dev * rdev, unsigned int old_selector, unsigned int new_selector )

Arguments
=========

``rdev``
    regulator source device

``old_selector``
    selector for starting voltage

``new_selector``
    selector for target voltage


Description
===========

Provided with the starting and target voltage selectors, this function returns time in microseconds required to rise or fall to this new voltage

Drivers providing ramp_delay in regulation_constraints can use this as their ``set_voltage_time_sel`` operation.
