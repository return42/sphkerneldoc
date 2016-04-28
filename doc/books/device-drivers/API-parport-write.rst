.. -*- coding: utf-8; mode: rst -*-

.. _API-parport-write:

=============
parport_write
=============

*man parport_write(9)*

*4.6.0-rc5*

write a block of data to a parallel port


Synopsis
========

.. c:function:: ssize_t parport_write( struct parport * port, const void * buffer, size_t len )

Arguments
=========

``port``
    port to write to

``buffer``
    data buffer (in kernel space)

``len``
    number of bytes of data to transfer


Description
===========

This will write up to ``len`` bytes of ``buffer`` to the port specified,
using the IEEE 1284 transfer mode most recently negotiated to (using
``parport_negotiate``), as long as that mode supports forward transfers
(host to peripheral).

It is the caller's responsibility to ensure that the first ``len`` bytes
of ``buffer`` are valid.

This function returns the number of bytes transferred (if zero or
positive), or else an error code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
