.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/power/snapshot.c

.. _`free_image_page`:

free_image_page
===============

.. c:function:: void free_image_page(void *addr, int clear_nosave_free)

    free page represented by \ ``addr``\ , allocated with get_image_page (page flags set by it must be cleared)

    :param void \*addr:
        *undescribed*

    :param int clear_nosave_free:
        *undescribed*

.. _`chain_allocator`:

struct chain_allocator
======================

.. c:type:: struct chain_allocator

    a linked list of pages called 'the chain'.

.. _`chain_allocator.definition`:

Definition
----------

.. code-block:: c

    struct chain_allocator {
        struct linked_page *chain;
        unsigned int used_space;
        gfp_t gfp_mask;
        int safe_needed;
    }

.. _`chain_allocator.members`:

Members
-------

chain
    *undescribed*

used_space
    *undescribed*

gfp_mask
    *undescribed*

safe_needed
    *undescribed*

.. _`chain_allocator.description`:

Description
-----------

The chain grows each time when there is no room for a new object in
the current page.  The allocated objects cannot be freed individually.
It is only possible to free them all at once, by freeing the entire
chain.

.. _`chain_allocator.note`:

NOTE
----

The chain allocator may be inefficient if the allocated objects
are not much smaller than PAGE_SIZE.

.. _`bm_end_of_map`:

BM_END_OF_MAP
=============

.. c:function::  BM_END_OF_MAP()

.. _`bm_end_of_map.description`:

Description
-----------

Memory bitmap is a structure consiting of many linked lists of
objects.  The main list's elements are of type struct zone_bitmap
and each of them corresonds to one zone.  For each zone bitmap
object there is a list of objects of type struct bm_block that
represent each blocks of bitmap in which information is stored.

struct memory_bitmap contains a pointer to the main list of zone
bitmap objects, a struct bm_position used for browsing the bitmap,
and a pointer to the list of pages used for allocating all of the
zone bitmap objects and bitmap block objects.

.. _`bm_end_of_map.note`:

NOTE
----

It has to be possible to lay out the bitmap in memory
using only allocations of order 0.  Additionally, the bitmap is
designed to work with arbitrary number of zones (this is over the
top for now, but let's avoid making unnecessary assumptions ;-).

struct zone_bitmap contains a pointer to a list of bitmap block
objects and a pointer to the bitmap block object that has been
most recently used for setting bits.  Additionally, it contains the
pfns that correspond to the start and end of the represented zone.

struct bm_block contains a pointer to the memory page in which
information is stored (in the form of a block of bitmap)
It also contains the pfns that correspond to the start and end of
the represented memory area.

The memory bitmap is organized as a radix tree to guarantee fast random
access to the bits. There is one radix tree for each zone (as returned
from create_mem_extents).

One radix tree is represented by one struct mem_zone_bm_rtree. There are
two linked lists for the nodes of the tree, one for the inner nodes and
one for the leave nodes. The linked leave nodes are used for fast linear
access of the memory bitmap.

The struct rtree_node represents one node of the radix tree.

.. _`free_mem_extents`:

free_mem_extents
================

.. c:function:: void free_mem_extents(struct list_head *list)

    free a list of memory extents \ ``list``\  - list of extents to empty

    :param struct list_head \*list:
        *undescribed*

.. _`create_mem_extents`:

create_mem_extents
==================

.. c:function:: int create_mem_extents(struct list_head *list, gfp_t gfp_mask)

    create a list of memory extents representing contiguous ranges of PFNs \ ``list``\  - list to put the extents into \ ``gfp_mask``\  - mask to use for memory allocations

    :param struct list_head \*list:
        *undescribed*

    :param gfp_t gfp_mask:
        *undescribed*

.. _`memory_bm_create`:

memory_bm_create
================

.. c:function:: int memory_bm_create(struct memory_bitmap *bm, gfp_t gfp_mask, int safe_needed)

    allocate memory for a memory bitmap

    :param struct memory_bitmap \*bm:
        *undescribed*

    :param gfp_t gfp_mask:
        *undescribed*

    :param int safe_needed:
        *undescribed*

.. _`memory_bm_free`:

memory_bm_free
==============

.. c:function:: void memory_bm_free(struct memory_bitmap *bm, int clear_nosave_free)

    free memory occupied by the memory bitmap \ ``bm``\ 

    :param struct memory_bitmap \*bm:
        *undescribed*

    :param int clear_nosave_free:
        *undescribed*

.. _`memory_bm_find_bit`:

memory_bm_find_bit
==================

.. c:function:: int memory_bm_find_bit(struct memory_bitmap *bm, unsigned long pfn, void **addr, unsigned int *bit_nr)

    Find the bit for pfn in the memory bitmap

    :param struct memory_bitmap \*bm:
        *undescribed*

    :param unsigned long pfn:
        *undescribed*

    :param void \*\*addr:
        *undescribed*

    :param unsigned int \*bit_nr:
        *undescribed*

.. _`memory_bm_find_bit.description`:

Description
-----------

Find the bit in the bitmap \ ``bm``\  that corresponds to given pfn.
The cur.zone, cur.block and cur.node_pfn member of \ ``bm``\  are
updated.
It walks the radix tree to find the page which contains the bit for
pfn and returns the bit position in \*\*addr and \*bit_nr.

.. _`memory_bm_next_pfn`:

memory_bm_next_pfn
==================

.. c:function:: unsigned long memory_bm_next_pfn(struct memory_bitmap *bm)

    Find the next set bit in the bitmap \ ``bm``\ 

    :param struct memory_bitmap \*bm:
        *undescribed*

.. _`memory_bm_next_pfn.description`:

Description
-----------

Starting from the last returned position this function searches
for the next set bit in the memory bitmap and returns its
number. If no more bit is set BM_END_OF_MAP is returned.

It is required to run \ :c:func:`memory_bm_position_reset`\  before the
first call to this function.

.. _`__register_nosave_region`:

__register_nosave_region
========================

.. c:function:: void __register_nosave_region(unsigned long start_pfn, unsigned long end_pfn, int use_kmalloc)

    register a range of page frames the contents of which should not be saved during the suspend (to be used in the early initialization code)

    :param unsigned long start_pfn:
        *undescribed*

    :param unsigned long end_pfn:
        *undescribed*

    :param int use_kmalloc:
        *undescribed*

.. _`mark_nosave_pages`:

mark_nosave_pages
=================

.. c:function:: void mark_nosave_pages(struct memory_bitmap *bm)

    set bits corresponding to the page frames the contents of which should not be saved in a given bitmap.

    :param struct memory_bitmap \*bm:
        *undescribed*

.. _`create_basic_memory_bitmaps`:

create_basic_memory_bitmaps
===========================

.. c:function:: int create_basic_memory_bitmaps( void)

    create bitmaps needed for marking page frames that should not be saved and free page frames.  The pointers forbidden_pages_map and free_pages_map are only modified if everything goes well, because we don't want the bits to be used before both bitmaps are set up.

    :param  void:
        no arguments

.. _`free_basic_memory_bitmaps`:

free_basic_memory_bitmaps
=========================

.. c:function:: void free_basic_memory_bitmaps( void)

    free memory bitmaps allocated by \ :c:func:`create_basic_memory_bitmaps`\ .  The auxiliary pointers are necessary so that the bitmaps themselves are not referred to while they are being freed.

    :param  void:
        no arguments

.. _`snapshot_additional_pages`:

snapshot_additional_pages
=========================

.. c:function:: unsigned int snapshot_additional_pages(struct zone *zone)

    estimate the number of additional pages be needed for setting up the suspend image data structures for given zone (usually the returned value is greater than the exact number)

    :param struct zone \*zone:
        *undescribed*

.. _`count_free_highmem_pages`:

count_free_highmem_pages
========================

.. c:function:: unsigned int count_free_highmem_pages( void)

    compute the total number of free highmem pages, system-wide.

    :param  void:
        no arguments

.. _`saveable_highmem_page`:

saveable_highmem_page
=====================

.. c:function:: struct page *saveable_highmem_page(struct zone *zone, unsigned long pfn)

    Determine whether a highmem page should be included in the suspend image.

    :param struct zone \*zone:
        *undescribed*

    :param unsigned long pfn:
        *undescribed*

.. _`saveable_highmem_page.description`:

Description
-----------

We should save the page if it isn't Nosave or NosaveFree, or Reserved,
and it isn't a part of a free chunk of pages.

.. _`count_highmem_pages`:

count_highmem_pages
===================

.. c:function:: unsigned int count_highmem_pages( void)

    compute the total number of saveable highmem pages.

    :param  void:
        no arguments

.. _`saveable_page`:

saveable_page
=============

.. c:function:: struct page *saveable_page(struct zone *zone, unsigned long pfn)

    Determine whether a non-highmem page should be included in the suspend image.

    :param struct zone \*zone:
        *undescribed*

    :param unsigned long pfn:
        *undescribed*

.. _`saveable_page.description`:

Description
-----------

We should save the page if it isn't Nosave, and is not in the range
of pages statically defined as 'unsaveable', and it isn't a part of
a free chunk of pages.

.. _`count_data_pages`:

count_data_pages
================

.. c:function:: unsigned int count_data_pages( void)

    compute the total number of saveable non-highmem pages.

    :param  void:
        no arguments

.. _`safe_copy_page`:

safe_copy_page
==============

.. c:function:: void safe_copy_page(void *dst, struct page *s_page)

    check if the page we are going to copy is marked as present in the kernel page tables (this always is the case if CONFIG_DEBUG_PAGEALLOC is not set and in that case \ :c:func:`kernel_page_present`\  always returns 'true').

    :param void \*dst:
        *undescribed*

    :param struct page \*s_page:
        *undescribed*

.. _`swsusp_free`:

swsusp_free
===========

.. c:function:: void swsusp_free( void)

    free pages allocated for the suspend.

    :param  void:
        no arguments

.. _`swsusp_free.description`:

Description
-----------

Suspend pages are alocated before the atomic copy is made, so we
need to release them after the resume.

.. _`preallocate_image_pages`:

preallocate_image_pages
=======================

.. c:function:: unsigned long preallocate_image_pages(unsigned long nr_pages, gfp_t mask)

    Allocate a number of pages for hibernation image

    :param unsigned long nr_pages:
        Number of page frames to allocate.

    :param gfp_t mask:
        GFP flags to use for the allocation.

.. _`preallocate_image_pages.return-value`:

Return value
------------

Number of page frames actually allocated

.. _`__fraction`:

__fraction
==========

.. c:function:: unsigned long __fraction(u64 x, u64 multiplier, u64 base)

    Compute (an approximation of) x \* (multiplier / base)

    :param u64 x:
        *undescribed*

    :param u64 multiplier:
        *undescribed*

    :param u64 base:
        *undescribed*

.. _`free_unnecessary_pages`:

free_unnecessary_pages
======================

.. c:function:: unsigned long free_unnecessary_pages( void)

    Release preallocated pages not needed for the image

    :param  void:
        no arguments

.. _`minimum_image_size`:

minimum_image_size
==================

.. c:function:: unsigned long minimum_image_size(unsigned long saveable)

    Estimate the minimum acceptable size of an image

    :param unsigned long saveable:
        Number of saveable pages in the system.

.. _`minimum_image_size.description`:

Description
-----------

We want to avoid attempting to free too much memory too hard, so estimate the
minimum acceptable size of a hibernation image to use as the lower limit for
preallocating memory.

We assume that the minimum image size should be proportional to

[number of saveable pages] - [number of pages that can be freed in theory]

where the second term is the sum of (1) reclaimable slab pages, (2) active
and (3) inactive anonymous pages, (4) active and (5) inactive file pages,
minus mapped file pages.

.. _`hibernate_preallocate_memory`:

hibernate_preallocate_memory
============================

.. c:function:: int hibernate_preallocate_memory( void)

    Preallocate memory for hibernation image

    :param  void:
        no arguments

.. _`hibernate_preallocate_memory.description`:

Description
-----------

To create a hibernation image it is necessary to make a copy of every page
frame in use.  We also need a number of page frames to be free during
hibernation for allocations made while saving the image and for device
drivers, in case they need to allocate memory from their hibernation
callbacks (these two numbers are given by PAGES_FOR_IO (which is a rough
estimate) and reserverd_size divided by PAGE_SIZE (which is tunable through
/sys/power/reserved_size, respectively).  To make this happen, we compute the
total number of available page frames and allocate at least

([page frames total] + PAGES_FOR_IO + [metadata pages]) / 2
+ 2 \* DIV_ROUND_UP(reserved_size, PAGE_SIZE)

of them, which corresponds to the maximum size of a hibernation image.

If image_size is set below the number following from the above formula,
the preallocation of memory is continued until the total number of saveable
pages in the system is below the requested image size or the minimum
acceptable image size returned by \ :c:func:`minimum_image_size`\ , whichever is greater.

.. _`count_pages_for_highmem`:

count_pages_for_highmem
=======================

.. c:function:: unsigned int count_pages_for_highmem(unsigned int nr_highmem)

    compute the number of non-highmem pages that will be necessary for creating copies of highmem pages.

    :param unsigned int nr_highmem:
        *undescribed*

.. _`enough_free_mem`:

enough_free_mem
===============

.. c:function:: int enough_free_mem(unsigned int nr_pages, unsigned int nr_highmem)

    Make sure we have enough free memory for the snapshot image.

    :param unsigned int nr_pages:
        *undescribed*

    :param unsigned int nr_highmem:
        *undescribed*

.. _`get_highmem_buffer`:

get_highmem_buffer
==================

.. c:function:: int get_highmem_buffer(int safe_needed)

    if there are some highmem pages in the suspend image, we may need the buffer to copy them and/or load their data.

    :param int safe_needed:
        *undescribed*

.. _`alloc_highmem_pages`:

alloc_highmem_pages
===================

.. c:function:: unsigned int alloc_highmem_pages(struct memory_bitmap *bm, unsigned int nr_highmem)

    allocate some highmem pages for the image. Try to allocate as many pages as needed, but if the number of free highmem pages is lesser than that, allocate them all.

    :param struct memory_bitmap \*bm:
        *undescribed*

    :param unsigned int nr_highmem:
        *undescribed*

.. _`swsusp_alloc`:

swsusp_alloc
============

.. c:function:: int swsusp_alloc(struct memory_bitmap *orig_bm, struct memory_bitmap *copy_bm, unsigned int nr_pages, unsigned int nr_highmem)

    allocate memory for the suspend image

    :param struct memory_bitmap \*orig_bm:
        *undescribed*

    :param struct memory_bitmap \*copy_bm:
        *undescribed*

    :param unsigned int nr_pages:
        *undescribed*

    :param unsigned int nr_highmem:
        *undescribed*

.. _`swsusp_alloc.description`:

Description
-----------

We first try to allocate as many highmem pages as there are
saveable highmem pages in the system.  If that fails, we allocate
non-highmem pages for the copies of the remaining highmem ones.

In this approach it is likely that the copies of highmem pages will
also be located in the high memory, because of the way in which
\ :c:func:`copy_data_pages`\  works.

.. _`pack_pfns`:

pack_pfns
=========

.. c:function:: void pack_pfns(unsigned long *buf, struct memory_bitmap *bm)

    pfns corresponding to the set bits found in the bitmap \ ``bm``\  are stored in the array \ ``buf``\ [] (1 page at a time)

    :param unsigned long \*buf:
        *undescribed*

    :param struct memory_bitmap \*bm:
        *undescribed*

.. _`snapshot_read_next`:

snapshot_read_next
==================

.. c:function:: int snapshot_read_next(struct snapshot_handle *handle)

    used for reading the system memory snapshot.

    :param struct snapshot_handle \*handle:
        *undescribed*

.. _`snapshot_read_next.description`:

Description
-----------

On the first call to it \ ``handle``\  should point to a zeroed
snapshot_handle structure.  The structure gets updated and a pointer
to it should be passed to this function every next time.

On success the function returns a positive number.  Then, the caller
is allowed to read up to the returned number of bytes from the memory
location computed by the \ :c:func:`data_of`\  macro.

The function returns 0 to indicate the end of data stream condition,
and a negative number is returned on error.  In such cases the
structure pointed to by \ ``handle``\  is not updated and should not be used
any more.

.. _`mark_unsafe_pages`:

mark_unsafe_pages
=================

.. c:function:: int mark_unsafe_pages(struct memory_bitmap *bm)

    mark the pages that cannot be used for storing the image during resume, because they conflict with the pages that had been used before suspend

    :param struct memory_bitmap \*bm:
        *undescribed*

.. _`load_header`:

load_header
===========

.. c:function:: int load_header(struct swsusp_info *info)

    check the image header and copy data from it

    :param struct swsusp_info \*info:
        *undescribed*

.. _`unpack_orig_pfns`:

unpack_orig_pfns
================

.. c:function:: int unpack_orig_pfns(unsigned long *buf, struct memory_bitmap *bm)

    for each element of \ ``buf``\ [] (1 page at a time) set the corresponding bit in the memory bitmap \ ``bm``\ 

    :param unsigned long \*buf:
        *undescribed*

    :param struct memory_bitmap \*bm:
        *undescribed*

.. _`count_highmem_image_pages`:

count_highmem_image_pages
=========================

.. c:function:: unsigned int count_highmem_image_pages(struct memory_bitmap *bm)

    compute the number of highmem pages in the suspend image.  The bits in the memory bitmap \ ``bm``\  that correspond to the image pages are assumed to be set.

    :param struct memory_bitmap \*bm:
        *undescribed*

.. _`copy_last_highmem_page`:

copy_last_highmem_page
======================

.. c:function:: void copy_last_highmem_page( void)

    copy the contents of a highmem image from \ ``buffer``\ , where the caller of \ :c:func:`snapshot_write_next`\  has place them, to the right location represented by \ ``last_highmem_page``\  .

    :param  void:
        no arguments

.. _`pbes_per_linked_page`:

PBES_PER_LINKED_PAGE
====================

.. c:function::  PBES_PER_LINKED_PAGE()

    use the memory bitmap \ ``bm``\  to mark the pages that will be overwritten in the process of restoring the system memory state from the suspend image ("unsafe" pages) and allocate memory for the image.

.. _`pbes_per_linked_page.description`:

Description
-----------

The idea is to allocate a new memory bitmap first and then allocate
as many pages as needed for the image data, but not to assign these
pages to specific tasks initially.  Instead, we just mark them as
allocated and create a lists of "safe" pages that will be used
later.  On systems with high memory a list of "safe" highmem pages is
also created.

.. _`get_buffer`:

get_buffer
==========

.. c:function:: void *get_buffer(struct memory_bitmap *bm, struct chain_allocator *ca)

    compute the address that \ :c:func:`snapshot_write_next`\  should set for its caller to write to.

    :param struct memory_bitmap \*bm:
        *undescribed*

    :param struct chain_allocator \*ca:
        *undescribed*

.. _`snapshot_write_next`:

snapshot_write_next
===================

.. c:function:: int snapshot_write_next(struct snapshot_handle *handle)

    used for writing the system memory snapshot.

    :param struct snapshot_handle \*handle:
        *undescribed*

.. _`snapshot_write_next.description`:

Description
-----------

On the first call to it \ ``handle``\  should point to a zeroed
snapshot_handle structure.  The structure gets updated and a pointer
to it should be passed to this function every next time.

On success the function returns a positive number.  Then, the caller
is allowed to write up to the returned number of bytes to the memory
location computed by the \ :c:func:`data_of`\  macro.

The function returns 0 to indicate the "end of file" condition,
and a negative number is returned on error.  In such cases the
structure pointed to by \ ``handle``\  is not updated and should not be used
any more.

.. _`snapshot_write_finalize`:

snapshot_write_finalize
=======================

.. c:function:: void snapshot_write_finalize(struct snapshot_handle *handle)

    must be called after the last call to \ :c:func:`snapshot_write_next`\  in case the last page in the image happens to be a highmem page and its contents should be stored in the highmem.  Additionally, it releases the memory that will not be used any more.

    :param struct snapshot_handle \*handle:
        *undescribed*

.. _`restore_highmem`:

restore_highmem
===============

.. c:function:: int restore_highmem( void)

    for each highmem page that was allocated before the suspend and included in the suspend image, and also has been allocated by the "resume" kernel swap its current (ie. "before resume") contents with the previous (ie. "before suspend") one.

    :param  void:
        no arguments

.. _`restore_highmem.description`:

Description
-----------

If the resume eventually fails, we can call this function once
again and restore the "before resume" highmem state.

.. This file was automatic generated / don't edit.

