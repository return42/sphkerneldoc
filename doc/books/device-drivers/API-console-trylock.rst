
.. _API-console-trylock:

===============
console_trylock
===============

*man console_trylock(9)*

*4.6.0-rc1*

try to lock the console system for exclusive use.


Synopsis
========

.. c:function:: int console_trylock( void )

Arguments
=========

``void``
    no arguments


Description
===========

Try to acquire a lock which guarantees that the caller has exclusive access to the console system and the console_drivers list.

returns 1 on success, and 0 on failure to acquire the lock.
