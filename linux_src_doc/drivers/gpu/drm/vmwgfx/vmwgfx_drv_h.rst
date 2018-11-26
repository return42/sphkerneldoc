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

.. _`vmw_resource`:

struct vmw_resource
===================

.. c:type:: struct vmw_resource

    resource - base class for hardware resources

.. _`vmw_resource.definition`:

Definition
----------

.. code-block:: c

    struct vmw_resource {
        struct kref kref;
        struct vmw_private *dev_priv;
        int id;
        unsigned long backup_size;
        bool res_dirty;
        bool backup_dirty;
        struct vmw_buffer_object *backup;
        unsigned long backup_offset;
        unsigned long pin_count;
        const struct vmw_res_func *func;
        struct list_head lru_head;
        struct list_head mob_head;
        struct list_head binding_head;
        void (*res_free) (struct vmw_resource *res);
        void (*hw_destroy) (struct vmw_resource *res);
    }

.. _`vmw_resource.members`:

Members
-------

kref
    For refcounting.

dev_priv
    Pointer to the device private for this resource. Immutable.

id
    Device id. Protected by \ ``dev_priv``\ ::resource_lock.

backup_size
    Backup buffer size. Immutable.

res_dirty
    Resource contains data not yet in the backup buffer. Protected
    by resource reserved.

backup_dirty
    Backup buffer contains data not yet in the HW resource.
    Protecte by resource reserved.

backup
    The backup buffer if any. Protected by resource reserved.

backup_offset
    Offset into the backup buffer if any. Protected by resource
    reserved. Note that only a few resource types can have a \ ``backup_offset``\ 
    different from zero.

pin_count
    The pin count for this resource. A pinned resource has a
    pin-count greater than zero. It is not on the resource LRU lists and its
    backup buffer is pinned. Hence it can't be evicted.

func
    Method vtable for this resource. Immutable.

lru_head
    List head for the LRU list. Protected by \ ``dev_priv``\ ::resource_lock.

mob_head
    List head for the MOB backup list. Protected by \ ``backup``\  reserved.

binding_head
    List head for the context binding list. Protected by
    the \ ``dev_priv``\ ::binding_mutex

res_free
    The resource destructor.

hw_destroy
    Callback to destroy the resource on the device, as part of
    resource destruction.

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
        uint32_t handle;
        struct vmw_resource *res;
        void *private;
        unsigned short valid_handle;
        unsigned short valid;
    }

.. _`vmw_res_cache_entry.members`:

Members
-------

handle
    User-space handle of a resource.

res
    Non-ref-counted pointer to the resource.

private
    *undescribed*

valid_handle
    Whether the \ ``handle``\  member is valid.

valid
    Whether the entry is valid, which also implies that the execbuf
    code holds a reference to the resource, and it's placed on the
    validation list.

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

.. _`vmw_sw_context`:

struct vmw_sw_context
=====================

.. c:type:: struct vmw_sw_context

    Command submission context

.. _`vmw_sw_context.definition`:

Definition
----------

.. code-block:: c

    struct vmw_sw_context {
        struct drm_open_hash res_ht;
        bool res_ht_initialized;
        bool kernel;
        struct vmw_fpriv *fp;
        uint32_t *cmd_bounce;
        uint32_t cmd_bounce_size;
        struct vmw_buffer_object *cur_query_bo;
        struct list_head bo_relocations;
        struct list_head res_relocations;
        uint32_t *buf_start;
        struct vmw_res_cache_entry res_cache[vmw_res_max];
        struct vmw_resource *last_query_ctx;
        bool needs_post_query_barrier;
        struct vmw_ctx_binding_state *staged_bindings;
        bool staged_bindings_inuse;
        struct list_head staged_cmd_res;
        struct list_head ctx_list;
        struct vmw_ctx_validation_info *dx_ctx_node;
        struct vmw_buffer_object *dx_query_mob;
        struct vmw_resource *dx_query_ctx;
        struct vmw_cmdbuf_res_manager *man;
        struct vmw_validation_context *ctx;
    }

.. _`vmw_sw_context.members`:

Members
-------

res_ht
    Pointer hash table used to find validation duplicates

res_ht_initialized
    *undescribed*

kernel
    Whether the command buffer originates from kernel code rather
    than from user-space

fp
    If \ ``kernel``\  is false, points to the file of the client. Otherwise
    NULL

cmd_bounce
    Command bounce buffer used for command validation before
    copying to fifo space

cmd_bounce_size
    Current command bounce buffer size

cur_query_bo
    Current buffer object used as query result buffer

bo_relocations
    List of buffer object relocations

res_relocations
    List of resource relocations

buf_start
    Pointer to start of memory where command validation takes
    place

res_cache
    Cache of recently looked up resources

last_query_ctx
    Last context that submitted a query

needs_post_query_barrier
    Whether a query barrier is needed after
    command submission

staged_bindings
    Cached per-context binding tracker

staged_bindings_inuse
    Whether the cached per-context binding tracker
    is in use

staged_cmd_res
    List of staged command buffer managed resources in this
    command buffer

ctx_list
    List of context resources referenced in this command buffer

dx_ctx_node
    Validation metadata of the current DX context

dx_query_mob
    The MOB used for DX queries

dx_query_ctx
    The DX context used for the last DX query

man
    Pointer to the command buffer managed resource manager

ctx
    The validation context

.. _`vmw_gmr_bind`:

vmw_gmr_bind
============

.. c:function:: int vmw_gmr_bind(struct vmw_private *dev_priv, const struct vmw_sg_table *vsgt, unsigned long num_pages, int gmr_id)

    vmwgfx_gmr.c

    :param dev_priv:
        *undescribed*
    :type dev_priv: struct vmw_private \*

    :param vsgt:
        *undescribed*
    :type vsgt: const struct vmw_sg_table \*

    :param num_pages:
        *undescribed*
    :type num_pages: unsigned long

    :param gmr_id:
        *undescribed*
    :type gmr_id: int

.. _`vmw_user_resource_noref_release`:

vmw_user_resource_noref_release
===============================

.. c:function:: void vmw_user_resource_noref_release( void)

    release a user resource pointer looked up without reference

    :param void:
        no arguments
    :type void: 

.. _`vmw_bo_pin_in_placement`:

vmw_bo_pin_in_placement
=======================

.. c:function:: int vmw_bo_pin_in_placement(struct vmw_private *vmw_priv, struct vmw_buffer_object *bo, struct ttm_placement *placement, bool interruptible)

    vmwgfx_bo.c

    :param vmw_priv:
        *undescribed*
    :type vmw_priv: struct vmw_private \*

    :param bo:
        *undescribed*
    :type bo: struct vmw_buffer_object \*

    :param placement:
        *undescribed*
    :type placement: struct ttm_placement \*

    :param interruptible:
        *undescribed*
    :type interruptible: bool

.. _`vmw_user_bo_noref_release`:

vmw_user_bo_noref_release
=========================

.. c:function:: void vmw_user_bo_noref_release( void)

    release a buffer object pointer looked up without reference

    :param void:
        no arguments
    :type void: 

.. _`vmw_getparam_ioctl`:

vmw_getparam_ioctl
==================

.. c:function:: int vmw_getparam_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    vmwgfx_ioctl.c

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

    :param data:
        *undescribed*
    :type data: void \*

    :param file_priv:
        *undescribed*
    :type file_priv: struct drm_file \*

.. _`vmw_fifo_init`:

vmw_fifo_init
=============

.. c:function:: int vmw_fifo_init(struct vmw_private *dev_priv, struct vmw_fifo_state *fifo)

    vmwgfx_fifo.c

    :param dev_priv:
        *undescribed*
    :type dev_priv: struct vmw_private \*

    :param fifo:
        *undescribed*
    :type fifo: struct vmw_fifo_state \*

.. _`vmw_ttm_global_init`:

vmw_ttm_global_init
===================

.. c:function:: int vmw_ttm_global_init(struct vmw_private *dev_priv)

    vmwgfx_ttm_glue.c

    :param dev_priv:
        *undescribed*
    :type dev_priv: struct vmw_private \*

.. _`vmw_piter_next`:

vmw_piter_next
==============

.. c:function:: bool vmw_piter_next(struct vmw_piter *viter)

    Advance the iterator one page.

    :param viter:
        Pointer to the iterator to advance.
    :type viter: struct vmw_piter \*

.. _`vmw_piter_next.description`:

Description
-----------

Returns false if past the list of pages, true otherwise.

.. _`vmw_piter_dma_addr`:

vmw_piter_dma_addr
==================

.. c:function:: dma_addr_t vmw_piter_dma_addr(struct vmw_piter *viter)

    Return the DMA address of the current page.

    :param viter:
        Pointer to the iterator
    :type viter: struct vmw_piter \*

.. _`vmw_piter_dma_addr.description`:

Description
-----------

Returns the DMA address of the page pointed to by \ ``viter``\ .

.. _`vmw_piter_page`:

vmw_piter_page
==============

.. c:function:: struct page *vmw_piter_page(struct vmw_piter *viter)

    Return a pointer to the current page.

    :param viter:
        Pointer to the iterator
    :type viter: struct vmw_piter \*

.. _`vmw_piter_page.description`:

Description
-----------

Returns the DMA address of the page pointed to by \ ``viter``\ .

.. _`vmw_execbuf_ioctl`:

vmw_execbuf_ioctl
=================

.. c:function:: int vmw_execbuf_ioctl(struct drm_device *dev, unsigned long data, struct drm_file *file_priv, size_t size)

    vmwgfx_execbuf.c

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

    :param data:
        *undescribed*
    :type data: unsigned long

    :param file_priv:
        *undescribed*
    :type file_priv: struct drm_file \*

    :param size:
        *undescribed*
    :type size: size_t

.. _`vmw_wait_seqno`:

vmw_wait_seqno
==============

.. c:function:: int vmw_wait_seqno(struct vmw_private *dev_priv, bool lazy, uint32_t seqno, bool interruptible, unsigned long timeout)

    vmwgfx_irq.c

    :param dev_priv:
        *undescribed*
    :type dev_priv: struct vmw_private \*

    :param lazy:
        *undescribed*
    :type lazy: bool

    :param seqno:
        *undescribed*
    :type seqno: uint32_t

    :param interruptible:
        *undescribed*
    :type interruptible: bool

    :param timeout:
        *undescribed*
    :type timeout: unsigned long

.. _`vmw_marker_queue_init`:

vmw_marker_queue_init
=====================

.. c:function:: void vmw_marker_queue_init(struct vmw_marker_queue *queue)

    like objects currently used only for throttling - vmwgfx_marker.c

    :param queue:
        *undescribed*
    :type queue: struct vmw_marker_queue \*

.. _`vmw_fb_init`:

vmw_fb_init
===========

.. c:function:: int vmw_fb_init(struct vmw_private *vmw_priv)

    vmwgfx_fb.c

    :param vmw_priv:
        *undescribed*
    :type vmw_priv: struct vmw_private \*

.. _`vmw_kms_init`:

vmw_kms_init
============

.. c:function:: int vmw_kms_init(struct vmw_private *dev_priv)

    vmwgfx_kms.c

    :param dev_priv:
        *undescribed*
    :type dev_priv: struct vmw_private \*

.. _`vmw_overlay_init`:

vmw_overlay_init
================

.. c:function:: int vmw_overlay_init(struct vmw_private *dev_priv)

    vmwgfx_overlay.c

    :param dev_priv:
        *undescribed*
    :type dev_priv: struct vmw_private \*

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

    :param srf:
        *undescribed*
    :type srf: struct vmw_surface \*\*

.. _`vmw_mmio_read`:

vmw_mmio_read
=============

.. c:function:: u32 vmw_mmio_read(u32 *addr)

    Perform a MMIO read from volatile memory

    :param addr:
        The address to read from
    :type addr: u32 \*

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

    :param value:
        *undescribed*
    :type value: u32

    :param addr:
        The address to write to
    :type addr: u32 \*

.. _`vmw_mmio_write.description`:

Description
-----------

This function is intended to be equivalent to iowrite32 on
memremap'd memory, but without byteswapping.

.. This file was automatic generated / don't edit.

