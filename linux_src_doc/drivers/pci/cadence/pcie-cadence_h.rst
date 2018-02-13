.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/cadence/pcie-cadence.h

.. _`cdns_pcie`:

struct cdns_pcie
================

.. c:type:: struct cdns_pcie

    private data for Cadence PCIe controller drivers

.. _`cdns_pcie.definition`:

Definition
----------

.. code-block:: c

    struct cdns_pcie {
        void __iomem *reg_base;
        struct resource *mem_res;
        bool is_rc;
        u8 bus;
    }

.. _`cdns_pcie.members`:

Members
-------

reg_base
    IO mapped register base

mem_res
    start/end offsets in the physical system memory to map PCI accesses

is_rc
    tell whether the PCIe controller mode is Root Complex or Endpoint.

bus
    In Root Complex mode, the bus number

.. This file was automatic generated / don't edit.

