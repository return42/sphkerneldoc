.. -*- coding: utf-8; mode: rst -*-

.. _API-clear-bit:

=========
clear_bit
=========

*man clear_bit(9)*

*4.6.0-rc5*

Clears a bit in memory


Synopsis
========

.. c:function:: void clear_bit( long nr, volatile unsigned long * addr )

Arguments
=========

``nr``
    Bit to clear

``addr``
    Address to start counting from


Description
===========

``clear_bit`` is atomic and may not be reordered. However, it does not
contain a memory barrier, so if it is used for locking purposes, you
should call ``smp_mb__before_atomic`` and/or ``smp_mb__after_atomic`` in
order to ensure changes are visible on other processors.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
