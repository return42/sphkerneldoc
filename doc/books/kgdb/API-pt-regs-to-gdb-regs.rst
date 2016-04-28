.. -*- coding: utf-8; mode: rst -*-

.. _API-pt-regs-to-gdb-regs:

===================
pt_regs_to_gdb_regs
===================

*man pt_regs_to_gdb_regs(9)*

*4.6.0-rc5*

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

Convert the pt_regs in ``regs`` into the format for registers that GDB
expects, stored in ``gdb_regs``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
