.. -*- coding: utf-8; mode: rst -*-

.. _API-regulator-is-supported-voltage:

==============================
regulator_is_supported_voltage
==============================

*man regulator_is_supported_voltage(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
