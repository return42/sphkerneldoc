
.. _API-console-lock:

============
console_lock
============

*man console_lock(9)*

*4.6.0-rc1*

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

Acquires a lock which guarantees that the caller has exclusive access to the console system and the console_drivers list.

Can sleep, returns nothing.
