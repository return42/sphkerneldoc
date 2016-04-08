
.. _API-regulator-set-voltage-time:

==========================
regulator_set_voltage_time
==========================

*man regulator_set_voltage_time(9)*

*4.6.0-rc1*

get raise/fall time


Synopsis
========

.. c:function:: int regulator_set_voltage_time( struct regulator * regulator, int old_uV, int new_uV )

Arguments
=========

``regulator``
    regulator source

``old_uV``
    starting voltage in microvolts

``new_uV``
    target voltage in microvolts


Description
===========

Provided with the starting and ending voltage, this function attempts to calculate the time in microseconds required to rise or fall to this new voltage.
