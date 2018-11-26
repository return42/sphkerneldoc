.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/controller/pcie-mediatek.c

.. _`mtk_pcie_soc`:

struct mtk_pcie_soc
===================

.. c:type:: struct mtk_pcie_soc

    differentiate between host generations

.. _`mtk_pcie_soc.definition`:

Definition
----------

.. code-block:: c

    struct mtk_pcie_soc {
        bool need_fix_class_id;
        struct pci_ops *ops;
        int (*startup)(struct mtk_pcie_port *port);
        int (*setup_irq)(struct mtk_pcie_port *port, struct device_node *node);
    }

.. _`mtk_pcie_soc.members`:

Members
-------

need_fix_class_id
    whether this host's class ID needed to be fixed or not

ops
    pointer to configuration access functions

startup
    pointer to controller setting functions

setup_irq
    pointer to initialize IRQ functions

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
        struct clk *ahb_ck;
        struct clk *axi_ck;
        struct clk *aux_ck;
        struct clk *obff_ck;
        struct clk *pipe_ck;
        struct phy *phy;
        u32 lane;
        u32 slot;
        int irq;
        struct irq_domain *irq_domain;
        struct irq_domain *inner_domain;
        struct irq_domain *msi_domain;
        struct mutex lock;
        DECLARE_BITMAP(msi_irq_in_use, MTK_MSI_IRQS_NUM);
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
    pointer to transaction/data link layer clock

ahb_ck
    pointer to AHB slave interface operating clock for CSR access
    and RC initiated MMIO access

axi_ck
    pointer to application layer MMIO channel operating clock

aux_ck
    pointer to pe2_mac_bridge and pe2_mac_core operating clock
    when pcie_mac_ck/pcie_pipe_ck is turned off

obff_ck
    pointer to OBFF functional block operating clock

pipe_ck
    pointer to LTSSM and PHY/MAC layer operating clock

phy
    pointer to PHY control block

lane
    lane count

slot
    port slot

irq
    GIC irq

irq_domain
    legacy INTx IRQ domain

inner_domain
    inner IRQ domain

msi_domain
    MSI IRQ domain

lock
    protect the msi_irq_in_use bitmap

msi_irq_in_use
    bit map for assigned MSI IRQ

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
        const struct mtk_pcie_soc *soc;
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

ports
    pointer to PCIe port information

soc
    pointer to SoC-dependent operations

.. This file was automatic generated / don't edit.

