
.. _API-regulator-set-current-limit:

===========================
regulator_set_current_limit
===========================

*man regulator_set_current_limit(9)*

*4.6.0-rc1*

set regulator output current limit


Synopsis
========

.. c:function:: int regulator_set_current_limit( struct regulator * regulator, int min_uA, int max_uA )

Arguments
=========

``regulator``
    regulator source

``min_uA``
    Minimum supported current in uA

``max_uA``
    Maximum supported current in uA


Description
===========

Sets current sink to the desired output current. This can be set during any regulator state. IOW, regulator can be disabled or enabled.

If the regulator is enabled then the current will change to the new value immediately otherwise if the regulator is disabled the regulator will output at the new current when
enabled.


NOTE
====

Regulator system constraints must be set for this regulator before calling this function otherwise this call will fail.
