
.. _API-kfifo-reset:

===========
kfifo_reset
===========

*man kfifo_reset(9)*

*4.6.0-rc1*

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

usage of ``kfifo_reset`` is dangerous. It should be only called when the fifo is exclusived locked or when it is secured that no other thread is accessing the fifo.
