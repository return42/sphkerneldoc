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
        struct vmem_altmap *altmap;
        const struct resource *res;
        struct percpu_ref *ref;
        struct device *dev;
    }

.. _`dev_pagemap.members`:

Members
-------

altmap
    pre-allocated/reserved memory for vmemmap allocations

res
    physical address range covered by \ ``ref``\ 

ref
    reference count that pins the \ :c:func:`devm_memremap_pages`\  mapping

dev
    host device of the mapping for debug

.. _`get_dev_pagemap`:

get_dev_pagemap
===============

.. c:function:: struct dev_pagemap *get_dev_pagemap(unsigned long pfn, struct dev_pagemap *pgmap)

    take a new live reference on the dev_pagemap for \ ``pfn``\ 

    :param unsigned long pfn:
        page frame number to lookup page_map

    :param struct dev_pagemap \*pgmap:
        optional known pgmap that already has a reference

.. _`get_dev_pagemap.description`:

Description
-----------

@pgmap allows the overhead of a lookup to be bypassed when \ ``pfn``\  lands in the
same mapping.

.. This file was automatic generated / don't edit.

