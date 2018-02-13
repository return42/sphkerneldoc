.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/memremap.c

.. _`memremap`:

memremap
========

.. c:function:: void *memremap(resource_size_t offset, size_t size, unsigned long flags)

    remap an iomem_resource as cacheable memory

    :param resource_size_t offset:
        iomem resource start address

    :param size_t size:
        size of remap

    :param unsigned long flags:
        any of MEMREMAP_WB, MEMREMAP_WT, MEMREMAP_WC,
        MEMREMAP_ENC, MEMREMAP_DEC

.. _`memremap.description`:

Description
-----------

memremap() is "ioremap" for cases where it is known that the resource
being mapped does not have i/o side effects and the \__iomem
annotation is not applicable. In the case of multiple flags, the different
mapping types will be attempted in the order listed below until one of
them succeeds.

MEMREMAP_WB - matches the default mapping for System RAM on
the architecture.  This is usually a read-allocate write-back cache.
Morever, if MEMREMAP_WB is specified and the requested remap region is RAM
\ :c:func:`memremap`\  will bypass establishing a new mapping and instead return
a pointer into the direct map.

MEMREMAP_WT - establish a mapping whereby writes either bypass the
cache or are written through to memory and never exist in a
cache-dirty state with respect to program visibility.  Attempts to
map System RAM with this mapping type will fail.

MEMREMAP_WC - establish a writecombine mapping, whereby writes may
be coalesced together (e.g. in the CPU's write buffers), but is otherwise
uncached. Attempts to map System RAM with this mapping type will fail.

.. _`devm_memremap_pages`:

devm_memremap_pages
===================

.. c:function:: void *devm_memremap_pages(struct device *dev, struct dev_pagemap *pgmap)

    remap and provide memmap backing for the given resource

    :param struct device \*dev:
        hosting device for \ ``res``\ 

    :param struct dev_pagemap \*pgmap:
        pointer to a struct dev_pgmap

.. _`devm_memremap_pages.notes`:

Notes
-----

1/ At a minimum the res, ref and type members of \ ``pgmap``\  must be initialized
by the caller before passing it to this function

2/ The altmap field may optionally be initialized, in which case altmap_valid
must be set to true

3/ pgmap.ref must be 'live' on entry and 'dead' before \ :c:func:`devm_memunmap_pages`\ 
time (or devm release event). The expected order of events is that ref has
been through \ :c:func:`percpu_ref_kill`\  before \ :c:func:`devm_memremap_pages_release`\ . The
wait for the completion of all references being dropped and
\ :c:func:`percpu_ref_exit`\  must occur after \ :c:func:`devm_memremap_pages_release`\ .

4/ res is expected to be a host memory range that could feasibly be
treated as a "System RAM" range, i.e. not a device mmio range, but
this is not enforced.

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

If \ ``pgmap``\  is non-NULL and covers \ ``pfn``\  it will be returned as-is.  If \ ``pgmap``\ 
is non-NULL but does not cover \ ``pfn``\  the reference to it will be released.

.. This file was automatic generated / don't edit.

