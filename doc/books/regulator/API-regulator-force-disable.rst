.. -*- coding: utf-8; mode: rst -*-

.. _API-regulator-force-disable:

=======================
regulator_force_disable
=======================

*man regulator_force_disable(9)*

*4.6.0-rc5*

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

this *will* disable the regulator output even if other consumer devices
have it enabled. This should be used for situations when device damage
will likely occur if the regulator is not disabled (e.g. over temp).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
