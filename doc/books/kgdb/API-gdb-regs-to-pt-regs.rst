
.. _API-gdb-regs-to-pt-regs:

===================
gdb_regs_to_pt_regs
===================

*man gdb_regs_to_pt_regs(9)*

*4.6.0-rc1*

Convert GDB regs to ptrace regs.


Synopsis
========

.. c:function:: void gdb_regs_to_pt_regs( unsigned long * gdb_regs, struct pt_regs * regs )

Arguments
=========

``gdb_regs``
    A pointer to hold the registers we've received from GDB.

``regs``
    A pointer to a ``struct pt_regs`` to hold these values in.


Description
===========

Convert the GDB regs in ``gdb_regs`` into the pt_regs, and store them in ``regs``.
