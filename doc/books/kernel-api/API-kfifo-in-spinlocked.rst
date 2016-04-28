.. -*- coding: utf-8; mode: rst -*-

.. _API-kfifo-in-spinlocked:

===================
kfifo_in_spinlocked
===================

*man kfifo_in_spinlocked(9)*

*4.6.0-rc5*

put data into the fifo using a spinlock for locking


Synopsis
========

.. c:function:: kfifo_in_spinlocked( fifo, buf, n, lock )

Arguments
=========

``fifo``
    address of the fifo to be used

``buf``
    the data to be added

``n``
    number of elements to be added

``lock``
    pointer to the spinlock to use for locking


Description
===========

This macro copies the given values buffer into the fifo and returns the
number of copied elements.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
