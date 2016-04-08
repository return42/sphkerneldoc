
.. _API-kgdb-arch-init:

==============
kgdb_arch_init
==============

*man kgdb_arch_init(9)*

*4.6.0-rc1*

Perform any architecture specific initalization.


Synopsis
========

.. c:function:: int kgdb_arch_init( void )

Arguments
=========

``void``
    no arguments


Description
===========

This function will handle the initalization of any architecture specific callbacks.
