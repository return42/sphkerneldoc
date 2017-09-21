.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/cavium/nitrox/nitrox_dev.h

.. _`max_msix_vectors`:

MAX_MSIX_VECTORS
================

.. c:function::  MAX_MSIX_VECTORS()

    error condition/mailbox.

.. _`nitrox_device`:

struct nitrox_device
====================

.. c:type:: struct nitrox_device

    NITROX Device Information.

.. _`nitrox_device.definition`:

Definition
----------

.. code-block:: c

    struct nitrox_device {
        struct list_head list;
        u8 __iomem *bar_addr;
        struct pci_dev *pdev;
        unsigned long status;
        unsigned long timeout;
        refcount_t refcnt;
        u8 idx;
        int node;
        u16 qlen;
        u16 nr_queues;
        struct dma_pool *ctx_pool;
        struct nitrox_cmdq *pkt_cmdqs;
        struct nitrox_msix msix;
        struct nitrox_bh bh;
        struct nitrox_hw hw;
    #if IS_ENABLED(CONFIG_DEBUG_FS)
        struct dentry *debugfs_dir;
    #endif
    }

.. _`nitrox_device.members`:

Members
-------

list
    pointer to linked list of devices

bar_addr
    iomap address

pdev
    PCI device information

status
    NITROX status

timeout
    Request timeout in jiffies

refcnt
    Device usage count

idx
    device index (0..N)

node
    NUMA node id attached

qlen
    Command queue length

nr_queues
    Number of command queues

ctx_pool
    DMA pool for crypto context

pkt_cmdqs
    SE Command queues

msix
    MSI-X information

bh
    post processing work

hw
    hardware information

debugfs_dir
    debugfs directory

.. _`nitrox_read_csr`:

nitrox_read_csr
===============

.. c:function:: u64 nitrox_read_csr(struct nitrox_device *ndev, u64 offset)

    Read from device register

    :param struct nitrox_device \*ndev:
        NITROX device

    :param u64 offset:
        offset of the register to read

.. _`nitrox_read_csr.return`:

Return
------

value read

.. _`nitrox_write_csr`:

nitrox_write_csr
================

.. c:function:: void nitrox_write_csr(struct nitrox_device *ndev, u64 offset, u64 value)

    Write to device register

    :param struct nitrox_device \*ndev:
        NITROX device

    :param u64 offset:
        offset of the register to write

    :param u64 value:
        value to write

.. This file was automatic generated / don't edit.

