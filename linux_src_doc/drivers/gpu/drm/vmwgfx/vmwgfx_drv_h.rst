.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vmwgfx/vmwgfx_drv.h

.. _`vmw_validate_buffer`:

struct vmw_validate_buffer
==========================

.. c:type:: struct vmw_validate_buffer

    Carries validation info about buffers.

.. _`vmw_validate_buffer.definition`:

Definition
----------

.. code-block:: c

    struct vmw_validate_buffer {
        struct ttm_validate_buffer base;
        struct drm_hash_item hash;
        bool validate_as_mob;
    }

.. _`vmw_validate_buffer.members`:

Members
-------

base
    Validation info for TTM.

hash
    Hash entry for quick lookup of the TTM buffer object.

validate_as_mob
    *undescribed*

.. _`vmw_validate_buffer.description`:

Description
-----------

This structure contains also driver private validation info
on top of the info needed by TTM.

.. _`vmw_res_cache_entry`:

struct vmw_res_cache_entry
==========================

.. c:type:: struct vmw_res_cache_entry

    resource information cache entry

.. _`vmw_res_cache_entry.definition`:

Definition
----------

.. code-block:: c

    struct vmw_res_cache_entry {
        bool valid;
        uint32_t handle;
        struct vmw_resource *res;
        struct vmw_resource_val_node *node;
    }

.. _`vmw_res_cache_entry.members`:

Members
-------

valid
    Whether the entry is valid, which also implies that the execbuf
    code holds a reference to the resource, and it's placed on the
    validation list.

handle
    User-space handle of a resource.

res
    Non-ref-counted pointer to the resource.

node
    *undescribed*

.. _`vmw_res_cache_entry.description`:

Description
-----------

Used to avoid frequent repeated user-space handle lookups of the
same resource.

.. _`vmw_dma_map_mode`:

enum vmw_dma_map_mode
=====================

.. c:type:: enum vmw_dma_map_mode

    indicate how to perform TTM page dma mappings.

.. _`vmw_dma_map_mode.definition`:

Definition
----------

.. code-block:: c

    enum vmw_dma_map_mode {
        vmw_dma_phys,
        vmw_dma_alloc_coherent,
        vmw_dma_map_populate,
        vmw_dma_map_bind,
        vmw_dma_map_max
    };

.. _`vmw_dma_map_mode.constants`:

Constants
---------

vmw_dma_phys
    *undescribed*

vmw_dma_alloc_coherent
    *undescribed*

vmw_dma_map_populate
    *undescribed*

vmw_dma_map_bind
    *undescribed*

vmw_dma_map_max
    *undescribed*

.. _`vmw_sg_table`:

struct vmw_sg_table
===================

.. c:type:: struct vmw_sg_table

    Scatter/gather table for binding, with additional device-specific information.

.. _`vmw_sg_table.definition`:

Definition
----------

.. code-block:: c

    struct vmw_sg_table {
        enum vmw_dma_map_mode mode;
        struct page **pages;
        const dma_addr_t *addrs;
        struct sg_table *sgt;
        unsigned long num_regions;
        unsigned long num_pages;
    }

.. _`vmw_sg_table.members`:

Members
-------

mode
    *undescribed*

pages
    *undescribed*

addrs
    *undescribed*

sgt
    Pointer to a struct sg_table with binding information

num_regions
    Number of regions with device-address contiguous pages

num_pages
    *undescribed*

.. _`vmw_piter`:

struct vmw_piter
================

.. c:type:: struct vmw_piter

    Page iterator that iterates over a list of pages and DMA addresses that could be either a scatter-gather list or arrays

.. _`vmw_piter.definition`:

Definition
----------

.. code-block:: c

    struct vmw_piter {
        struct page **pages;
        const dma_addr_t *addrs;
        struct sg_page_iter iter;
        unsigned long i;
        unsigned long num_pages;
        bool (*next)(struct vmw_piter *);
        dma_addr_t (*dma_address)(struct vmw_piter *);
        struct page *(*page)(struct vmw_piter *);
    }

.. _`vmw_piter.members`:

Members
-------

pages
    Array of page pointers to the pages.

addrs
    DMA addresses to the pages if coherent pages are used.

iter
    Scatter-gather page iterator. Current position in SG list.

i
    Current position in arrays.

num_pages
    Number of pages total.

next
    Function to advance the iterator. Returns false if past the list
    of pages, true otherwise.

dma_address
    Function to return the DMA address of the current page.

page
    *undescribed*

.. _`vmw_gmr_bind`:

vmw_gmr_bind
============

.. c:function:: int vmw_gmr_bind(struct vmw_private *dev_priv, const struct vmw_sg_table *vsgt, unsigned long num_pages, int gmr_id)

    vmwgfx_gmr.c

    :param struct vmw_private \*dev_priv:
        *undescribed*

    :param const struct vmw_sg_table \*vsgt:
        *undescribed*

    :param unsigned long num_pages:
        *undescribed*

    :param int gmr_id:
        *undescribed*

.. _`vmw_dmabuf_pin_in_placement`:

vmw_dmabuf_pin_in_placement
===========================

.. c:function:: int vmw_dmabuf_pin_in_placement(struct vmw_private *vmw_priv, struct vmw_dma_buffer *bo, struct ttm_placement *placement, bool interruptible)

    vmwgfx_dmabuf.c

    :param struct vmw_private \*vmw_priv:
        *undescribed*

    :param struct vmw_dma_buffer \*bo:
        *undescribed*

    :param struct ttm_placement \*placement:
        *undescribed*

    :param bool interruptible:
        *undescribed*

.. _`vmw_getparam_ioctl`:

vmw_getparam_ioctl
==================

.. c:function:: int vmw_getparam_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    vmwgfx_ioctl.c

    :param struct drm_device \*dev:
        *undescribed*

    :param void \*data:
        *undescribed*

    :param struct drm_file \*file_priv:
        *undescribed*

.. _`vmw_fifo_init`:

vmw_fifo_init
=============

.. c:function:: int vmw_fifo_init(struct vmw_private *dev_priv, struct vmw_fifo_state *fifo)

    vmwgfx_fifo.c

    :param struct vmw_private \*dev_priv:
        *undescribed*

    :param struct vmw_fifo_state \*fifo:
        *undescribed*

.. _`vmw_ttm_global_init`:

vmw_ttm_global_init
===================

.. c:function:: int vmw_ttm_global_init(struct vmw_private *dev_priv)

    vmwgfx_ttm_glue.c

    :param struct vmw_private \*dev_priv:
        *undescribed*

.. _`vmw_piter_next`:

vmw_piter_next
==============

.. c:function:: bool vmw_piter_next(struct vmw_piter *viter)

    Advance the iterator one page.

    :param struct vmw_piter \*viter:
        Pointer to the iterator to advance.

.. _`vmw_piter_next.description`:

Description
-----------

Returns false if past the list of pages, true otherwise.

.. _`vmw_piter_dma_addr`:

vmw_piter_dma_addr
==================

.. c:function:: dma_addr_t vmw_piter_dma_addr(struct vmw_piter *viter)

    Return the DMA address of the current page.

    :param struct vmw_piter \*viter:
        Pointer to the iterator

.. _`vmw_piter_dma_addr.description`:

Description
-----------

Returns the DMA address of the page pointed to by \ ``viter``\ .

.. _`vmw_piter_page`:

vmw_piter_page
==============

.. c:function:: struct page *vmw_piter_page(struct vmw_piter *viter)

    Return a pointer to the current page.

    :param struct vmw_piter \*viter:
        Pointer to the iterator

.. _`vmw_piter_page.description`:

Description
-----------

Returns the DMA address of the page pointed to by \ ``viter``\ .

.. _`vmw_execbuf_ioctl`:

vmw_execbuf_ioctl
=================

.. c:function:: int vmw_execbuf_ioctl(struct drm_device *dev, unsigned long data, struct drm_file *file_priv, size_t size)

    vmwgfx_execbuf.c

    :param struct drm_device \*dev:
        *undescribed*

    :param unsigned long data:
        *undescribed*

    :param struct drm_file \*file_priv:
        *undescribed*

    :param size_t size:
        *undescribed*

.. _`vmw_wait_seqno`:

vmw_wait_seqno
==============

.. c:function:: int vmw_wait_seqno(struct vmw_private *dev_priv, bool lazy, uint32_t seqno, bool interruptible, unsigned long timeout)

    vmwgfx_irq.c

    :param struct vmw_private \*dev_priv:
        *undescribed*

    :param bool lazy:
        *undescribed*

    :param uint32_t seqno:
        *undescribed*

    :param bool interruptible:
        *undescribed*

    :param unsigned long timeout:
        *undescribed*

.. _`vmw_marker_queue_init`:

vmw_marker_queue_init
=====================

.. c:function:: void vmw_marker_queue_init(struct vmw_marker_queue *queue)

    like objects currently used only for throttling - vmwgfx_marker.c

    :param struct vmw_marker_queue \*queue:
        *undescribed*

.. _`vmw_fb_init`:

vmw_fb_init
===========

.. c:function:: int vmw_fb_init(struct vmw_private *vmw_priv)

    vmwgfx_fb.c

    :param struct vmw_private \*vmw_priv:
        *undescribed*

.. _`vmw_kms_init`:

vmw_kms_init
============

.. c:function:: int vmw_kms_init(struct vmw_private *dev_priv)

    vmwgfx_kms.c

    :param struct vmw_private \*dev_priv:
        *undescribed*

.. _`vmw_overlay_init`:

vmw_overlay_init
================

.. c:function:: int vmw_overlay_init(struct vmw_private *dev_priv)

    vmwgfx_overlay.c

    :param struct vmw_private \*dev_priv:
        *undescribed*

.. _`vmw_diff_cpy`:

struct vmw_diff_cpy
===================

.. c:type:: struct vmw_diff_cpy

    CPU blit information structure

.. _`vmw_diff_cpy.definition`:

Definition
----------

.. code-block:: c

    struct vmw_diff_cpy {
        struct drm_rect rect;
        size_t line;
        size_t line_offset;
        int cpp;
        void (*do_cpy)(struct vmw_diff_cpy *diff, u8 *dest, const u8 *src, size_t n);
    }

.. _`vmw_diff_cpy.members`:

Members
-------

rect
    The output bounding box rectangle.

line
    The current line of the blit.

line_offset
    Offset of the current line segment.

cpp
    Bytes per pixel (granularity information).

do_cpy
    *undescribed*

.. _`vmw_surface_unreference`:

vmw_surface_unreference
=======================

.. c:function:: void vmw_surface_unreference(struct vmw_surface **srf)

    :param struct vmw_surface \*\*srf:
        *undescribed*

.. _`vmw_mmio_read`:

vmw_mmio_read
=============

.. c:function:: u32 vmw_mmio_read(u32 *addr)

    Perform a MMIO read from volatile memory

    :param u32 \*addr:
        The address to read from

.. _`vmw_mmio_read.description`:

Description
-----------

This function is intended to be equivalent to \ :c:func:`ioread32`\  on
memremap'd memory, but without byteswapping.

.. _`vmw_mmio_write`:

vmw_mmio_write
==============

.. c:function:: void vmw_mmio_write(u32 value, u32 *addr)

    Perform a MMIO write to volatile memory

    :param u32 value:
        *undescribed*

    :param u32 \*addr:
        The address to write to

.. _`vmw_mmio_write.description`:

Description
-----------

This function is intended to be equivalent to iowrite32 on
memremap'd memory, but without byteswapping.

.. _`vmw_host_log`:

vmw_host_log
============

.. c:function:: int vmw_host_log(const char *log)

    :param const char \*log:
        *undescribed*

.. This file was automatic generated / don't edit.

