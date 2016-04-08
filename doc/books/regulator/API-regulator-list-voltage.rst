
.. _API-regulator-list-voltage:

======================
regulator_list_voltage
======================

*man regulator_list_voltage(9)*

*4.6.0-rc1*

enumerate supported voltages


Synopsis
========

.. c:function:: int regulator_list_voltage( struct regulator * regulator, unsigned selector )

Arguments
=========

``regulator``
    regulator source

``selector``
    identify voltage to list


Context
=======

can sleep


Description
===========

Returns a voltage that can be passed to ``regulator_set_voltage``\ (), zero if this selector code can't be used on this system, or a negative errno.
