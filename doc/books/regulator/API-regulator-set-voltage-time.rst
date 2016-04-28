.. -*- coding: utf-8; mode: rst -*-

.. _API-regulator-set-voltage-time:

==========================
regulator_set_voltage_time
==========================

*man regulator_set_voltage_time(9)*

*4.6.0-rc5*

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

Provided with the starting and ending voltage, this function attempts to
calculate the time in microseconds required to rise or fall to this new
voltage.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
