.. -*- coding: utf-8; mode: rst -*-

.. _API-kfifo-reset:

===========
kfifo_reset
===========

*man kfifo_reset(9)*

*4.6.0-rc5*

removes the entire fifo content


Synopsis
========

.. c:function:: kfifo_reset( fifo )

Arguments
=========

``fifo``
    address of the fifo to be used


Note
====

usage of ``kfifo_reset`` is dangerous. It should be only called when the
fifo is exclusived locked or when it is secured that no other thread is
accessing the fifo.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
