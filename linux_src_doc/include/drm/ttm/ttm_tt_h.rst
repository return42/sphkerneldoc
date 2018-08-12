.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/ttm/ttm_tt.h

.. _`ttm_tt`:

struct ttm_tt
=============

.. c:type:: struct ttm_tt


.. _`ttm_tt.definition`:

Definition
----------

.. code-block:: c

    struct ttm_tt {
        struct ttm_bo_device *bdev;
        struct ttm_backend_func *func;
        struct page **pages;
        uint32_t page_flags;
        unsigned long num_pages;
        struct sg_table *sg;
        struct file *swap_storage;
        enum ttm_caching_state caching_state;
        enum {
            tt_bound,
            tt_unbound,
            tt_unpopulated,
        } state;
    }

.. _`ttm_tt.members`:

Members
-------

bdev
    Pointer to the current struct ttm_bo_device.

func
    Pointer to a struct ttm_backend_func that describes
    the backend methods.
    pointer.

pages
    Array of pages backing the data.

page_flags
    *undescribed*

num_pages
    Number of pages in the page array.

sg
    *undescribed*

swap_storage
    Pointer to shmem struct file for swap storage.

caching_state
    The current caching state of the pages.

state
    The current binding state of the pages.

.. _`ttm_tt.description`:

Description
-----------

This is a structure holding the pages, caching- and aperture binding
status for a buffer object that isn't backed by fixed (VRAM / AGP)
memory.

.. _`ttm_dma_tt`:

struct ttm_dma_tt
=================

.. c:type:: struct ttm_dma_tt


.. _`ttm_dma_tt.definition`:

Definition
----------

.. code-block:: c

    struct ttm_dma_tt {
        struct ttm_tt ttm;
        dma_addr_t *dma_address;
        struct list_head pages_list;
    }

.. _`ttm_dma_tt.members`:

Members
-------

ttm
    Base ttm_tt struct.

dma_address
    The DMA (bus) addresses of the pages

pages_list
    used by some page allocation backend

.. _`ttm_dma_tt.description`:

Description
-----------

This is a structure holding the pages, caching- and aperture binding
status for a buffer object that isn't backed by fixed (VRAM / AGP)
memory.

.. _`ttm_tt_create`:

ttm_tt_create
=============

.. c:function:: int ttm_tt_create(struct ttm_buffer_object *bo, bool zero_alloc)

    :param struct ttm_buffer_object \*bo:
        pointer to a struct ttm_buffer_object

    :param bool zero_alloc:
        true if allocated pages needs to be zeroed

.. _`ttm_tt_create.description`:

Description
-----------

Make sure we have a TTM structure allocated for the given BO.
No pages are actually allocated.

.. _`ttm_tt_init`:

ttm_tt_init
===========

.. c:function:: int ttm_tt_init(struct ttm_tt *ttm, struct ttm_buffer_object *bo, uint32_t page_flags)

    :param struct ttm_tt \*ttm:
        The struct ttm_tt.

    :param struct ttm_buffer_object \*bo:
        The buffer object we create the ttm for.

    :param uint32_t page_flags:
        Page flags as identified by TTM_PAGE_FLAG_XX flags.

.. _`ttm_tt_init.description`:

Description
-----------

Create a struct ttm_tt to back data with system memory pages.
No pages are actually allocated.

.. _`ttm_tt_init.null`:

NULL
----

Out of memory.

.. _`ttm_tt_fini`:

ttm_tt_fini
===========

.. c:function:: void ttm_tt_fini(struct ttm_tt *ttm)

    :param struct ttm_tt \*ttm:
        the ttm_tt structure.

.. _`ttm_tt_fini.description`:

Description
-----------

Free memory of ttm_tt structure

.. _`ttm_tt_bind`:

ttm_tt_bind
===========

.. c:function:: int ttm_tt_bind(struct ttm_tt *ttm, struct ttm_mem_reg *bo_mem, struct ttm_operation_ctx *ctx)

    :param struct ttm_tt \*ttm:
        The struct ttm_tt containing backing pages.

    :param struct ttm_mem_reg \*bo_mem:
        The struct ttm_mem_reg identifying the binding location.

    :param struct ttm_operation_ctx \*ctx:
        *undescribed*

.. _`ttm_tt_bind.description`:

Description
-----------

Bind the pages of \ ``ttm``\  to an aperture location identified by \ ``bo_mem``\ 

.. _`ttm_tt_destroy`:

ttm_tt_destroy
==============

.. c:function:: void ttm_tt_destroy(struct ttm_tt *ttm)

    :param struct ttm_tt \*ttm:
        The struct ttm_tt.

.. _`ttm_tt_destroy.description`:

Description
-----------

Unbind, unpopulate and destroy common struct ttm_tt.

.. _`ttm_tt_unbind`:

ttm_tt_unbind
=============

.. c:function:: void ttm_tt_unbind(struct ttm_tt *ttm)

    :param struct ttm_tt \*ttm:
        The struct ttm_tt.

.. _`ttm_tt_unbind.description`:

Description
-----------

Unbind a struct ttm_tt.

.. _`ttm_tt_swapin`:

ttm_tt_swapin
=============

.. c:function:: int ttm_tt_swapin(struct ttm_tt *ttm)

    :param struct ttm_tt \*ttm:
        The struct ttm_tt.

.. _`ttm_tt_swapin.description`:

Description
-----------

Swap in a previously swap out ttm_tt.

.. _`ttm_tt_set_placement_caching`:

ttm_tt_set_placement_caching
============================

.. c:function:: int ttm_tt_set_placement_caching(struct ttm_tt *ttm, uint32_t placement)

    :param struct ttm_tt \*ttm:
        *undescribed*

    :param uint32_t placement:
        Flag indicating the desired caching policy.

.. _`ttm_tt_set_placement_caching.description`:

Description
-----------

\ ``ttm``\  A struct ttm_tt the backing pages of which will change caching policy.

This function will change caching policy of any default kernel mappings of
the pages backing \ ``ttm``\ . If changing from cached to uncached or
write-combined,
all CPU caches will first be flushed to make sure the data of the pages
hit RAM. This function may be very costly as it involves global TLB
and cache flushes and potential page splitting / combining.

.. _`ttm_tt_populate`:

ttm_tt_populate
===============

.. c:function:: int ttm_tt_populate(struct ttm_tt *ttm, struct ttm_operation_ctx *ctx)

    allocate pages for a ttm

    :param struct ttm_tt \*ttm:
        Pointer to the ttm_tt structure

    :param struct ttm_operation_ctx \*ctx:
        *undescribed*

.. _`ttm_tt_populate.description`:

Description
-----------

Calls the driver method to allocate pages for a ttm

.. _`ttm_tt_unpopulate`:

ttm_tt_unpopulate
=================

.. c:function:: void ttm_tt_unpopulate(struct ttm_tt *ttm)

    free pages from a ttm

    :param struct ttm_tt \*ttm:
        Pointer to the ttm_tt structure

.. _`ttm_tt_unpopulate.description`:

Description
-----------

Calls the driver method to free all pages from a ttm

.. _`ttm_agp_tt_create`:

ttm_agp_tt_create
=================

.. c:function:: struct ttm_tt *ttm_agp_tt_create(struct ttm_buffer_object *bo, struct agp_bridge_data *bridge, uint32_t page_flags)

    :param struct ttm_buffer_object \*bo:
        Buffer object we allocate the ttm for.

    :param struct agp_bridge_data \*bridge:
        The agp bridge this device is sitting on.

    :param uint32_t page_flags:
        Page flags as identified by TTM_PAGE_FLAG_XX flags.

.. _`ttm_agp_tt_create.description`:

Description
-----------


Create a TTM backend that uses the indicated AGP bridge as an aperture
for TT memory. This function uses the linux agpgart interface to
bind and unbind memory backing a ttm_tt.

.. This file was automatic generated / don't edit.

