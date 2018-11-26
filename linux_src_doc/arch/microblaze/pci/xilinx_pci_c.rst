.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/microblaze/pci/xilinx_pci.c

.. _`xilinx_pci_fixup_bridge`:

xilinx_pci_fixup_bridge
=======================

.. c:function:: void xilinx_pci_fixup_bridge(struct pci_dev *dev)

    Block Xilinx PHB configuration.

    :param dev:
        *undescribed*
    :type dev: struct pci_dev \*

.. _`xilinx_pci_exclude_device`:

xilinx_pci_exclude_device
=========================

.. c:function:: int xilinx_pci_exclude_device(struct pci_controller *hose, u_char bus, u8 devfn)

    Don't do config access for non-root bus

    :param hose:
        *undescribed*
    :type hose: struct pci_controller \*

    :param bus:
        *undescribed*
    :type bus: u_char

    :param devfn:
        *undescribed*
    :type devfn: u8

.. _`xilinx_pci_exclude_device.description`:

Description
-----------

This is a hack.  Config access to any bus other than bus 0 does not
currently work on the ML510 so we prevent it here.

.. _`xilinx_early_pci_scan`:

xilinx_early_pci_scan
=====================

.. c:function:: void xilinx_early_pci_scan(struct pci_controller *hose)

    List pci config space for available devices

    :param hose:
        *undescribed*
    :type hose: struct pci_controller \*

.. _`xilinx_early_pci_scan.description`:

Description
-----------

List pci devices in very early phase.

.. _`xilinx_pci_init`:

xilinx_pci_init
===============

.. c:function:: void xilinx_pci_init( void)

    Find and register a Xilinx PCI host bridge

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

