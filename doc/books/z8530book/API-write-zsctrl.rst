.. -*- coding: utf-8; mode: rst -*-

.. _API-write-zsctrl:

============
write_zsctrl
============

*man write_zsctrl(9)*

*4.6.0-rc5*

Write to a Z8530 control register


Synopsis
========

.. c:function:: void write_zsctrl( struct z8530_channel * c, u8 val )

Arguments
=========

``c``
    The Z8530 channel

``val``
    Value to write


Description
===========

Write directly to the control register on the Z8530


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
