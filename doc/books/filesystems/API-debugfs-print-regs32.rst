
.. _API-debugfs-print-regs32:

====================
debugfs_print_regs32
====================

*man debugfs_print_regs32(9)*

*4.6.0-rc1*

use seq_print to describe a set of registers


Synopsis
========

.. c:function:: void debugfs_print_regs32( struct seq_file * s, const struct debugfs_reg32 * regs, int nregs, void __iomem * base, char * prefix )

Arguments
=========

``s``
    the seq_file structure being used to generate output

``regs``
    an array if struct debugfs_reg32 structures

``nregs``
    the length of the above array

``base``
    the base address to be used in reading the registers

``prefix``
    a string to be prefixed to every output line


Description
===========

This function outputs a text block describing the current values of some 32-bit hardware registers. It is meant to be used within debugfs files based on seq_file that need to show
registers, intermixed with other information. The prefix argument may be used to specify a leading string, because some peripherals have several blocks of identical registers, for
example configuration of dma channels
