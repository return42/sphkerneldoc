.. -*- coding: utf-8; mode: rst -*-

.. _API-regulator-list-voltage:

======================
regulator_list_voltage
======================

*man regulator_list_voltage(9)*

*4.6.0-rc5*

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

Returns a voltage that can be passed to ``regulator_set_voltage``\ (),
zero if this selector code can't be used on this system, or a negative
errno.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
