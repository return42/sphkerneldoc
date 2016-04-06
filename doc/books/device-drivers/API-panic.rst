
.. _API-panic:

=====
panic
=====

*man panic(9)*

*4.6.0-rc1*

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
