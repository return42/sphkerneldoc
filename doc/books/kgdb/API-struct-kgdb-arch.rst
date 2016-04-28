.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-kgdb-arch:

================
struct kgdb_arch
================

*man struct kgdb_arch(9)*

*4.6.0-rc5*

Describe architecture specific values.


Synopsis
========

.. code-block:: c

    struct kgdb_arch {
      unsigned char gdb_bpt_instr[BREAK_INSTR_SIZE];
      unsigned long flags;
      int (* set_breakpoint) (unsigned long, char *);
      int (* remove_breakpoint) (unsigned long, char *);
      int (* set_hw_breakpoint) (unsigned long, int, enum kgdb_bptype);
      int (* remove_hw_breakpoint) (unsigned long, int, enum kgdb_bptype);
      void (* disable_hw_break) (struct pt_regs *regs);
      void (* remove_all_hw_break) (void);
      void (* correct_hw_break) (void);
      void (* enable_nmi) (bool on);
    };


Members
=======

gdb_bpt_instr[BREAK_INSTR_SIZE]
    The instruction to trigger a breakpoint.

flags
    Flags for the breakpoint, currently just ``KGDB_HW_BREAKPOINT``.

set_breakpoint
    Allow an architecture to specify how to set a software breakpoint.

remove_breakpoint
    Allow an architecture to specify how to remove a software
    breakpoint.

set_hw_breakpoint
    Allow an architecture to specify how to set a hardware breakpoint.

remove_hw_breakpoint
    Allow an architecture to specify how to remove a hardware
    breakpoint.

disable_hw_break
    Allow an architecture to specify how to disable hardware breakpoints
    for a single cpu.

remove_all_hw_break
    Allow an architecture to specify how to remove all hardware
    breakpoints.

correct_hw_break
    Allow an architecture to specify how to correct the hardware debug
    registers.

enable_nmi
    Manage NMI-triggered entry to KGDB


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
