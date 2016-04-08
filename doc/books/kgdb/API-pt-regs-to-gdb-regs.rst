
.. _API-pt-regs-to-gdb-regs:

===================
pt_regs_to_gdb_regs
===================

*man pt_regs_to_gdb_regs(9)*

*4.6.0-rc1*

Convert ptrace regs to GDB regs


Synopsis
========

.. c:function:: void pt_regs_to_gdb_regs( unsigned long * gdb_regs, struct pt_regs * regs )

Arguments
=========

``gdb_regs``
    A pointer to hold the registers in the order GDB wants.

``regs``
    The ``struct pt_regs`` of the current process.


Description
===========

Convert the pt_regs in ``regs`` into the format for registers that GDB expects, stored in ``gdb_regs``.
