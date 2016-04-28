.. -*- coding: utf-8; mode: rst -*-

.. _API-w1-touch-bit:

============
w1_touch_bit
============

*man w1_touch_bit(9)*

*4.6.0-rc5*

Generates a write-0 or write-1 cycle and samples the level.


Synopsis
========

.. c:function:: u8 w1_touch_bit( struct w1_master * dev, int bit )

Arguments
=========

``dev``
    the master device

``bit``
    0 - write a 0, 1 - write a 0 read the level


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
