.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/controller/pcie-xilinx-nwl.c

.. _`nwl_pcie_map_bus`:

nwl_pcie_map_bus
================

.. c:function:: void __iomem *nwl_pcie_map_bus(struct pci_bus *bus, unsigned int devfn, int where)

    Get configuration base

    :param bus:
        Bus structure of current bus
    :type bus: struct pci_bus \*

    :param devfn:
        Device/function
    :type devfn: unsigned int

    :param where:
        Offset from base
    :type where: int

.. _`nwl_pcie_map_bus.return`:

Return
------

Base address of the configuration space needed to be
accessed.

.. This file was automatic generated / don't edit.

