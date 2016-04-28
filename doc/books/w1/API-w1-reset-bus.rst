.. -*- coding: utf-8; mode: rst -*-

.. _API-w1-reset-bus:

============
w1_reset_bus
============

*man w1_reset_bus(9)*

*4.6.0-rc5*

Issues a reset bus sequence.


Synopsis
========

.. c:function:: int w1_reset_bus( struct w1_master * dev )

Arguments
=========

``dev``
    the master device


Return
======

0=Device present, 1=No device present or error


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
