.. -*- coding: utf-8; mode: rst -*-

.. _API-kfifo-peek-len:

==============
kfifo_peek_len
==============

*man kfifo_peek_len(9)*

*4.6.0-rc5*

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

This function returns the size of the next fifo record in number of
bytes.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
