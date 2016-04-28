.. -*- coding: utf-8; mode: rst -*-

.. _API-sleeping-thread-to-gdb-regs:

===========================
sleeping_thread_to_gdb_regs
===========================

*man sleeping_thread_to_gdb_regs(9)*

*4.6.0-rc5*

Convert ptrace regs to GDB regs


Synopsis
========

.. c:function:: void sleeping_thread_to_gdb_regs( unsigned long * gdb_regs, struct task_struct * p )

Arguments
=========

``gdb_regs``
    A pointer to hold the registers in the order GDB wants.

``p``
    The ``struct task_struct`` of the desired process.


Description
===========

Convert the register values of the sleeping process in ``p`` to the
format that GDB expects. This function is called when kgdb does not have
access to the ``struct pt_regs`` and therefore it should fill the gdb
registers ``gdb_regs`` with what has been saved in
``struct thread_struct`` thread field during switch_to.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
