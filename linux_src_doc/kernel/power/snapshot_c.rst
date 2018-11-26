.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/power/snapshot.c

.. _`get_image_page`:

get_image_page
==============

.. c:function:: void *get_image_page(gfp_t gfp_mask, int safe_needed)

    Allocate a page for a hibernation image.

    :param gfp_mask:
        GFP mask for the allocation.
    :type gfp_mask: gfp_t

    :param safe_needed:
        Get pages that were not used before hibernation (restore only)
    :type safe_needed: int

.. _`get_image_page.description`:

Description
-----------

During image restoration, for storing the PBE list and the image data, we can
only use memory pages that do not conflict with the pages used before
hibernation.  The "unsafe" pages have PageNosaveFree set and we count them
using allocated_unsafe_pages.

Each allocated image page is marked as PageNosave and PageNosaveFree so that
\ :c:func:`swsusp_free`\  can release it.

.. _`free_image_page`:

free_image_page
===============

.. c:function:: void free_image_page(void *addr, int clear_nosave_free)

    Free a page allocated for hibernation image.

    :param addr:
        Address of the page to free.
    :type addr: void \*

    :param clear_nosave_free:
        If set, clear the PageNosaveFree bit for the page.
    :type clear_nosave_free: int

.. _`free_image_page.description`:

Description
-----------

The page to free should have been allocated by \ :c:func:`get_image_page`\  (page flags
set by it are affected).

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
PFNs that correspond to the start and end of the represented zone.

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

.. _`alloc_rtree_node`:

alloc_rtree_node
================

.. c:function:: struct rtree_node *alloc_rtree_node(gfp_t gfp_mask, int safe_needed, struct chain_allocator *ca, struct list_head *list)

    Allocate a new node and add it to the radix tree.

    :param gfp_mask:
        *undescribed*
    :type gfp_mask: gfp_t

    :param safe_needed:
        *undescribed*
    :type safe_needed: int

    :param ca:
        *undescribed*
    :type ca: struct chain_allocator \*

    :param list:
        *undescribed*
    :type list: struct list_head \*

.. _`alloc_rtree_node.description`:

Description
-----------

This function is used to allocate inner nodes as well as the
leave nodes of the radix tree. It also adds the node to the
corresponding linked list passed in by the \*list parameter.

.. _`add_rtree_block`:

add_rtree_block
===============

.. c:function:: int add_rtree_block(struct mem_zone_bm_rtree *zone, gfp_t gfp_mask, int safe_needed, struct chain_allocator *ca)

    Add a new leave node to the radix tree.

    :param zone:
        *undescribed*
    :type zone: struct mem_zone_bm_rtree \*

    :param gfp_mask:
        *undescribed*
    :type gfp_mask: gfp_t

    :param safe_needed:
        *undescribed*
    :type safe_needed: int

    :param ca:
        *undescribed*
    :type ca: struct chain_allocator \*

.. _`add_rtree_block.description`:

Description
-----------

The leave nodes need to be allocated in order to keep the leaves
linked list in order. This is guaranteed by the zone->blocks
counter.

.. _`create_zone_bm_rtree`:

create_zone_bm_rtree
====================

.. c:function:: struct mem_zone_bm_rtree *create_zone_bm_rtree(gfp_t gfp_mask, int safe_needed, struct chain_allocator *ca, unsigned long start, unsigned long end)

    Create a radix tree for one zone.

    :param gfp_mask:
        *undescribed*
    :type gfp_mask: gfp_t

    :param safe_needed:
        *undescribed*
    :type safe_needed: int

    :param ca:
        *undescribed*
    :type ca: struct chain_allocator \*

    :param start:
        *undescribed*
    :type start: unsigned long

    :param end:
        *undescribed*
    :type end: unsigned long

.. _`create_zone_bm_rtree.description`:

Description
-----------

Allocated the mem_zone_bm_rtree structure and initializes it.
This function also allocated and builds the radix tree for the
zone.

.. _`free_zone_bm_rtree`:

free_zone_bm_rtree
==================

.. c:function:: void free_zone_bm_rtree(struct mem_zone_bm_rtree *zone, int clear_nosave_free)

    Free the memory of the radix tree.

    :param zone:
        *undescribed*
    :type zone: struct mem_zone_bm_rtree \*

    :param clear_nosave_free:
        *undescribed*
    :type clear_nosave_free: int

.. _`free_zone_bm_rtree.description`:

Description
-----------

Free all node pages of the radix tree. The mem_zone_bm_rtree
structure itself is not freed here nor are the rtree_node
structs.

.. _`free_mem_extents`:

free_mem_extents
================

.. c:function:: void free_mem_extents(struct list_head *list)

    Free a list of memory extents.

    :param list:
        List of extents to free.
    :type list: struct list_head \*

.. _`create_mem_extents`:

create_mem_extents
==================

.. c:function:: int create_mem_extents(struct list_head *list, gfp_t gfp_mask)

    Create a list of memory extents.

    :param list:
        List to put the extents into.
    :type list: struct list_head \*

    :param gfp_mask:
        Mask to use for memory allocations.
    :type gfp_mask: gfp_t

.. _`create_mem_extents.description`:

Description
-----------

The extents represent contiguous ranges of PFNs.

.. _`memory_bm_create`:

memory_bm_create
================

.. c:function:: int memory_bm_create(struct memory_bitmap *bm, gfp_t gfp_mask, int safe_needed)

    Allocate memory for a memory bitmap.

    :param bm:
        *undescribed*
    :type bm: struct memory_bitmap \*

    :param gfp_mask:
        *undescribed*
    :type gfp_mask: gfp_t

    :param safe_needed:
        *undescribed*
    :type safe_needed: int

.. _`memory_bm_free`:

memory_bm_free
==============

.. c:function:: void memory_bm_free(struct memory_bitmap *bm, int clear_nosave_free)

    Free memory occupied by the memory bitmap.

    :param bm:
        Memory bitmap.
    :type bm: struct memory_bitmap \*

    :param clear_nosave_free:
        *undescribed*
    :type clear_nosave_free: int

.. _`memory_bm_find_bit`:

memory_bm_find_bit
==================

.. c:function:: int memory_bm_find_bit(struct memory_bitmap *bm, unsigned long pfn, void **addr, unsigned int *bit_nr)

    Find the bit for a given PFN in a memory bitmap.

    :param bm:
        *undescribed*
    :type bm: struct memory_bitmap \*

    :param pfn:
        *undescribed*
    :type pfn: unsigned long

    :param addr:
        *undescribed*
    :type addr: void \*\*

    :param bit_nr:
        *undescribed*
    :type bit_nr: unsigned int \*

.. _`memory_bm_find_bit.description`:

Description
-----------

Find the bit in memory bitmap \ ``bm``\  that corresponds to the given PFN.
The cur.zone, cur.block and cur.node_pfn members of \ ``bm``\  are updated.

Walk the radix tree to find the page containing the bit that represents \ ``pfn``\ 
and return the position of the bit in \ ``addr``\  and \ ``bit_nr``\ .

.. _`memory_bm_next_pfn`:

memory_bm_next_pfn
==================

.. c:function:: unsigned long memory_bm_next_pfn(struct memory_bitmap *bm)

    Find the next set bit in a memory bitmap.

    :param bm:
        Memory bitmap.
    :type bm: struct memory_bitmap \*

.. _`memory_bm_next_pfn.description`:

Description
-----------

Starting from the last returned position this function searches for the next
set bit in \ ``bm``\  and returns the PFN represented by it.  If no more bits are
set, BM_END_OF_MAP is returned.

It is required to run \ :c:func:`memory_bm_position_reset`\  before the first call to
this function for the given memory bitmap.

.. _`__register_nosave_region`:

\__register_nosave_region
=========================

.. c:function:: void __register_nosave_region(unsigned long start_pfn, unsigned long end_pfn, int use_kmalloc)

    Register a region of unsaveable memory.

    :param start_pfn:
        *undescribed*
    :type start_pfn: unsigned long

    :param end_pfn:
        *undescribed*
    :type end_pfn: unsigned long

    :param use_kmalloc:
        *undescribed*
    :type use_kmalloc: int

.. _`__register_nosave_region.description`:

Description
-----------

Register a range of page frames the contents of which should not be saved
during hibernation (to be used in the early initialization code).

.. _`mark_nosave_pages`:

mark_nosave_pages
=================

.. c:function:: void mark_nosave_pages(struct memory_bitmap *bm)

    Mark pages that should not be saved.

    :param bm:
        Memory bitmap.
    :type bm: struct memory_bitmap \*

.. _`mark_nosave_pages.description`:

Description
-----------

Set the bits in \ ``bm``\  that correspond to the page frames the contents of which
should not be saved.

.. _`create_basic_memory_bitmaps`:

create_basic_memory_bitmaps
===========================

.. c:function:: int create_basic_memory_bitmaps( void)

    Create bitmaps to hold basic page information.

    :param void:
        no arguments
    :type void: 

.. _`create_basic_memory_bitmaps.description`:

Description
-----------

Create bitmaps needed for marking page frames that should not be saved and
free page frames.  The forbidden_pages_map and free_pages_map pointers are
only modified if everything goes well, because we don't want the bits to be
touched before both bitmaps are set up.

.. _`free_basic_memory_bitmaps`:

free_basic_memory_bitmaps
=========================

.. c:function:: void free_basic_memory_bitmaps( void)

    Free memory bitmaps holding basic information.

    :param void:
        no arguments
    :type void: 

.. _`free_basic_memory_bitmaps.description`:

Description
-----------

Free memory bitmaps allocated by \ :c:func:`create_basic_memory_bitmaps`\ .  The
auxiliary pointers are necessary so that the bitmaps themselves are not
referred to while they are being freed.

.. _`snapshot_additional_pages`:

snapshot_additional_pages
=========================

.. c:function:: unsigned int snapshot_additional_pages(struct zone *zone)

    Estimate the number of extra pages needed.

    :param zone:
        Memory zone to carry out the computation for.
    :type zone: struct zone \*

.. _`snapshot_additional_pages.description`:

Description
-----------

Estimate the number of additional pages needed for setting up a hibernation
image data structures for \ ``zone``\  (usually, the returned value is greater than
the exact number).

.. _`count_free_highmem_pages`:

count_free_highmem_pages
========================

.. c:function:: unsigned int count_free_highmem_pages( void)

    Compute the total number of free highmem pages.

    :param void:
        no arguments
    :type void: 

.. _`count_free_highmem_pages.description`:

Description
-----------

The returned number is system-wide.

.. _`saveable_highmem_page`:

saveable_highmem_page
=====================

.. c:function:: struct page *saveable_highmem_page(struct zone *zone, unsigned long pfn)

    Check if a highmem page is saveable.

    :param zone:
        *undescribed*
    :type zone: struct zone \*

    :param pfn:
        *undescribed*
    :type pfn: unsigned long

.. _`saveable_highmem_page.description`:

Description
-----------

Determine whether a highmem page should be included in a hibernation image.

We should save the page if it isn't Nosave or NosaveFree, or Reserved,
and it isn't part of a free chunk of pages.

.. _`count_highmem_pages`:

count_highmem_pages
===================

.. c:function:: unsigned int count_highmem_pages( void)

    Compute the total number of saveable highmem pages.

    :param void:
        no arguments
    :type void: 

.. _`saveable_page`:

saveable_page
=============

.. c:function:: struct page *saveable_page(struct zone *zone, unsigned long pfn)

    Check if the given page is saveable.

    :param zone:
        *undescribed*
    :type zone: struct zone \*

    :param pfn:
        *undescribed*
    :type pfn: unsigned long

.. _`saveable_page.description`:

Description
-----------

Determine whether a non-highmem page should be included in a hibernation
image.

We should save the page if it isn't Nosave, and is not in the range
of pages statically defined as 'unsaveable', and it isn't part of
a free chunk of pages.

.. _`count_data_pages`:

count_data_pages
================

.. c:function:: unsigned int count_data_pages( void)

    Compute the total number of saveable non-highmem pages.

    :param void:
        no arguments
    :type void: 

.. _`safe_copy_page`:

safe_copy_page
==============

.. c:function:: void safe_copy_page(void *dst, struct page *s_page)

    Copy a page in a safe way.

    :param dst:
        *undescribed*
    :type dst: void \*

    :param s_page:
        *undescribed*
    :type s_page: struct page \*

.. _`safe_copy_page.description`:

Description
-----------

Check if the page we are going to copy is marked as present in the kernel
page tables (this always is the case if CONFIG_DEBUG_PAGEALLOC is not set
and in that case \ :c:func:`kernel_page_present`\  always returns 'true').

.. _`swsusp_free`:

swsusp_free
===========

.. c:function:: void swsusp_free( void)

    Free pages allocated for hibernation image.

    :param void:
        no arguments
    :type void: 

.. _`swsusp_free.description`:

Description
-----------

Image pages are alocated before snapshot creation, so they need to be
released after resume.

.. _`preallocate_image_pages`:

preallocate_image_pages
=======================

.. c:function:: unsigned long preallocate_image_pages(unsigned long nr_pages, gfp_t mask)

    Allocate a number of pages for hibernation image.

    :param nr_pages:
        Number of page frames to allocate.
    :type nr_pages: unsigned long

    :param mask:
        GFP flags to use for the allocation.
    :type mask: gfp_t

.. _`preallocate_image_pages.return-value`:

Return value
------------

Number of page frames actually allocated

.. _`__fraction`:

\__fraction
===========

.. c:function:: unsigned long __fraction(u64 x, u64 multiplier, u64 base)

    Compute (an approximation of) x \* (multiplier / base).

    :param x:
        *undescribed*
    :type x: u64

    :param multiplier:
        *undescribed*
    :type multiplier: u64

    :param base:
        *undescribed*
    :type base: u64

.. _`free_unnecessary_pages`:

free_unnecessary_pages
======================

.. c:function:: unsigned long free_unnecessary_pages( void)

    Release preallocated pages not needed for the image.

    :param void:
        no arguments
    :type void: 

.. _`minimum_image_size`:

minimum_image_size
==================

.. c:function:: unsigned long minimum_image_size(unsigned long saveable)

    Estimate the minimum acceptable size of an image.

    :param saveable:
        Number of saveable pages in the system.
    :type saveable: unsigned long

.. _`minimum_image_size.description`:

Description
-----------

We want to avoid attempting to free too much memory too hard, so estimate the
minimum acceptable size of a hibernation image to use as the lower limit for
preallocating memory.

We assume that the minimum image size should be proportional to

[number of saveable pages] - [number of pages that can be freed in theory]

where the second term is the sum of (1) reclaimable slab pages, (2) active
and (3) inactive anonymous pages, (4) active and (5) inactive file pages.

.. _`hibernate_preallocate_memory`:

hibernate_preallocate_memory
============================

.. c:function:: int hibernate_preallocate_memory( void)

    Preallocate memory for hibernation image.

    :param void:
        no arguments
    :type void: 

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

    Count non-highmem pages needed for copying highmem.

    :param nr_highmem:
        *undescribed*
    :type nr_highmem: unsigned int

.. _`count_pages_for_highmem.description`:

Description
-----------

Compute the number of non-highmem pages that will be necessary for creating
copies of highmem pages.

.. _`enough_free_mem`:

enough_free_mem
===============

.. c:function:: int enough_free_mem(unsigned int nr_pages, unsigned int nr_highmem)

    Check if there is enough free memory for the image.

    :param nr_pages:
        *undescribed*
    :type nr_pages: unsigned int

    :param nr_highmem:
        *undescribed*
    :type nr_highmem: unsigned int

.. _`get_highmem_buffer`:

get_highmem_buffer
==================

.. c:function:: int get_highmem_buffer(int safe_needed)

    Allocate a buffer for highmem pages.

    :param safe_needed:
        *undescribed*
    :type safe_needed: int

.. _`get_highmem_buffer.description`:

Description
-----------

If there are some highmem pages in the hibernation image, we may need a
buffer to copy them and/or load their data.

.. _`alloc_highmem_pages`:

alloc_highmem_pages
===================

.. c:function:: unsigned int alloc_highmem_pages(struct memory_bitmap *bm, unsigned int nr_highmem)

    Allocate some highmem pages for the image.

    :param bm:
        *undescribed*
    :type bm: struct memory_bitmap \*

    :param nr_highmem:
        *undescribed*
    :type nr_highmem: unsigned int

.. _`alloc_highmem_pages.description`:

Description
-----------

Try to allocate as many pages as needed, but if the number of free highmem
pages is less than that, allocate them all.

.. _`swsusp_alloc`:

swsusp_alloc
============

.. c:function:: int swsusp_alloc(struct memory_bitmap *copy_bm, unsigned int nr_pages, unsigned int nr_highmem)

    Allocate memory for hibernation image.

    :param copy_bm:
        *undescribed*
    :type copy_bm: struct memory_bitmap \*

    :param nr_pages:
        *undescribed*
    :type nr_pages: unsigned int

    :param nr_highmem:
        *undescribed*
    :type nr_highmem: unsigned int

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

    Prepare PFNs for saving.

    :param buf:
        Memory buffer to store the PFNs in.
    :type buf: unsigned long \*

    :param bm:
        Memory bitmap.
    :type bm: struct memory_bitmap \*

.. _`pack_pfns.description`:

Description
-----------

PFNs corresponding to set bits in \ ``bm``\  are stored in the area of memory
pointed to by \ ``buf``\  (1 page at a time).

.. _`snapshot_read_next`:

snapshot_read_next
==================

.. c:function:: int snapshot_read_next(struct snapshot_handle *handle)

    Get the address to read the next image page from.

    :param handle:
        Snapshot handle to be used for the reading.
    :type handle: struct snapshot_handle \*

.. _`snapshot_read_next.description`:

Description
-----------

On the first call, \ ``handle``\  should point to a zeroed snapshot_handle
structure.  The structure gets populated then and a pointer to it should be
passed to this function every next time.

On success, the function returns a positive number.  Then, the caller
is allowed to read up to the returned number of bytes from the memory
location computed by the \ :c:func:`data_of`\  macro.

The function returns 0 to indicate the end of the data stream condition,
and negative numbers are returned on errors.  If that happens, the structure
pointed to by \ ``handle``\  is not updated and should not be used any more.

.. _`mark_unsafe_pages`:

mark_unsafe_pages
=================

.. c:function:: void mark_unsafe_pages(struct memory_bitmap *bm)

    Mark pages that were used before hibernation.

    :param bm:
        *undescribed*
    :type bm: struct memory_bitmap \*

.. _`mark_unsafe_pages.description`:

Description
-----------

Mark the pages that cannot be used for storing the image during restoration,
because they conflict with the pages that had been used before hibernation.

.. _`load_header`:

load_header
===========

.. c:function:: int load_header(struct swsusp_info *info)

    Check the image header and copy the data from it.

    :param info:
        *undescribed*
    :type info: struct swsusp_info \*

.. _`unpack_orig_pfns`:

unpack_orig_pfns
================

.. c:function:: int unpack_orig_pfns(unsigned long *buf, struct memory_bitmap *bm)

    Set bits corresponding to given PFNs in a memory bitmap.

    :param buf:
        Area of memory containing the PFNs.
    :type buf: unsigned long \*

    :param bm:
        Memory bitmap.
    :type bm: struct memory_bitmap \*

.. _`unpack_orig_pfns.description`:

Description
-----------

For each element of the array pointed to by \ ``buf``\  (1 page at a time), set the
corresponding bit in \ ``bm``\ .

.. _`count_highmem_image_pages`:

count_highmem_image_pages
=========================

.. c:function:: unsigned int count_highmem_image_pages(struct memory_bitmap *bm)

    Compute the number of highmem pages in the image.

    :param bm:
        Memory bitmap.
    :type bm: struct memory_bitmap \*

.. _`count_highmem_image_pages.description`:

Description
-----------

The bits in \ ``bm``\  that correspond to image pages are assumed to be set.

.. _`prepare_highmem_image`:

prepare_highmem_image
=====================

.. c:function:: int prepare_highmem_image(struct memory_bitmap *bm, unsigned int *nr_highmem_p)

    Allocate memory for loading highmem data from image.

    :param bm:
        Pointer to an uninitialized memory bitmap structure.
    :type bm: struct memory_bitmap \*

    :param nr_highmem_p:
        Pointer to the number of highmem image pages.
    :type nr_highmem_p: unsigned int \*

.. _`prepare_highmem_image.description`:

Description
-----------

Try to allocate as many highmem pages as there are highmem image pages
(@nr_highmem_p points to the variable containing the number of highmem image
pages).  The pages that are "safe" (ie. will not be overwritten when the
hibernation image is restored entirely) have the corresponding bits set in
\ ``bm``\  (it must be unitialized).

.. _`prepare_highmem_image.note`:

NOTE
----

This function should not be called if there are no highmem image pages.

.. _`get_highmem_page_buffer`:

get_highmem_page_buffer
=======================

.. c:function:: void *get_highmem_page_buffer(struct page *page, struct chain_allocator *ca)

    Prepare a buffer to store a highmem image page.

    :param page:
        *undescribed*
    :type page: struct page \*

    :param ca:
        *undescribed*
    :type ca: struct chain_allocator \*

.. _`get_highmem_page_buffer.description`:

Description
-----------

For a given highmem image page get a buffer that \ :c:func:`suspend_write_next`\  should
return to its caller to write to.

If the page is to be saved to its "original" page frame or a copy of
the page is to be made in the highmem, \ ``buffer``\  is returned.  Otherwise,
the copy of the page is to be made in normal memory, so the address of
the copy is returned.

If \ ``buffer``\  is returned, the caller of \ :c:func:`suspend_write_next`\  will write
the page's contents to \ ``buffer``\ , so they will have to be copied to the
right location on the next call to \ :c:func:`suspend_write_next`\  and it is done
with the help of \ :c:func:`copy_last_highmem_page`\ .  For this purpose, if
\ ``buffer``\  is returned, \ ``last_highmem_page``\  is set to the page to which
the data will have to be copied from \ ``buffer``\ .

.. _`copy_last_highmem_page`:

copy_last_highmem_page
======================

.. c:function:: void copy_last_highmem_page( void)

    Copy most the most recent highmem image page.

    :param void:
        no arguments
    :type void: 

.. _`copy_last_highmem_page.description`:

Description
-----------

Copy the contents of a highmem image from \ ``buffer``\ , where the caller of
\ :c:func:`snapshot_write_next`\  has stored them, to the right location represented by
\ ``last_highmem_page``\  .

.. _`prepare_image`:

prepare_image
=============

.. c:function:: int prepare_image(struct memory_bitmap *new_bm, struct memory_bitmap *bm)

    Make room for loading hibernation image.

    :param new_bm:
        Unitialized memory bitmap structure.
    :type new_bm: struct memory_bitmap \*

    :param bm:
        Memory bitmap with unsafe pages marked.
    :type bm: struct memory_bitmap \*

.. _`prepare_image.description`:

Description
-----------

Use \ ``bm``\  to mark the pages that will be overwritten in the process of
restoring the system memory state from the suspend image ("unsafe" pages)
and allocate memory for the image.

The idea is to allocate a new memory bitmap first and then allocate
as many pages as needed for image data, but without specifying what those
pages will be used for just yet.  Instead, we mark them all as allocated and
create a lists of "safe" pages to be used later.  On systems with high
memory a list of "safe" highmem pages is created too.

.. _`get_buffer`:

get_buffer
==========

.. c:function:: void *get_buffer(struct memory_bitmap *bm, struct chain_allocator *ca)

    Get the address to store the next image data page.

    :param bm:
        *undescribed*
    :type bm: struct memory_bitmap \*

    :param ca:
        *undescribed*
    :type ca: struct chain_allocator \*

.. _`get_buffer.description`:

Description
-----------

Get the address that \ :c:func:`snapshot_write_next`\  should return to its caller to
write to.

.. _`snapshot_write_next`:

snapshot_write_next
===================

.. c:function:: int snapshot_write_next(struct snapshot_handle *handle)

    Get the address to store the next image page.

    :param handle:
        Snapshot handle structure to guide the writing.
    :type handle: struct snapshot_handle \*

.. _`snapshot_write_next.description`:

Description
-----------

On the first call, \ ``handle``\  should point to a zeroed snapshot_handle
structure.  The structure gets populated then and a pointer to it should be
passed to this function every next time.

On success, the function returns a positive number.  Then, the caller
is allowed to write up to the returned number of bytes to the memory
location computed by the \ :c:func:`data_of`\  macro.

The function returns 0 to indicate the "end of file" condition.  Negative
numbers are returned on errors, in which cases the structure pointed to by
\ ``handle``\  is not updated and should not be used any more.

.. _`snapshot_write_finalize`:

snapshot_write_finalize
=======================

.. c:function:: void snapshot_write_finalize(struct snapshot_handle *handle)

    Complete the loading of a hibernation image.

    :param handle:
        *undescribed*
    :type handle: struct snapshot_handle \*

.. _`snapshot_write_finalize.description`:

Description
-----------

Must be called after the last call to \ :c:func:`snapshot_write_next`\  in case the last
page in the image happens to be a highmem page and its contents should be
stored in highmem.  Additionally, it recycles bitmap memory that's not
necessary any more.

.. _`restore_highmem`:

restore_highmem
===============

.. c:function:: int restore_highmem( void)

    Put highmem image pages into their original locations.

    :param void:
        no arguments
    :type void: 

.. _`restore_highmem.description`:

Description
-----------

For each highmem page that was in use before hibernation and is included in
the image, and also has been allocated by the "restore" kernel, swap its
current contents with the previous (ie. "before hibernation") ones.

If the restore eventually fails, we can call this function once again and
restore the highmem state as seen by the restore kernel.

.. This file was automatic generated / don't edit.

