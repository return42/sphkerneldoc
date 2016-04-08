
.. _API-kgdb-arch-exit:

==============
kgdb_arch_exit
==============

*man kgdb_arch_exit(9)*

*4.6.0-rc1*

Perform any architecture specific uninitalization.


Synopsis
========

.. c:function:: void kgdb_arch_exit( void )

Arguments
=========

``void``
    no arguments


Description
===========

This function will handle the uninitalization of any architecture specific callbacks, for dynamic registration and unregistration.
