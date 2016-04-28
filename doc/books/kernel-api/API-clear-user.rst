.. -*- coding: utf-8; mode: rst -*-

.. _API-clear-user:

==========
clear_user
==========

*man clear_user(9)*

*4.6.0-rc5*

Zero a block of memory in user space.


Synopsis
========

.. c:function:: unsigned long clear_user( void __user * to, unsigned long n )

Arguments
=========

``to``
    Destination address, in user space.

``n``
    Number of bytes to zero.


Description
===========

Zero a block of memory in user space.

Returns number of bytes that could not be cleared. On success, this will
be zero.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
