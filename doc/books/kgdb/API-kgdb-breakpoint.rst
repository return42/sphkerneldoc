
.. _API-kgdb-breakpoint:

===============
kgdb_breakpoint
===============

*man kgdb_breakpoint(9)*

*4.6.0-rc1*

compiled in breakpoint


Synopsis
========

.. c:function:: void kgdb_breakpoint( void )

Arguments
=========

``void``
    no arguments


Description
===========

This will be implemented as a static inline per architecture. This function is called by the kgdb core to execute an architecture specific trap to cause kgdb to enter the exception
processing.
