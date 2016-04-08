
.. _API-regulator-force-disable:

=======================
regulator_force_disable
=======================

*man regulator_force_disable(9)*

*4.6.0-rc1*

force disable regulator output


Synopsis
========

.. c:function:: int regulator_force_disable( struct regulator * regulator )

Arguments
=========

``regulator``
    regulator source


Description
===========

Forcibly disable the regulator output voltage or current.


NOTE
====

this ⋆will⋆ disable the regulator output even if other consumer devices have it enabled. This should be used for situations when device damage will likely occur if the regulator is
not disabled (e.g. over temp).
