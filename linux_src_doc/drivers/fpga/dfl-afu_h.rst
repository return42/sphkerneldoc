.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/fpga/dfl-afu.h

.. _`dfl_afu_mmio_region`:

struct dfl_afu_mmio_region
==========================

.. c:type:: struct dfl_afu_mmio_region

    afu mmio region data structure

.. _`dfl_afu_mmio_region.definition`:

Definition
----------

.. code-block:: c

    struct dfl_afu_mmio_region {
        u32 index;
        u32 flags;
        u64 size;
        u64 offset;
        u64 phys;
        struct list_head node;
    }

.. _`dfl_afu_mmio_region.members`:

Members
-------

index
    region index.

flags
    region flags (access permission).

size
    region size.

offset
    region offset from start of the device fd.

phys
    region's physical address.

node
    node to add to afu feature dev's region list.

.. _`dfl_afu_dma_region`:

struct dfl_afu_dma_region
=========================

.. c:type:: struct dfl_afu_dma_region

    afu DMA region data structure

.. _`dfl_afu_dma_region.definition`:

Definition
----------

.. code-block:: c

    struct dfl_afu_dma_region {
        u64 user_addr;
        u64 length;
        u64 iova;
        struct page **pages;
        struct rb_node node;
        bool in_use;
    }

.. _`dfl_afu_dma_region.members`:

Members
-------

user_addr
    region userspace virtual address.

length
    region length.

iova
    region IO virtual address.

pages
    ptr to pages of this region.

node
    rb tree node.

in_use
    flag to indicate if this region is in_use.

.. _`dfl_afu`:

struct dfl_afu
==============

.. c:type:: struct dfl_afu

    afu device data structure

.. _`dfl_afu.definition`:

Definition
----------

.. code-block:: c

    struct dfl_afu {
        u64 region_cur_offset;
        int num_regions;
        u8 num_umsgs;
        struct list_head regions;
        struct rb_root dma_regions;
        struct dfl_feature_platform_data *pdata;
    }

.. _`dfl_afu.members`:

Members
-------

region_cur_offset
    current region offset from start to the device fd.

num_regions
    num of mmio regions.

num_umsgs
    num of umsgs.

regions
    the mmio region linked list of this afu feature device.

dma_regions
    root of dma regions rb tree.

pdata
    afu platform device's pdata.

.. This file was automatic generated / don't edit.

