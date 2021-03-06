.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/memremap.h

.. _`vmem_altmap`:

struct vmem_altmap
==================

.. c:type:: struct vmem_altmap

    pre-allocated storage for vmemmap_populate

.. _`vmem_altmap.definition`:

Definition
----------

.. code-block:: c

    struct vmem_altmap {
        const unsigned long base_pfn;
        const unsigned long reserve;
        unsigned long free;
        unsigned long align;
        unsigned long alloc;
    }

.. _`vmem_altmap.members`:

Members
-------

base_pfn
    base of the entire dev_pagemap mapping

reserve
    pages mapped, but reserved for driver use (relative to \ ``base``\ )

free
    free pages set aside in the mapping for memmap storage

align
    pages reserved to meet allocation alignments

alloc
    track pages consumed, private to \ :c:func:`vmemmap_populate`\ 

.. _`dev_pagemap`:

struct dev_pagemap
==================

.. c:type:: struct dev_pagemap

    metadata for ZONE_DEVICE mappings

.. _`dev_pagemap.definition`:

Definition
----------

.. code-block:: c

    struct dev_pagemap {
        dev_page_fault_t page_fault;
        dev_page_free_t page_free;
        struct vmem_altmap altmap;
        bool altmap_valid;
        struct resource res;
        struct percpu_ref *ref;
        struct device *dev;
        void *data;
        enum memory_type type;
        u64 pci_p2pdma_bus_offset;
    }

.. _`dev_pagemap.members`:

Members
-------

page_fault
    callback when CPU fault on an unaddressable device page

page_free
    free page callback when page refcount reaches 1

altmap
    pre-allocated/reserved memory for vmemmap allocations

altmap_valid
    *undescribed*

res
    physical address range covered by \ ``ref``\ 

ref
    reference count that pins the \ :c:func:`devm_memremap_pages`\  mapping

dev
    host device of the mapping for debug

data
    private data pointer for \ :c:func:`page_free`\ 

type
    memory type: see MEMORY\_\* in memory_hotplug.h

pci_p2pdma_bus_offset
    *undescribed*

.. This file was automatic generated / don't edit.

