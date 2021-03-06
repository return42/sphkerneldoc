.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/percpu-vm.c

.. _`pcpu_get_pages`:

pcpu_get_pages
==============

.. c:function:: struct page **pcpu_get_pages( void)

    get temp pages array

    :param void:
        no arguments
    :type void: 

.. _`pcpu_get_pages.description`:

Description
-----------

Returns pointer to array of pointers to struct page which can be indexed
with \ :c:func:`pcpu_page_idx`\ .  Note that there is only one array and accesses
should be serialized by pcpu_alloc_mutex.

.. _`pcpu_get_pages.return`:

Return
------

Pointer to temp pages array on success.

.. _`pcpu_free_pages`:

pcpu_free_pages
===============

.. c:function:: void pcpu_free_pages(struct pcpu_chunk *chunk, struct page **pages, int page_start, int page_end)

    free pages which were allocated for \ ``chunk``\ 

    :param chunk:
        chunk pages were allocated for
    :type chunk: struct pcpu_chunk \*

    :param pages:
        array of pages to be freed, indexed by \ :c:func:`pcpu_page_idx`\ 
    :type pages: struct page \*\*

    :param page_start:
        page index of the first page to be freed
    :type page_start: int

    :param page_end:
        page index of the last page to be freed + 1
    :type page_end: int

.. _`pcpu_free_pages.description`:

Description
-----------

Free pages [@page_start and \ ``page_end``\ ) in \ ``pages``\  for all units.
The pages were allocated for \ ``chunk``\ .

.. _`pcpu_alloc_pages`:

pcpu_alloc_pages
================

.. c:function:: int pcpu_alloc_pages(struct pcpu_chunk *chunk, struct page **pages, int page_start, int page_end, gfp_t gfp)

    allocates pages for \ ``chunk``\ 

    :param chunk:
        target chunk
    :type chunk: struct pcpu_chunk \*

    :param pages:
        array to put the allocated pages into, indexed by \ :c:func:`pcpu_page_idx`\ 
    :type pages: struct page \*\*

    :param page_start:
        page index of the first page to be allocated
    :type page_start: int

    :param page_end:
        page index of the last page to be allocated + 1
    :type page_end: int

    :param gfp:
        allocation flags passed to the underlying allocator
    :type gfp: gfp_t

.. _`pcpu_alloc_pages.description`:

Description
-----------

Allocate pages [@page_start,@page_end) into \ ``pages``\  for all units.
The allocation is for \ ``chunk``\ .  Percpu core doesn't care about the
content of \ ``pages``\  and will pass it verbatim to \ :c:func:`pcpu_map_pages`\ .

.. _`pcpu_pre_unmap_flush`:

pcpu_pre_unmap_flush
====================

.. c:function:: void pcpu_pre_unmap_flush(struct pcpu_chunk *chunk, int page_start, int page_end)

    flush cache prior to unmapping

    :param chunk:
        chunk the regions to be flushed belongs to
    :type chunk: struct pcpu_chunk \*

    :param page_start:
        page index of the first page to be flushed
    :type page_start: int

    :param page_end:
        page index of the last page to be flushed + 1
    :type page_end: int

.. _`pcpu_pre_unmap_flush.description`:

Description
-----------

Pages in [@page_start,@page_end) of \ ``chunk``\  are about to be
unmapped.  Flush cache.  As each flushing trial can be very
expensive, issue flush on the whole region at once rather than
doing it for each cpu.  This could be an overkill but is more
scalable.

.. _`pcpu_unmap_pages`:

pcpu_unmap_pages
================

.. c:function:: void pcpu_unmap_pages(struct pcpu_chunk *chunk, struct page **pages, int page_start, int page_end)

    unmap pages out of a pcpu_chunk

    :param chunk:
        chunk of interest
    :type chunk: struct pcpu_chunk \*

    :param pages:
        pages array which can be used to pass information to free
    :type pages: struct page \*\*

    :param page_start:
        page index of the first page to unmap
    :type page_start: int

    :param page_end:
        page index of the last page to unmap + 1
    :type page_end: int

.. _`pcpu_unmap_pages.description`:

Description
-----------

For each cpu, unmap pages [@page_start,@page_end) out of \ ``chunk``\ .
Corresponding elements in \ ``pages``\  were cleared by the caller and can
be used to carry information to \ :c:func:`pcpu_free_pages`\  which will be
called after all unmaps are finished.  The caller should call
proper pre/post flush functions.

.. _`pcpu_post_unmap_tlb_flush`:

pcpu_post_unmap_tlb_flush
=========================

.. c:function:: void pcpu_post_unmap_tlb_flush(struct pcpu_chunk *chunk, int page_start, int page_end)

    flush TLB after unmapping

    :param chunk:
        pcpu_chunk the regions to be flushed belong to
    :type chunk: struct pcpu_chunk \*

    :param page_start:
        page index of the first page to be flushed
    :type page_start: int

    :param page_end:
        page index of the last page to be flushed + 1
    :type page_end: int

.. _`pcpu_post_unmap_tlb_flush.description`:

Description
-----------

Pages [@page_start,@page_end) of \ ``chunk``\  have been unmapped.  Flush
TLB for the regions.  This can be skipped if the area is to be
returned to vmalloc as vmalloc will handle TLB flushing lazily.

As with \ :c:func:`pcpu_pre_unmap_flush`\ , TLB flushing also is done at once
for the whole region.

.. _`pcpu_map_pages`:

pcpu_map_pages
==============

.. c:function:: int pcpu_map_pages(struct pcpu_chunk *chunk, struct page **pages, int page_start, int page_end)

    map pages into a pcpu_chunk

    :param chunk:
        chunk of interest
    :type chunk: struct pcpu_chunk \*

    :param pages:
        pages array containing pages to be mapped
    :type pages: struct page \*\*

    :param page_start:
        page index of the first page to map
    :type page_start: int

    :param page_end:
        page index of the last page to map + 1
    :type page_end: int

.. _`pcpu_map_pages.description`:

Description
-----------

For each cpu, map pages [@page_start,@page_end) into \ ``chunk``\ .  The
caller is responsible for calling \ :c:func:`pcpu_post_map_flush`\  after all
mappings are complete.

This function is responsible for setting up whatever is necessary for
reverse lookup (addr -> chunk).

.. _`pcpu_post_map_flush`:

pcpu_post_map_flush
===================

.. c:function:: void pcpu_post_map_flush(struct pcpu_chunk *chunk, int page_start, int page_end)

    flush cache after mapping

    :param chunk:
        pcpu_chunk the regions to be flushed belong to
    :type chunk: struct pcpu_chunk \*

    :param page_start:
        page index of the first page to be flushed
    :type page_start: int

    :param page_end:
        page index of the last page to be flushed + 1
    :type page_end: int

.. _`pcpu_post_map_flush.description`:

Description
-----------

Pages [@page_start,@page_end) of \ ``chunk``\  have been mapped.  Flush
cache.

As with \ :c:func:`pcpu_pre_unmap_flush`\ , TLB flushing also is done at once
for the whole region.

.. _`pcpu_populate_chunk`:

pcpu_populate_chunk
===================

.. c:function:: int pcpu_populate_chunk(struct pcpu_chunk *chunk, int page_start, int page_end, gfp_t gfp)

    populate and map an area of a pcpu_chunk

    :param chunk:
        chunk of interest
    :type chunk: struct pcpu_chunk \*

    :param page_start:
        the start page
    :type page_start: int

    :param page_end:
        the end page
    :type page_end: int

    :param gfp:
        allocation flags passed to the underlying memory allocator
    :type gfp: gfp_t

.. _`pcpu_populate_chunk.description`:

Description
-----------

For each cpu, populate and map pages [@page_start,@page_end) into
\ ``chunk``\ .

.. _`pcpu_populate_chunk.context`:

Context
-------

pcpu_alloc_mutex, does GFP_KERNEL allocation.

.. _`pcpu_depopulate_chunk`:

pcpu_depopulate_chunk
=====================

.. c:function:: void pcpu_depopulate_chunk(struct pcpu_chunk *chunk, int page_start, int page_end)

    depopulate and unmap an area of a pcpu_chunk

    :param chunk:
        chunk to depopulate
    :type chunk: struct pcpu_chunk \*

    :param page_start:
        the start page
    :type page_start: int

    :param page_end:
        the end page
    :type page_end: int

.. _`pcpu_depopulate_chunk.description`:

Description
-----------

For each cpu, depopulate and unmap pages [@page_start,@page_end)
from \ ``chunk``\ .

.. _`pcpu_depopulate_chunk.context`:

Context
-------

pcpu_alloc_mutex.

.. This file was automatic generated / don't edit.

