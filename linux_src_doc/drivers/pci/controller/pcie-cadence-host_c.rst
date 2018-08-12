.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/controller/pcie-cadence-host.c

.. _`cdns_pcie_rc`:

struct cdns_pcie_rc
===================

.. c:type:: struct cdns_pcie_rc

    private data for this PCIe Root Complex driver

.. _`cdns_pcie_rc.definition`:

Definition
----------

.. code-block:: c

    struct cdns_pcie_rc {
        struct cdns_pcie pcie;
        struct device *dev;
        struct resource *cfg_res;
        struct resource *bus_range;
        void __iomem *cfg_base;
        u32 max_regions;
        u32 no_bar_nbits;
        u16 vendor_id;
        u16 device_id;
    }

.. _`cdns_pcie_rc.members`:

Members
-------

pcie
    Cadence PCIe controller

dev
    pointer to PCIe device

cfg_res
    start/end offsets in the physical system memory to map PCI
    configuration space accesses

bus_range
    first/last buses behind the PCIe host controller

cfg_base
    IO mapped window to access the PCI configuration space of a
    single function at a time

max_regions
    maximum number of regions supported by the hardware

no_bar_nbits
    Number of bits to keep for inbound (PCIe -> CPU) address
    translation (nbits sets into the "no BAR match" register)

vendor_id
    PCI vendor ID

device_id
    PCI device ID

.. This file was automatic generated / don't edit.

