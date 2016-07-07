.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/xilinx/xilinx_axienet.h

.. _`axidma_bd`:

struct axidma_bd
================

.. c:type:: struct axidma_bd

    Axi Dma buffer descriptor layout

.. _`axidma_bd.definition`:

Definition
----------

.. code-block:: c

    struct axidma_bd {
        u32 next;
        u32 reserved1;
        u32 phys;
        u32 reserved2;
        u32 reserved3;
        u32 reserved4;
        u32 cntrl;
        u32 status;
        u32 app0;
        u32 app1;
        u32 app2;
        u32 app3;
        u32 app4;
        u32 sw_id_offset;
        u32 reserved5;
        u32 reserved6;
    }

.. _`axidma_bd.members`:

Members
-------

next
    MM2S/S2MM Next Descriptor Pointer

reserved1
    Reserved and not used

phys
    MM2S/S2MM Buffer Address

reserved2
    Reserved and not used

reserved3
    Reserved and not used

reserved4
    Reserved and not used

cntrl
    MM2S/S2MM Control value

status
    MM2S/S2MM Status value

app0
    MM2S/S2MM User Application Field 0.

app1
    MM2S/S2MM User Application Field 1.

app2
    MM2S/S2MM User Application Field 2.

app3
    MM2S/S2MM User Application Field 3.

app4
    MM2S/S2MM User Application Field 4.

sw_id_offset
    MM2S/S2MM Sw ID

reserved5
    Reserved and not used

reserved6
    Reserved and not used

.. _`axienet_local`:

struct axienet_local
====================

.. c:type:: struct axienet_local

    axienet private per device data

.. _`axienet_local.definition`:

Definition
----------

.. code-block:: c

    struct axienet_local {
        struct net_device *ndev;
        struct device *dev;
        struct phy_device *phy_dev;
        struct device_node *phy_node;
        struct mii_bus *mii_bus;
        void __iomem *regs;
        void __iomem *dma_regs;
        struct tasklet_struct dma_err_tasklet;
        int tx_irq;
        int rx_irq;
        u32 phy_type;
        u32 options;
        u32 last_link;
        u32 features;
        struct axidma_bd *tx_bd_v;
        dma_addr_t tx_bd_p;
        struct axidma_bd *rx_bd_v;
        dma_addr_t rx_bd_p;
        u32 tx_bd_ci;
        u32 tx_bd_tail;
        u32 rx_bd_ci;
        u32 max_frm_size;
        u32 rxmem;
        int csum_offload_on_tx_path;
        int csum_offload_on_rx_path;
        u32 coalesce_count_rx;
        u32 coalesce_count_tx;
    }

.. _`axienet_local.members`:

Members
-------

ndev
    Pointer for net_device to which it will be attached.

dev
    Pointer to device structure

phy_dev
    Pointer to PHY device structure attached to the axienet_local

phy_node
    Pointer to device node structure

mii_bus
    Pointer to MII bus structure

regs
    Base address for the axienet_local device address space

dma_regs
    Base address for the axidma device address space

dma_err_tasklet
    Tasklet structure to process Axi DMA errors

tx_irq
    Axidma TX IRQ number

rx_irq
    Axidma RX IRQ number

phy_type
    Phy type to identify between MII/GMII/RGMII/SGMII/1000 Base-X

options
    AxiEthernet option word

last_link
    Phy link state in which the PHY was negotiated earlier

features
    Stores the extended features supported by the axienet hw

tx_bd_v
    Virtual address of the TX buffer descriptor ring

tx_bd_p
    Physical address(start address) of the TX buffer descr. ring

rx_bd_v
    Virtual address of the RX buffer descriptor ring

rx_bd_p
    Physical address(start address) of the RX buffer descr. ring

tx_bd_ci
    Stores the index of the Tx buffer descriptor in the ring being
    accessed currently. Used while alloc. BDs before a TX starts

tx_bd_tail
    Stores the index of the Tx buffer descriptor in the ring being
    accessed currently. Used while processing BDs after the TX
    completed.

rx_bd_ci
    Stores the index of the Rx buffer descriptor in the ring being
    accessed currently.

max_frm_size
    Stores the maximum size of the frame that can be that
    Txed/Rxed in the existing hardware. If jumbo option is
    supported, the maximum frame size would be 9k. Else it is
    1522 bytes (assuming support for basic VLAN)

rxmem
    Stores rx memory size for jumbo frame handling.

csum_offload_on_tx_path
    Stores the checksum selection on TX side.

csum_offload_on_rx_path
    Stores the checksum selection on RX side.

coalesce_count_rx
    Store the irq coalesce on RX side.

coalesce_count_tx
    Store the irq coalesce on TX side.

.. _`axienet_option`:

struct axienet_option
=====================

.. c:type:: struct axienet_option

    Used to set axi ethernet hardware options

.. _`axienet_option.definition`:

Definition
----------

.. code-block:: c

    struct axienet_option {
        u32 opt;
        u32 reg;
        u32 m_or;
    }

.. _`axienet_option.members`:

Members
-------

opt
    Option to be set.

reg
    Register offset to be written for setting the option

m_or
    Mask to be ORed for setting the option in the register

.. _`axienet_ior`:

axienet_ior
===========

.. c:function:: u32 axienet_ior(struct axienet_local *lp, off_t offset)

    Memory mapped Axi Ethernet register read

    :param struct axienet_local \*lp:
        Pointer to axienet local structure

    :param off_t offset:
        Address offset from the base address of Axi Ethernet core

.. _`axienet_ior.return`:

Return
------

The contents of the Axi Ethernet register

This function returns the contents of the corresponding register.

.. _`axienet_iow`:

axienet_iow
===========

.. c:function:: void axienet_iow(struct axienet_local *lp, off_t offset, u32 value)

    Memory mapped Axi Ethernet register write

    :param struct axienet_local \*lp:
        Pointer to axienet local structure

    :param off_t offset:
        Address offset from the base address of Axi Ethernet core

    :param u32 value:
        Value to be written into the Axi Ethernet register

.. _`axienet_iow.description`:

Description
-----------

This function writes the desired value into the corresponding Axi Ethernet
register.

.. This file was automatic generated / don't edit.

