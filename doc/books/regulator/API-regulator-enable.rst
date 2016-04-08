
.. _API-regulator-enable:

================
regulator_enable
================

*man regulator_enable(9)*

*4.6.0-rc1*

enable regulator output


Synopsis
========

.. c:function:: int regulator_enable( struct regulator * regulator )

Arguments
=========

``regulator``
    regulator source


Description
===========

Request that the regulator be enabled with the regulator output at the predefined voltage or current value. Calls to ``regulator_enable`` must be balanced with calls to
``regulator_disable``.


NOTE
====

the output value can be set by other drivers, boot loader or may be hardwired in the regulator.
