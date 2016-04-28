.. -*- coding: utf-8; mode: rst -*-

.. _API-regulator-get-voltage:

=====================
regulator_get_voltage
=====================

*man regulator_get_voltage(9)*

*4.6.0-rc5*

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

If the regulator is disabled it will return the voltage value. This
function should not be used to determine regulator state.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
