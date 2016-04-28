.. -*- coding: utf-8; mode: rst -*-

.. _API-parport-find-base:

=================
parport_find_base
=================

*man parport_find_base(9)*

*4.6.0-rc5*

find a parallel port by base address


Synopsis
========

.. c:function:: struct parport * parport_find_base( unsigned long base )

Arguments
=========

``base``
    base I/O address


Description
===========

This returns the parallel port with the specified base address, or
``NULL`` if there is none.

There is an implicit ``parport_get_port`` done already; to throw away
the reference to the port that ``parport_find_base`` gives you, use
``parport_put_port``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
