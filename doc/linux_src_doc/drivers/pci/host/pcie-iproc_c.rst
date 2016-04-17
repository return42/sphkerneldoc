.. -*- coding: utf-8; mode: rst -*-

============
pcie-iproc.c
============


.. _`iproc_pcie_map_cfg_bus`:

iproc_pcie_map_cfg_bus
======================

.. c:function:: void __iomem *iproc_pcie_map_cfg_bus (struct pci_bus *bus, unsigned int devfn, int where)

    :param struct pci_bus \*bus:

        *undescribed*

    :param unsigned int devfn:

        *undescribed*

    :param int where:

        *undescribed*



.. _`iproc_pcie_map_cfg_bus.description`:

Description
-----------

by 'pci_lock' in drivers/pci/access.c



.. _`iproc_pcie_setup_ob`:

iproc_pcie_setup_ob
===================

.. c:function:: int iproc_pcie_setup_ob (struct iproc_pcie *pcie, u64 axi_addr, u64 pci_addr, resource_size_t size)

    :param struct iproc_pcie \*pcie:

        *undescribed*

    :param u64 axi_addr:

        *undescribed*

    :param u64 pci_addr:

        *undescribed*

    :param resource_size_t size:

        *undescribed*



.. _`iproc_pcie_setup_ob.outbound-address-translation`:

Outbound address translation
----------------------------


iproc_pcie_address = axi_address - axi_offset
OARR = iproc_pcie_address
OMAP = pci_addr

axi_addr -> iproc_pcie_address -> OARR -> OMAP -> pci_address

