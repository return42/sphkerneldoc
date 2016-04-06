
.. _API-parport-read:

============
parport_read
============

*man parport_read(9)*

*4.6.0-rc1*

read a block of data from a parallel port


Synopsis
========

.. c:function:: ssize_t parport_read( struct parport * port, void * buffer, size_t len )

Arguments
=========

``port``
    port to read from

``buffer``
    data buffer (in kernel space)

``len``
    number of bytes of data to transfer


Description
===========

This will read up to ``len`` bytes of ``buffer`` to the port specified, using the IEEE 1284 transfer mode most recently negotiated to (using ``parport_negotiate``), as long as that
mode supports reverse transfers (peripheral to host).

It is the caller's responsibility to ensure that the first ``len`` bytes of ``buffer`` are available to write to.

This function returns the number of bytes transferred (if zero or positive), or else an error code.
