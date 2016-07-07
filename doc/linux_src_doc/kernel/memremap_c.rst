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
        any of MEMREMAP_WB, MEMREMAP_WT and MEMREMAP_WC

.. _`memremap.description`:

Description
-----------

\ :c:func:`memremap`\  is "ioremap" for cases where it is known that the resource
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

.. c:function:: void *devm_memremap_pages(struct device *dev, struct resource *res, struct percpu_ref *ref, struct vmem_altmap *altmap)

    remap and provide memmap backing for the given resource

    :param struct device \*dev:
        hosting device for \ ``res``\ 

    :param struct resource \*res:
        "host memory" address range

    :param struct percpu_ref \*ref:
        a live per-cpu reference count

    :param struct vmem_altmap \*altmap:
        optional descriptor for allocating the memmap from \ ``res``\ 

.. _`devm_memremap_pages.notes`:

Notes
-----

1/ \ ``ref``\  must be 'live' on entry and 'dead' before \ :c:func:`devm_memunmap_pages`\  time
(or devm release event).

2/ \ ``res``\  is expected to be a host memory range that could feasibly be
treated as a "System RAM" range, i.e. not a device mmio range, but
this is not enforced.

.. This file was automatic generated / don't edit.

