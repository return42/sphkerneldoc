.. -*- coding: utf-8; mode: rst -*-

.. _API-regulator-disable:

=================
regulator_disable
=================

*man regulator_disable(9)*

*4.6.0-rc5*

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

Disable the regulator output voltage or current. Calls to
``regulator_enable`` must be balanced with calls to
``regulator_disable``.


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
