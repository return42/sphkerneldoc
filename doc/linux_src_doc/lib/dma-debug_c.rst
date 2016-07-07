.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/dma-debug.c

.. _`dma_debug_entry`:

struct dma_debug_entry
======================

.. c:type:: struct dma_debug_entry

    track a dma_map\* or dma_alloc_coherent mapping

.. _`dma_debug_entry.definition`:

Definition
----------

.. code-block:: c

    struct dma_debug_entry {
        struct list_head list;
        struct device *dev;
        int type;
        unsigned long pfn;
        size_t offset;
        u64 dev_addr;
        u64 size;
        int direction;
        int sg_call_ents;
        int sg_mapped_ents;
        enum map_err_types map_err_type;
        #ifdef CONFIG_STACKTRACE
        struct stack_trace stacktrace;
        unsigned long st_entries[DMA_DEBUG_STACKTRACE_ENTRIES];
        #endif
    }

.. _`dma_debug_entry.members`:

Members
-------

list
    node on pre-allocated free_entries list

dev
    'dev' argument to dma_map_{page\|single\|sg} or dma_alloc_coherent

type
    single, page, sg, coherent

pfn
    page frame of the start address

offset
    offset of mapping relative to pfn

dev_addr
    *undescribed*

size
    length of the mapping

direction
    enum dma_data_direction

sg_call_ents
    'nents' from dma_map_sg

sg_mapped_ents
    'mapped_ents' from dma_map_sg

map_err_type
    track whether \ :c:func:`dma_mapping_error`\  was checked

stacktrace
    support backtraces when a violation is detected

.. _`debug_dma_assert_idle`:

debug_dma_assert_idle
=====================

.. c:function:: void debug_dma_assert_idle(struct page *page)

    assert that a page is not undergoing dma

    :param struct page \*page:
        page to lookup in the dma_active_cacheline tree

.. _`debug_dma_assert_idle.description`:

Description
-----------

Place a call to this routine in cases where the cpu touching the page
before the dma completes (page is dma_unmapped) will lead to data
corruption.

.. This file was automatic generated / don't edit.

