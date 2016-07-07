.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/pci/pci-ar2315.c

.. _`ar2315_pci_1ms_reg`:

AR2315_PCI_1MS_REG
==================

.. c:function::  AR2315_PCI_1MS_REG()

    and interrupt. PCI interface supports MMIO access method, but does not seem to support I/O ports.

.. _`ar2315_pci_1ms_reg.description`:

Description
-----------

Read/write operation in the region 0x80000000-0xBFFFFFFF causes
a memory read/write command on the PCI bus. 30 LSBs of address on
the bus are taken from memory read/write request and 2 MSBs are
determined by PCI unit configuration.

To work with the configuration space instead of memory is necessary set
the CFG_SEL bit in the PCI_MISC_CONFIG register.

Devices on the bus can perform DMA requests via chip BAR1. PCI host
controller BARs are programmend as if an external device is programmed.
Which means that during configuration, IDSEL pin of the chip should be
asserted.

We know (and support) only one board that uses the PCI interface -
Fonera 2.0g (FON2202). It has a USB EHCI controller connected to the
AR2315 PCI bus. IDSEL pin of USB controller is connected to AD[13] line
and IDSEL pin of AR2315 is connected to AD[16] line.

.. This file was automatic generated / don't edit.

