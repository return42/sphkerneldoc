.. -*- coding: utf-8; mode: rst -*-

.. _API-read-zsreg:

==========
read_zsreg
==========

*man read_zsreg(9)*

*4.6.0-rc5*

Read a register from a Z85230


Synopsis
========

.. c:function:: u8 read_zsreg( struct z8530_channel * c, u8 reg )

Arguments
=========

``c``
    Z8530 channel to read from (2 per chip)

``reg``
    Register to read


FIXME
=====

Use a spinlock.

Most of the Z8530 registers are indexed off the control registers. A
read is done by writing to the control register and reading the register
back. The caller must hold the lock


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
