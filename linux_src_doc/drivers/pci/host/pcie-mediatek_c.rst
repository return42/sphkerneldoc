.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/host/pcie-mediatek.c

.. _`mtk_pcie_port`:

struct mtk_pcie_port
====================

.. c:type:: struct mtk_pcie_port

    PCIe port information

.. _`mtk_pcie_port.definition`:

Definition
----------

.. code-block:: c

    struct mtk_pcie_port {
        void __iomem *base;
        struct list_head list;
        struct mtk_pcie *pcie;
        struct reset_control *reset;
        struct clk *sys_ck;
        struct phy *phy;
        u32 lane;
        u32 index;
    }

.. _`mtk_pcie_port.members`:

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

sys_ck
    pointer to bus clock

phy
    pointer to phy control block

lane
    lane count

index
    port index

.. _`mtk_pcie`:

struct mtk_pcie
===============

.. c:type:: struct mtk_pcie

    PCIe host information

.. _`mtk_pcie.definition`:

Definition
----------

.. code-block:: c

    struct mtk_pcie {
        struct device *dev;
        void __iomem *base;
        struct clk *free_ck;
        struct resource io;
        struct resource pio;
        struct resource mem;
        struct resource busn;
        struct {
            resource_size_t mem;
            resource_size_t io;
        } offset;
        struct list_head ports;
    }

.. _`mtk_pcie.members`:

Members
-------

dev
    pointer to PCIe device

base
    IO mapped register base

free_ck
    free-run reference clock

io
    IO resource

pio
    PIO resource

mem
    non-prefetchable memory resource

busn
    bus range

offset
    IO / Memory offset

mem
    non-prefetchable memory resource

io
    IO resource

ports
    pointer to PCIe port information

.. This file was automatic generated / don't edit.

