.. -*- coding: utf-8; mode: rst -*-

.. _API-regulator-set-mode:

==================
regulator_set_mode
==================

*man regulator_set_mode(9)*

*4.6.0-rc5*

set regulator operating mode


Synopsis
========

.. c:function:: int regulator_set_mode( struct regulator * regulator, unsigned int mode )

Arguments
=========

``regulator``
    regulator source

``mode``
    operating mode - one of the REGULATOR_MODE constants


Description
===========

Set regulator operating mode to increase regulator efficiency or improve
regulation performance.


NOTE
====

Regulator system constraints must be set for this regulator before
calling this function otherwise this call will fail.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
