.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/mt7621-pci/pci-mt7621.c

.. _`mt7621_pcie_port`:

struct mt7621_pcie_port
=======================

.. c:type:: struct mt7621_pcie_port

    PCIe port information

.. _`mt7621_pcie_port.definition`:

Definition
----------

.. code-block:: c

    struct mt7621_pcie_port {
        void __iomem *base;
        struct list_head list;
        struct mt7621_pcie *pcie;
        struct reset_control *reset;
    }

.. _`mt7621_pcie_port.members`:

Members
-------

base
    IO mapped register base

list
    port list

pcie
    pointer to PCIe host info

reset
    pointer to port reset control

.. _`mt7621_pcie`:

struct mt7621_pcie
==================

.. c:type:: struct mt7621_pcie

    PCIe host information

.. _`mt7621_pcie.definition`:

Definition
----------

.. code-block:: c

    struct mt7621_pcie {
        void __iomem *base;
        struct device *dev;
        struct resource io;
        struct resource mem;
        struct resource busn;
        struct {
            resource_size_t mem;
            resource_size_t io;
        } offset;
        struct list_head ports;
    }

.. _`mt7621_pcie.members`:

Members
-------

base
    IO Mapped Register Base

dev
    Pointer to PCIe device

io
    IO resource

mem
    non-prefetchable memory resource

busn
    bus range

offset
    IO / Memory offset

ports
    pointer to PCIe port information

.. This file was automatic generated / don't edit.

