.. -*- coding: utf-8; mode: rst -*-

.. _API-z8530-status:

============
z8530_status
============

*man z8530_status(9)*

*4.6.0-rc5*

Handle a PIO status exception


Synopsis
========

.. c:function:: void z8530_status( struct z8530_channel * chan )

Arguments
=========

``chan``
    Z8530 channel to process


Description
===========

A status event occurred in PIO synchronous mode. There are several
reasons the chip will bother us here. A transmit underrun means we
failed to feed the chip fast enough and just broke a packet. A DCD
change is a line up or down.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
