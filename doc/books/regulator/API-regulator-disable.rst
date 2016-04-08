
.. _API-regulator-disable:

=================
regulator_disable
=================

*man regulator_disable(9)*

*4.6.0-rc1*

disable regulator output


Synopsis
========

.. c:function:: int regulator_disable( struct regulator * regulator )

Arguments
=========

``regulator``
    regulator source


Description
===========

Disable the regulator output voltage or current. Calls to ``regulator_enable`` must be balanced with calls to ``regulator_disable``.


NOTE
====

this will only disable the regulator output if no other consumer devices have it enabled, the regulator device supports disabling and machine constraints permit this operation.
