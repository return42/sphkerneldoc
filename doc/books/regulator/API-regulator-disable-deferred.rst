.. -*- coding: utf-8; mode: rst -*-

.. _API-regulator-disable-deferred:

==========================
regulator_disable_deferred
==========================

*man regulator_disable_deferred(9)*

*4.6.0-rc5*

disable regulator output with delay


Synopsis
========

.. c:function:: int regulator_disable_deferred( struct regulator * regulator, int ms )

Arguments
=========

``regulator``
    regulator source

``ms``
    miliseconds until the regulator is disabled


Description
===========

Execute ``regulator_disable`` on the regulator after a delay. This is
intended for use with devices that require some time to quiesce.


NOTE
====

this will only disable the regulator output if no other consumer devices
have it enabled, the regulator device supports disabling and machine
constraints permit this operation.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
