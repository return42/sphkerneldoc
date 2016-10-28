.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/host/pcie-xilinx-nwl.c

.. _`nwl_pcie_map_bus`:

nwl_pcie_map_bus
================

.. c:function:: void __iomem *nwl_pcie_map_bus(struct pci_bus *bus, unsigned int devfn, int where)

    Get configuration base

    :param struct pci_bus \*bus:
        Bus structure of current bus

    :param unsigned int devfn:
        Device/function

    :param int where:
        Offset from base

.. _`nwl_pcie_map_bus.return`:

Return
------

Base address of the configuration space needed to be
accessed.

.. This file was automatic generated / don't edit.

