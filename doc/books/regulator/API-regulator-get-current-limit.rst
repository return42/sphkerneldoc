
.. _API-regulator-get-current-limit:

===========================
regulator_get_current_limit
===========================

*man regulator_get_current_limit(9)*

*4.6.0-rc1*

get regulator output current


Synopsis
========

.. c:function:: int regulator_get_current_limit( struct regulator * regulator )

Arguments
=========

``regulator``
    regulator source


Description
===========

This returns the current supplied by the specified current sink in uA.


NOTE
====

If the regulator is disabled it will return the current value. This function should not be used to determine regulator state.
