.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/ethoc.c

.. _`ethoc`:

struct ethoc
============

.. c:type:: struct ethoc

    driver-private device structure

.. _`ethoc.definition`:

Definition
----------

.. code-block:: c

    struct ethoc {
        void __iomem *iobase;
        void __iomem *membase;
        int dma_alloc;
        resource_size_t io_region_size;
        bool big_endian;
        unsigned int num_bd;
        unsigned int num_tx;
        unsigned int cur_tx;
        unsigned int dty_tx;
        unsigned int num_rx;
        unsigned int cur_rx;
        void **vma;
        struct net_device *netdev;
        struct napi_struct napi;
        u32 msg_enable;
        spinlock_t lock;
        struct mii_bus *mdio;
        struct clk *clk;
        s8 phy_id;
        int old_link;
        int old_duplex;
    }

.. _`ethoc.members`:

Members
-------

iobase
    pointer to I/O memory region

membase
    pointer to buffer memory region

dma_alloc
    dma allocated buffer size

io_region_size
    I/O memory region size

big_endian
    *undescribed*

num_bd
    number of buffer descriptors

num_tx
    number of send buffers

cur_tx
    last send buffer written

dty_tx
    last buffer actually sent

num_rx
    number of receive buffers

cur_rx
    current receive buffer

vma
    pointer to array of virtual memory addresses for buffers

netdev
    pointer to network device structure

napi
    NAPI structure

msg_enable
    device state flags

lock
    device lock

mdio
    MDIO bus for PHY access

clk
    *undescribed*

phy_id
    address of attached PHY

old_link
    *undescribed*

old_duplex
    *undescribed*

.. _`ethoc_bd`:

struct ethoc_bd
===============

.. c:type:: struct ethoc_bd

    buffer descriptor

.. _`ethoc_bd.definition`:

Definition
----------

.. code-block:: c

    struct ethoc_bd {
        u32 stat;
        u32 addr;
    }

.. _`ethoc_bd.members`:

Members
-------

stat
    buffer statistics

addr
    physical memory address

.. _`ethoc_probe`:

ethoc_probe
===========

.. c:function:: int ethoc_probe(struct platform_device *pdev)

    initialize OpenCores ethernet MAC

    :param struct platform_device \*pdev:
        *undescribed*

.. _`ethoc_probe.pdev`:

pdev
----

platform device

.. _`ethoc_remove`:

ethoc_remove
============

.. c:function:: int ethoc_remove(struct platform_device *pdev)

    shutdown OpenCores ethernet MAC

    :param struct platform_device \*pdev:
        platform device

.. This file was automatic generated / don't edit.

