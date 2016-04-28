.. -*- coding: utf-8; mode: rst -*-

.. _API-panic:

=====
panic
=====

*man panic(9)*

*4.6.0-rc5*

halt the system


Synopsis
========

.. c:function:: void panic( const char * fmt, ... )

Arguments
=========

``fmt``
    The text string to print

``...``
    variable arguments


Description
===========

Display a message, then perform cleanups.

This function never returns.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
