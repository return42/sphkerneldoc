.. -*- coding: utf-8; mode: rst -*-

.. _API-regulator-can-change-voltage:

============================
regulator_can_change_voltage
============================

*man regulator_can_change_voltage(9)*

*4.6.0-rc5*

check if regulator can change voltage


Synopsis
========

.. c:function:: int regulator_can_change_voltage( struct regulator * regulator )

Arguments
=========

``regulator``
    regulator source


Description
===========

Returns positive if the regulator driver backing the source/client can
change its voltage, false otherwise. Useful for detecting fixed or dummy
regulators and disabling voltage change logic in the client driver.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
