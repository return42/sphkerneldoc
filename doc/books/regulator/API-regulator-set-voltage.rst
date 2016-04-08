
.. _API-regulator-set-voltage:

=====================
regulator_set_voltage
=====================

*man regulator_set_voltage(9)*

*4.6.0-rc1*

set regulator output voltage


Synopsis
========

.. c:function:: int regulator_set_voltage( struct regulator * regulator, int min_uV, int max_uV )

Arguments
=========

``regulator``
    regulator source

``min_uV``
    Minimum required voltage in uV

``max_uV``
    Maximum acceptable voltage in uV


Description
===========

Sets a voltage regulator to the desired output voltage. This can be set during any regulator state. IOW, regulator can be disabled or enabled.

If the regulator is enabled then the voltage will change to the new value immediately otherwise if the regulator is disabled the regulator will output at the new voltage when
enabled.


NOTE
====

If the regulator is shared between several devices then the lowest request voltage that meets the system constraints will be used. Regulator system constraints must be set for this
regulator before calling this function otherwise this call will fail.
