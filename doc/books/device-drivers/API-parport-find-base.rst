
.. _API-parport-find-base:

=================
parport_find_base
=================

*man parport_find_base(9)*

*4.6.0-rc1*

find a parallel port by base address


Synopsis
========

.. c:function:: struct parport ⋆ parport_find_base( unsigned long base )

Arguments
=========

``base``
    base I/O address


Description
===========

This returns the parallel port with the specified base address, or ``NULL`` if there is none.

There is an implicit ``parport_get_port`` done already; to throw away the reference to the port that ``parport_find_base`` gives you, use ``parport_put_port``.
