.. -*- coding: utf-8; mode: rst -*-

.. _API-w1-touch-block:

==============
w1_touch_block
==============

*man w1_touch_block(9)*

*4.6.0-rc5*

Touches a series of bytes.


Synopsis
========

.. c:function:: void w1_touch_block( struct w1_master * dev, u8 * buf, int len )

Arguments
=========

``dev``
    the master device

``buf``
    pointer to the data to write

``len``
    the number of bytes to write


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
