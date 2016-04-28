.. -*- coding: utf-8; mode: rst -*-

.. _API-console-lock:

============
console_lock
============

*man console_lock(9)*

*4.6.0-rc5*

lock the console system for exclusive use.


Synopsis
========

.. c:function:: void console_lock( void )

Arguments
=========

``void``
    no arguments


Description
===========

Acquires a lock which guarantees that the caller has exclusive access to
the console system and the console_drivers list.

Can sleep, returns nothing.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
