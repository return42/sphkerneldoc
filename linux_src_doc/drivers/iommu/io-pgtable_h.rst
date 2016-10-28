.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iommu/io-pgtable.h

.. _`iommu_gather_ops`:

struct iommu_gather_ops
=======================

.. c:type:: struct iommu_gather_ops

    IOMMU callbacks for TLB and page table management.

.. _`iommu_gather_ops.definition`:

Definition
----------

.. code-block:: c

    struct iommu_gather_ops {
        void (*tlb_flush_all)(void *cookie);
        void (*tlb_add_flush)(unsigned long iova, size_t size, size_t granule,bool leaf, void *cookie);
        void (*tlb_sync)(void *cookie);
    }

.. _`iommu_gather_ops.members`:

Members
-------

tlb_flush_all
    Synchronously invalidate the entire TLB context.

tlb_add_flush
    Queue up a TLB invalidation for a virtual address range.

tlb_sync
    Ensure any queued TLB invalidation has taken effect, and
    any corresponding page table updates are visible to the
    IOMMU.

.. _`iommu_gather_ops.description`:

Description
-----------

Note that these can all be called in atomic context and must therefore
not block.

.. _`io_pgtable_cfg`:

struct io_pgtable_cfg
=====================

.. c:type:: struct io_pgtable_cfg

    Configuration data for a set of page tables.

.. _`io_pgtable_cfg.definition`:

Definition
----------

.. code-block:: c

    struct io_pgtable_cfg {
    #define IO_PGTABLE_QUIRK_ARM_NS BIT(0)
    #define IO_PGTABLE_QUIRK_NO_PERMS BIT(1)
    #define IO_PGTABLE_QUIRK_TLBI_ON_MAP BIT(2)
    #define IO_PGTABLE_QUIRK_ARM_MTK_4GB BIT(3)
        unsigned long quirks;
        unsigned long pgsize_bitmap;
        unsigned int ias;
        unsigned int oas;
        const struct iommu_gather_ops *tlb;
        struct device *iommu_dev;
        union {unnamed_union};
    }

.. _`io_pgtable_cfg.members`:

Members
-------

quirks
    A bitmap of hardware quirks that require some special
    action by the low-level page table allocator.

pgsize_bitmap
    A bitmap of page sizes supported by this set of page
    tables.

ias
    Input address (iova) size, in bits.

oas
    Output address (paddr) size, in bits.

tlb
    TLB management callbacks for this set of tables.

iommu_dev
    The device representing the DMA configuration for the
    page table walker.

{unnamed_union}
    anonymous


.. _`io_pgtable_ops`:

struct io_pgtable_ops
=====================

.. c:type:: struct io_pgtable_ops

    Page table manipulation API for IOMMU drivers.

.. _`io_pgtable_ops.definition`:

Definition
----------

.. code-block:: c

    struct io_pgtable_ops {
        int (*map)(struct io_pgtable_ops *ops, unsigned long iova,phys_addr_t paddr, size_t size, int prot);
        int (*unmap)(struct io_pgtable_ops *ops, unsigned long iova,size_t size);
        phys_addr_t (*iova_to_phys)(struct io_pgtable_ops *ops,unsigned long iova);
    }

.. _`io_pgtable_ops.members`:

Members
-------

map
    Map a physically contiguous memory region.

unmap
    Unmap a physically contiguous memory region.

iova_to_phys
    Translate iova to physical address.

.. _`io_pgtable_ops.description`:

Description
-----------

These functions map directly onto the iommu_ops member functions with
the same names.

.. _`alloc_io_pgtable_ops`:

alloc_io_pgtable_ops
====================

.. c:function:: struct io_pgtable_ops *alloc_io_pgtable_ops(enum io_pgtable_fmt fmt, struct io_pgtable_cfg *cfg, void *cookie)

    Allocate a page table allocator for use by an IOMMU.

    :param enum io_pgtable_fmt fmt:
        The page table format.

    :param struct io_pgtable_cfg \*cfg:
        The page table configuration. This will be modified to represent
        the configuration actually provided by the allocator (e.g. the
        pgsize_bitmap may be restricted).

    :param void \*cookie:
        An opaque token provided by the IOMMU driver and passed back to
        the callback routines in cfg->tlb.

.. _`free_io_pgtable_ops`:

free_io_pgtable_ops
===================

.. c:function:: void free_io_pgtable_ops(struct io_pgtable_ops *ops)

    Free an io_pgtable_ops structure. The caller \*must\* ensure that the page table is no longer live, but the TLB can be dirty.

    :param struct io_pgtable_ops \*ops:
        The ops returned from alloc_io_pgtable_ops.

.. _`io_pgtable`:

struct io_pgtable
=================

.. c:type:: struct io_pgtable

    Internal structure describing a set of page tables.

.. _`io_pgtable.definition`:

Definition
----------

.. code-block:: c

    struct io_pgtable {
        enum io_pgtable_fmt fmt;
        void *cookie;
        bool tlb_sync_pending;
        struct io_pgtable_cfg cfg;
        struct io_pgtable_ops ops;
    }

.. _`io_pgtable.members`:

Members
-------

fmt
    The page table format.

cookie
    An opaque token provided by the IOMMU driver and passed back to
    any callback routines.

tlb_sync_pending
    Private flag for optimising out redundant syncs.

cfg
    A copy of the page table configuration.

ops
    The page table operations in use for this set of page tables.

.. _`io_pgtable_init_fns`:

struct io_pgtable_init_fns
==========================

.. c:type:: struct io_pgtable_init_fns

    Alloc/free a set of page tables for a particular format.

.. _`io_pgtable_init_fns.definition`:

Definition
----------

.. code-block:: c

    struct io_pgtable_init_fns {
        struct io_pgtable *(*alloc)(struct io_pgtable_cfg *cfg, void *cookie);
        void (*free)(struct io_pgtable *iop);
    }

.. _`io_pgtable_init_fns.members`:

Members
-------

alloc
    Allocate a set of page tables described by cfg.

free
    Free the page tables associated with iop.

.. This file was automatic generated / don't edit.

