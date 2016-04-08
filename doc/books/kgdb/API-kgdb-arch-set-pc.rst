
.. _API-kgdb-arch-set-pc:

================
kgdb_arch_set_pc
================

*man kgdb_arch_set_pc(9)*

*4.6.0-rc1*

Generic call back to the program counter


Synopsis
========

.. c:function:: void kgdb_arch_set_pc( struct pt_regs * regs, unsigned long pc )

Arguments
=========

``regs``
    Current ``struct pt_regs``.

``pc``
    The new value for the program counter


Description
===========

This function handles updating the program counter and requires an architecture specific implementation.
