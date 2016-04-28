.. -*- coding: utf-8; mode: rst -*-

.. _API-kfifo-out-spinlocked:

====================
kfifo_out_spinlocked
====================

*man kfifo_out_spinlocked(9)*

*4.6.0-rc5*

get data from the fifo using a spinlock for locking


Synopsis
========

.. c:function:: kfifo_out_spinlocked( fifo, buf, n, lock )

Arguments
=========

``fifo``
    address of the fifo to be used

``buf``
    pointer to the storage buffer

``n``
    max. number of elements to get

``lock``
    pointer to the spinlock to use for locking


Description
===========

This macro get the data from the fifo and return the numbers of elements
copied.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
