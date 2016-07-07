.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/ioat/dma.h

.. _`ioatdma_device`:

struct ioatdma_device
=====================

.. c:type:: struct ioatdma_device

    internal representation of a IOAT device

.. _`ioatdma_device.definition`:

Definition
----------

.. code-block:: c

    struct ioatdma_device {
        struct pci_dev *pdev;
        void __iomem *reg_base;
        struct dma_pool *completion_pool;
        #define MAX_SED_POOLS 5
        struct dma_pool  *sed_hw_pool[MAX_SED_POOLS];
        struct dma_device dma_dev;
        u8 version;
        #define IOAT_MAX_CHANS 4
        struct msix_entry msix_entries[IOAT_MAX_CHANS];
        struct ioatdma_chan  *idx[IOAT_MAX_CHANS];
        struct dca_provider *dca;
        enum ioat_irq_mode irq_mode;
        u32 cap;
        u64 msixtba0;
        u64 msixdata0;
        u32 msixpba;
    }

.. _`ioatdma_device.members`:

Members
-------

pdev
    PCI-Express device

reg_base
    MMIO register space base address

completion_pool
    DMA buffers for completion ops

sed_hw_pool
    DMA super descriptor pools

dma_dev
    embedded struct dma_device

version
    version of ioatdma device

msix_entries
    irq handlers

idx
    per channel data

dca
    direct cache access context

irq_mode
    interrupt mode (INTX, MSI, MSIX)

cap
    read DMA capabilities register

msixtba0
    *undescribed*

msixdata0
    *undescribed*

msixpba
    *undescribed*

.. _`ioat_sed_ent`:

struct ioat_sed_ent
===================

.. c:type:: struct ioat_sed_ent

    wrapper around super extended hardware descriptor

.. _`ioat_sed_ent.definition`:

Definition
----------

.. code-block:: c

    struct ioat_sed_ent {
        struct ioat_sed_raw_descriptor *hw;
        dma_addr_t dma;
        struct ioat_ring_ent *parent;
        unsigned int hw_pool;
    }

.. _`ioat_sed_ent.members`:

Members
-------

hw
    hardware SED

dma
    dma address for the SED

parent
    point to the dma descriptor that's the parent

hw_pool
    descriptor pool index

.. _`ioat_ring_ent`:

struct ioat_ring_ent
====================

.. c:type:: struct ioat_ring_ent

    wrapper around hardware descriptor

.. _`ioat_ring_ent.definition`:

Definition
----------

.. code-block:: c

    struct ioat_ring_ent {
        union {unnamed_union};
        size_t len;
        struct dma_async_tx_descriptor txd;
        enum sum_check_flags *result;
        #ifdef DEBUG
        int id;
        #endif
        struct ioat_sed_ent *sed;
    }

.. _`ioat_ring_ent.members`:

Members
-------

{unnamed_union}
    anonymous


len
    total transaction length for unmap

txd
    the generic software descriptor for all engines

result
    asynchronous result of validate operations

id
    identifier for debug

sed
    pointer to super extended descriptor sw desc

.. This file was automatic generated / don't edit.

