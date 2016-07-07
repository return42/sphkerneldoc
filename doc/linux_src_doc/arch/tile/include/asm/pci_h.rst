.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/tile/include/asm/pci.h

.. _`pcie_host_bar0_size`:

PCIE_HOST_BAR0_SIZE
===================

.. c:function::  PCIE_HOST_BAR0_SIZE()

    size address range at the top of the 64-bit address space to serve as the PCI window, emulating the BAR0 space of an endpoint device. This window is used by the chip-to-chip applications running on the RC node. The reason for carving out this window is that Mem-Maps that back up this window will not overlap with those that map the real physical memory.

.. _`pcie_host_regs_size`:

PCIE_HOST_REGS_SIZE
===================

.. c:function::  PCIE_HOST_REGS_SIZE()

    gxpci_host_regs structure.

.. This file was automatic generated / don't edit.

