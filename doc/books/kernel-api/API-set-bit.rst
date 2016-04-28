.. -*- coding: utf-8; mode: rst -*-

.. _API-set-bit:

=======
set_bit
=======

*man set_bit(9)*

*4.6.0-rc5*

Atomically set a bit in memory


Synopsis
========

.. c:function:: void set_bit( long nr, volatile unsigned long * addr )

Arguments
=========

``nr``
    the bit to set

``addr``
    the address to start counting from


Description
===========

This function is atomic and may not be reordered. See ``__set_bit`` if
you do not require the atomic guarantees.


Note
====

there are no guarantees that this function will not be reordered on non
x86 architectures, so if you are writing portable code, make sure not to
rely on its reordering guarantees.

Note that ``nr`` may be almost arbitrarily large; this function is not
restricted to acting on a single-word quantity.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
