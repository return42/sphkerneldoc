.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/iomem.c

.. _`memremap`:

memremap
========

.. c:function:: void *memremap(resource_size_t offset, size_t size, unsigned long flags)

    remap an iomem_resource as cacheable memory

    :param offset:
        iomem resource start address
    :type offset: resource_size_t

    :param size:
        size of remap
    :type size: size_t

    :param flags:
        any of MEMREMAP_WB, MEMREMAP_WT, MEMREMAP_WC,
        MEMREMAP_ENC, MEMREMAP_DEC
    :type flags: unsigned long

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

.. This file was automatic generated / don't edit.

