.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/sysdev/xilinx_pci.c

.. _`xilinx_pci_fixup_bridge`:

xilinx_pci_fixup_bridge
=======================

.. c:function:: void xilinx_pci_fixup_bridge(struct pci_dev *dev)

    Block Xilinx PHB configuration.

    :param struct pci_dev \*dev:
        *undescribed*

.. _`xilinx_pci_exclude_device`:

xilinx_pci_exclude_device
=========================

.. c:function:: int xilinx_pci_exclude_device(struct pci_controller *hose, u_char bus, u8 devfn)

    Don't do config access for non-root bus

    :param struct pci_controller \*hose:
        *undescribed*

    :param u_char bus:
        *undescribed*

    :param u8 devfn:
        *undescribed*

.. _`xilinx_pci_exclude_device.description`:

Description
-----------

This is a hack.  Config access to any bus other than bus 0 does not
currently work on the ML510 so we prevent it here.

.. _`xilinx_pci_init`:

xilinx_pci_init
===============

.. c:function:: void xilinx_pci_init( void)

    Find and register a Xilinx PCI host bridge

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

