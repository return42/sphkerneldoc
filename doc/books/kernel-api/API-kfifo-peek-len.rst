
.. _API-kfifo-peek-len:

==============
kfifo_peek_len
==============

*man kfifo_peek_len(9)*

*4.6.0-rc1*

gets the size of the next fifo record


Synopsis
========

.. c:function:: kfifo_peek_len( fifo )

Arguments
=========

``fifo``
    address of the fifo to be used


Description
===========

This function returns the size of the next fifo record in number of bytes.
