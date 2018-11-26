.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/memblock.c

.. _`memblock-overview`:

memblock overview
=================

Memblock is a method of managing memory regions during the early
boot period when the usual kernel memory allocators are not up and
running.

Memblock views the system memory as collections of contiguous
regions. There are several types of these collections:

* ``memory`` - describes the physical memory available to the
  kernel; this may differ from the actual physical memory installed
  in the system, for instance when the memory is restricted with
  ``mem=`` command line parameter
* ``reserved`` - describes the regions that were allocated
* ``physmap`` - describes the actual physical memory regardless of
  the possible restrictions; the ``physmap`` type is only available
  on some architectures.

Each region is represented by :c:type:`struct memblock_region` that
defines the region extents, its attributes and NUMA node id on NUMA
systems. Every memory type is described by the :c:type:`struct
memblock_type` which contains an array of memory regions along with
the allocator metadata. The memory types are nicely wrapped with
:c:type:`struct memblock`. This structure is statically initialzed
at build time. The region arrays for the "memory" and "reserved"
types are initially sized to \ ``INIT_MEMBLOCK_REGIONS``\  and for the
"physmap" type to \ ``INIT_PHYSMEM_REGIONS``\ .
The :c:func:`memblock_allow_resize` enables automatic resizing of
the region arrays during addition of new regions. This feature
should be used with care so that memory allocated for the region
array will not overlap with areas that should be reserved, for
example initrd.

The early architecture setup should tell memblock what the physical
memory layout is by using :c:func:`memblock_add` or
:c:func:`memblock_add_node` functions. The first function does not
assign the region to a NUMA node and it is appropriate for UMA
systems. Yet, it is possible to use it on NUMA systems as well and
assign the region to a NUMA node later in the setup process using
:c:func:`memblock_set_node`. The :c:func:`memblock_add_node`
performs such an assignment directly.

Once memblock is setup the memory can be allocated using either
memblock or bootmem APIs.

As the system boot progresses, the architecture specific
:c:func:`mem_init` function frees all the memory to the buddy page
allocator.

If an architecure enables \ ``CONFIG_ARCH_DISCARD_MEMBLOCK``\ , the
memblock data structures will be discarded after the system
initialization compltes.

.. _`__memblock_find_range_bottom_up`:

__memblock_find_range_bottom_up
===============================

.. c:function:: phys_addr_t __init_memblock __memblock_find_range_bottom_up(phys_addr_t start, phys_addr_t end, phys_addr_t size, phys_addr_t align, int nid, enum memblock_flags flags)

    find free area utility in bottom-up

    :param start:
        start of candidate range
    :type start: phys_addr_t

    :param end:
        end of candidate range, can be \ ``MEMBLOCK_ALLOC_ANYWHERE``\  or
        \ ``MEMBLOCK_ALLOC_ACCESSIBLE``\ 
    :type end: phys_addr_t

    :param size:
        size of free area to find
    :type size: phys_addr_t

    :param align:
        alignment of free area to find
    :type align: phys_addr_t

    :param nid:
        nid of the free area to find, \ ``NUMA_NO_NODE``\  for any node
    :type nid: int

    :param flags:
        pick from blocks based on memory attributes
    :type flags: enum memblock_flags

.. _`__memblock_find_range_bottom_up.description`:

Description
-----------

Utility called from \ :c:func:`memblock_find_in_range_node`\ , find free area bottom-up.

.. _`__memblock_find_range_bottom_up.return`:

Return
------

Found address on success, 0 on failure.

.. _`__memblock_find_range_top_down`:

__memblock_find_range_top_down
==============================

.. c:function:: phys_addr_t __init_memblock __memblock_find_range_top_down(phys_addr_t start, phys_addr_t end, phys_addr_t size, phys_addr_t align, int nid, enum memblock_flags flags)

    find free area utility, in top-down

    :param start:
        start of candidate range
    :type start: phys_addr_t

    :param end:
        end of candidate range, can be \ ``MEMBLOCK_ALLOC_ANYWHERE``\  or
        \ ``MEMBLOCK_ALLOC_ACCESSIBLE``\ 
    :type end: phys_addr_t

    :param size:
        size of free area to find
    :type size: phys_addr_t

    :param align:
        alignment of free area to find
    :type align: phys_addr_t

    :param nid:
        nid of the free area to find, \ ``NUMA_NO_NODE``\  for any node
    :type nid: int

    :param flags:
        pick from blocks based on memory attributes
    :type flags: enum memblock_flags

.. _`__memblock_find_range_top_down.description`:

Description
-----------

Utility called from \ :c:func:`memblock_find_in_range_node`\ , find free area top-down.

.. _`__memblock_find_range_top_down.return`:

Return
------

Found address on success, 0 on failure.

.. _`memblock_find_in_range_node`:

memblock_find_in_range_node
===========================

.. c:function:: phys_addr_t __init_memblock memblock_find_in_range_node(phys_addr_t size, phys_addr_t align, phys_addr_t start, phys_addr_t end, int nid, enum memblock_flags flags)

    find free area in given range and node

    :param size:
        size of free area to find
    :type size: phys_addr_t

    :param align:
        alignment of free area to find
    :type align: phys_addr_t

    :param start:
        start of candidate range
    :type start: phys_addr_t

    :param end:
        end of candidate range, can be \ ``MEMBLOCK_ALLOC_ANYWHERE``\  or
        \ ``MEMBLOCK_ALLOC_ACCESSIBLE``\ 
    :type end: phys_addr_t

    :param nid:
        nid of the free area to find, \ ``NUMA_NO_NODE``\  for any node
    :type nid: int

    :param flags:
        pick from blocks based on memory attributes
    :type flags: enum memblock_flags

.. _`memblock_find_in_range_node.description`:

Description
-----------

Find \ ``size``\  free area aligned to \ ``align``\  in the specified range and node.

When allocation direction is bottom-up, the \ ``start``\  should be greater
than the end of the kernel image. Otherwise, it will be trimmed. The
reason is that we want the bottom-up allocation just near the kernel
image so it is highly likely that the allocated memory and the kernel
will reside in the same node.

If bottom-up allocation failed, will try to allocate memory top-down.

.. _`memblock_find_in_range_node.return`:

Return
------

Found address on success, 0 on failure.

.. _`memblock_find_in_range`:

memblock_find_in_range
======================

.. c:function:: phys_addr_t __init_memblock memblock_find_in_range(phys_addr_t start, phys_addr_t end, phys_addr_t size, phys_addr_t align)

    find free area in given range

    :param start:
        start of candidate range
    :type start: phys_addr_t

    :param end:
        end of candidate range, can be \ ``MEMBLOCK_ALLOC_ANYWHERE``\  or
        \ ``MEMBLOCK_ALLOC_ACCESSIBLE``\ 
    :type end: phys_addr_t

    :param size:
        size of free area to find
    :type size: phys_addr_t

    :param align:
        alignment of free area to find
    :type align: phys_addr_t

.. _`memblock_find_in_range.description`:

Description
-----------

Find \ ``size``\  free area aligned to \ ``align``\  in the specified range.

.. _`memblock_find_in_range.return`:

Return
------

Found address on success, 0 on failure.

.. _`memblock_discard`:

memblock_discard
================

.. c:function:: void memblock_discard( void)

    discard memory and reserved arrays if they were allocated

    :param void:
        no arguments
    :type void: 

.. _`memblock_double_array`:

memblock_double_array
=====================

.. c:function:: int __init_memblock memblock_double_array(struct memblock_type *type, phys_addr_t new_area_start, phys_addr_t new_area_size)

    double the size of the memblock regions array

    :param type:
        memblock type of the regions array being doubled
    :type type: struct memblock_type \*

    :param new_area_start:
        starting address of memory range to avoid overlap with
    :type new_area_start: phys_addr_t

    :param new_area_size:
        size of memory range to avoid overlap with
    :type new_area_size: phys_addr_t

.. _`memblock_double_array.description`:

Description
-----------

Double the size of the \ ``type``\  regions array. If memblock is being used to
allocate memory for a new reserved regions array and there is a previously
allocated memory range [@new_area_start, \ ``new_area_start``\  + \ ``new_area_size``\ ]
waiting to be reserved, ensure the memory used by the new array does
not overlap.

.. _`memblock_double_array.return`:

Return
------

0 on success, -1 on failure.

.. _`memblock_merge_regions`:

memblock_merge_regions
======================

.. c:function:: void __init_memblock memblock_merge_regions(struct memblock_type *type)

    merge neighboring compatible regions

    :param type:
        memblock type to scan
    :type type: struct memblock_type \*

.. _`memblock_merge_regions.description`:

Description
-----------

Scan \ ``type``\  and merge neighboring compatible regions.

.. _`memblock_insert_region`:

memblock_insert_region
======================

.. c:function:: void __init_memblock memblock_insert_region(struct memblock_type *type, int idx, phys_addr_t base, phys_addr_t size, int nid, enum memblock_flags flags)

    insert new memblock region

    :param type:
        memblock type to insert into
    :type type: struct memblock_type \*

    :param idx:
        index for the insertion point
    :type idx: int

    :param base:
        base address of the new region
    :type base: phys_addr_t

    :param size:
        size of the new region
    :type size: phys_addr_t

    :param nid:
        node id of the new region
    :type nid: int

    :param flags:
        flags of the new region
    :type flags: enum memblock_flags

.. _`memblock_insert_region.description`:

Description
-----------

Insert new memblock region [@base, \ ``base``\  + \ ``size``\ ) into \ ``type``\  at \ ``idx``\ .
\ ``type``\  must already have extra room to accommodate the new region.

.. _`memblock_add_range`:

memblock_add_range
==================

.. c:function:: int __init_memblock memblock_add_range(struct memblock_type *type, phys_addr_t base, phys_addr_t size, int nid, enum memblock_flags flags)

    add new memblock region

    :param type:
        memblock type to add new region into
    :type type: struct memblock_type \*

    :param base:
        base address of the new region
    :type base: phys_addr_t

    :param size:
        size of the new region
    :type size: phys_addr_t

    :param nid:
        nid of the new region
    :type nid: int

    :param flags:
        flags of the new region
    :type flags: enum memblock_flags

.. _`memblock_add_range.description`:

Description
-----------

Add new memblock region [@base, \ ``base``\  + \ ``size``\ ) into \ ``type``\ .  The new region
is allowed to overlap with existing ones - overlaps don't affect already
existing regions.  \ ``type``\  is guaranteed to be minimal (all neighbouring
compatible regions are merged) after the addition.

.. _`memblock_add_range.return`:

Return
------

0 on success, -errno on failure.

.. _`memblock_add_node`:

memblock_add_node
=================

.. c:function:: int __init_memblock memblock_add_node(phys_addr_t base, phys_addr_t size, int nid)

    add new memblock region within a NUMA node

    :param base:
        base address of the new region
    :type base: phys_addr_t

    :param size:
        size of the new region
    :type size: phys_addr_t

    :param nid:
        nid of the new region
    :type nid: int

.. _`memblock_add_node.description`:

Description
-----------

Add new memblock region [@base, \ ``base``\  + \ ``size``\ ) to the "memory"
type. See \ :c:func:`memblock_add_range`\  description for mode details

.. _`memblock_add_node.return`:

Return
------

0 on success, -errno on failure.

.. _`memblock_add`:

memblock_add
============

.. c:function:: int __init_memblock memblock_add(phys_addr_t base, phys_addr_t size)

    add new memblock region

    :param base:
        base address of the new region
    :type base: phys_addr_t

    :param size:
        size of the new region
    :type size: phys_addr_t

.. _`memblock_add.description`:

Description
-----------

Add new memblock region [@base, \ ``base``\  + \ ``size``\ ) to the "memory"
type. See \ :c:func:`memblock_add_range`\  description for mode details

.. _`memblock_add.return`:

Return
------

0 on success, -errno on failure.

.. _`memblock_isolate_range`:

memblock_isolate_range
======================

.. c:function:: int __init_memblock memblock_isolate_range(struct memblock_type *type, phys_addr_t base, phys_addr_t size, int *start_rgn, int *end_rgn)

    isolate given range into disjoint memblocks

    :param type:
        memblock type to isolate range for
    :type type: struct memblock_type \*

    :param base:
        base of range to isolate
    :type base: phys_addr_t

    :param size:
        size of range to isolate
    :type size: phys_addr_t

    :param start_rgn:
        out parameter for the start of isolated region
    :type start_rgn: int \*

    :param end_rgn:
        out parameter for the end of isolated region
    :type end_rgn: int \*

.. _`memblock_isolate_range.description`:

Description
-----------

Walk \ ``type``\  and ensure that regions don't cross the boundaries defined by
[@base, \ ``base``\  + \ ``size``\ ).  Crossing regions are split at the boundaries,
which may create at most two more regions.  The index of the first
region inside the range is returned in *@start_rgn and end in *@end_rgn.

.. _`memblock_isolate_range.return`:

Return
------

0 on success, -errno on failure.

.. _`memblock_setclr_flag`:

memblock_setclr_flag
====================

.. c:function:: int __init_memblock memblock_setclr_flag(phys_addr_t base, phys_addr_t size, int set, int flag)

    set or clear flag for a memory region

    :param base:
        base address of the region
    :type base: phys_addr_t

    :param size:
        size of the region
    :type size: phys_addr_t

    :param set:
        set or clear the flag
    :type set: int

    :param flag:
        the flag to udpate
    :type flag: int

.. _`memblock_setclr_flag.description`:

Description
-----------

This function isolates region [@base, \ ``base``\  + \ ``size``\ ), and sets/clears flag

.. _`memblock_setclr_flag.return`:

Return
------

0 on success, -errno on failure.

.. _`memblock_mark_hotplug`:

memblock_mark_hotplug
=====================

.. c:function:: int __init_memblock memblock_mark_hotplug(phys_addr_t base, phys_addr_t size)

    Mark hotpluggable memory with flag MEMBLOCK_HOTPLUG.

    :param base:
        the base phys addr of the region
    :type base: phys_addr_t

    :param size:
        the size of the region
    :type size: phys_addr_t

.. _`memblock_mark_hotplug.return`:

Return
------

0 on success, -errno on failure.

.. _`memblock_clear_hotplug`:

memblock_clear_hotplug
======================

.. c:function:: int __init_memblock memblock_clear_hotplug(phys_addr_t base, phys_addr_t size)

    Clear flag MEMBLOCK_HOTPLUG for a specified region.

    :param base:
        the base phys addr of the region
    :type base: phys_addr_t

    :param size:
        the size of the region
    :type size: phys_addr_t

.. _`memblock_clear_hotplug.return`:

Return
------

0 on success, -errno on failure.

.. _`memblock_mark_mirror`:

memblock_mark_mirror
====================

.. c:function:: int __init_memblock memblock_mark_mirror(phys_addr_t base, phys_addr_t size)

    Mark mirrored memory with flag MEMBLOCK_MIRROR.

    :param base:
        the base phys addr of the region
    :type base: phys_addr_t

    :param size:
        the size of the region
    :type size: phys_addr_t

.. _`memblock_mark_mirror.return`:

Return
------

0 on success, -errno on failure.

.. _`memblock_mark_nomap`:

memblock_mark_nomap
===================

.. c:function:: int __init_memblock memblock_mark_nomap(phys_addr_t base, phys_addr_t size)

    Mark a memory region with flag MEMBLOCK_NOMAP.

    :param base:
        the base phys addr of the region
    :type base: phys_addr_t

    :param size:
        the size of the region
    :type size: phys_addr_t

.. _`memblock_mark_nomap.return`:

Return
------

0 on success, -errno on failure.

.. _`memblock_clear_nomap`:

memblock_clear_nomap
====================

.. c:function:: int __init_memblock memblock_clear_nomap(phys_addr_t base, phys_addr_t size)

    Clear flag MEMBLOCK_NOMAP for a specified region.

    :param base:
        the base phys addr of the region
    :type base: phys_addr_t

    :param size:
        the size of the region
    :type size: phys_addr_t

.. _`memblock_clear_nomap.return`:

Return
------

0 on success, -errno on failure.

.. _`__next_reserved_mem_region`:

__next_reserved_mem_region
==========================

.. c:function:: void __init_memblock __next_reserved_mem_region(u64 *idx, phys_addr_t *out_start, phys_addr_t *out_end)

    next function for \ :c:func:`for_each_reserved_region`\ 

    :param idx:
        pointer to u64 loop variable
    :type idx: u64 \*

    :param out_start:
        ptr to phys_addr_t for start address of the region, can be \ ``NULL``\ 
    :type out_start: phys_addr_t \*

    :param out_end:
        ptr to phys_addr_t for end address of the region, can be \ ``NULL``\ 
    :type out_end: phys_addr_t \*

.. _`__next_reserved_mem_region.description`:

Description
-----------

Iterate over all reserved memory regions.

.. _`__next_mem_range`:

__next_mem_range
================

.. c:function:: void __init_memblock __next_mem_range(u64 *idx, int nid, enum memblock_flags flags, struct memblock_type *type_a, struct memblock_type *type_b, phys_addr_t *out_start, phys_addr_t *out_end, int *out_nid)

    next function for \ :c:func:`for_each_free_mem_range`\  etc.

    :param idx:
        pointer to u64 loop variable
    :type idx: u64 \*

    :param nid:
        node selector, \ ``NUMA_NO_NODE``\  for all nodes
    :type nid: int

    :param flags:
        pick from blocks based on memory attributes
    :type flags: enum memblock_flags

    :param type_a:
        pointer to memblock_type from where the range is taken
    :type type_a: struct memblock_type \*

    :param type_b:
        pointer to memblock_type which excludes memory from being taken
    :type type_b: struct memblock_type \*

    :param out_start:
        ptr to phys_addr_t for start address of the range, can be \ ``NULL``\ 
    :type out_start: phys_addr_t \*

    :param out_end:
        ptr to phys_addr_t for end address of the range, can be \ ``NULL``\ 
    :type out_end: phys_addr_t \*

    :param out_nid:
        ptr to int for nid of the range, can be \ ``NULL``\ 
    :type out_nid: int \*

.. _`__next_mem_range.description`:

Description
-----------

Find the first area from *@idx which matches \ ``nid``\ , fill the out
parameters, and update *@idx for the next iteration.  The lower 32bit of
*@idx contains index into type_a and the upper 32bit indexes the
areas before each region in type_b.  For example, if type_b regions
look like the following,

     0:[0-16), 1:[32-48), 2:[128-130)

The upper 32bit indexes the following regions.

     0:[0-0), 1:[16-32), 2:[48-128), 3:[130-MAX)

As both region arrays are sorted, the function advances the two indices
in lockstep and returns each intersection.

.. _`__next_mem_range_rev`:

__next_mem_range_rev
====================

.. c:function:: void __init_memblock __next_mem_range_rev(u64 *idx, int nid, enum memblock_flags flags, struct memblock_type *type_a, struct memblock_type *type_b, phys_addr_t *out_start, phys_addr_t *out_end, int *out_nid)

    generic next function for for_each_*_range_rev()

    :param idx:
        pointer to u64 loop variable
    :type idx: u64 \*

    :param nid:
        node selector, \ ``NUMA_NO_NODE``\  for all nodes
    :type nid: int

    :param flags:
        pick from blocks based on memory attributes
    :type flags: enum memblock_flags

    :param type_a:
        pointer to memblock_type from where the range is taken
    :type type_a: struct memblock_type \*

    :param type_b:
        pointer to memblock_type which excludes memory from being taken
    :type type_b: struct memblock_type \*

    :param out_start:
        ptr to phys_addr_t for start address of the range, can be \ ``NULL``\ 
    :type out_start: phys_addr_t \*

    :param out_end:
        ptr to phys_addr_t for end address of the range, can be \ ``NULL``\ 
    :type out_end: phys_addr_t \*

    :param out_nid:
        ptr to int for nid of the range, can be \ ``NULL``\ 
    :type out_nid: int \*

.. _`__next_mem_range_rev.description`:

Description
-----------

Finds the next range from type_a which is not marked as unsuitable
in type_b.

Reverse of \ :c:func:`__next_mem_range`\ .

.. _`memblock_set_node`:

memblock_set_node
=================

.. c:function:: int __init_memblock memblock_set_node(phys_addr_t base, phys_addr_t size, struct memblock_type *type, int nid)

    set node ID on memblock regions

    :param base:
        base of area to set node ID for
    :type base: phys_addr_t

    :param size:
        size of area to set node ID for
    :type size: phys_addr_t

    :param type:
        memblock type to set node ID for
    :type type: struct memblock_type \*

    :param nid:
        node ID to set
    :type nid: int

.. _`memblock_set_node.description`:

Description
-----------

Set the nid of memblock \ ``type``\  regions in [@base, \ ``base``\  + \ ``size``\ ) to \ ``nid``\ .
Regions which cross the area boundaries are split as necessary.

.. _`memblock_set_node.return`:

Return
------

0 on success, -errno on failure.

.. _`memblock_alloc_internal`:

memblock_alloc_internal
=======================

.. c:function:: void *memblock_alloc_internal(phys_addr_t size, phys_addr_t align, phys_addr_t min_addr, phys_addr_t max_addr, int nid)

    allocate boot memory block

    :param size:
        size of memory block to be allocated in bytes
    :type size: phys_addr_t

    :param align:
        alignment of the region and block's size
    :type align: phys_addr_t

    :param min_addr:
        the lower bound of the memory region to allocate (phys address)
    :type min_addr: phys_addr_t

    :param max_addr:
        the upper bound of the memory region to allocate (phys address)
    :type max_addr: phys_addr_t

    :param nid:
        nid of the free area to find, \ ``NUMA_NO_NODE``\  for any node
    :type nid: int

.. _`memblock_alloc_internal.description`:

Description
-----------

The \ ``min_addr``\  limit is dropped if it can not be satisfied and the allocation
will fall back to memory below \ ``min_addr``\ . Also, allocation may fall back
to any node in the system if the specified node can not
hold the requested memory.

The allocation is performed from memory region limited by
memblock.current_limit if \ ``max_addr``\  == \ ``MEMBLOCK_ALLOC_ACCESSIBLE``\ .

The phys address of allocated boot memory block is converted to virtual and
allocated memory is reset to 0.

In addition, function sets the min_count to 0 using kmemleak_alloc for
allocated boot memory block, so that it is never reported as leaks.

.. _`memblock_alloc_internal.return`:

Return
------

Virtual address of allocated memory block on success, NULL on failure.

.. _`memblock_alloc_try_nid_raw`:

memblock_alloc_try_nid_raw
==========================

.. c:function:: void *memblock_alloc_try_nid_raw(phys_addr_t size, phys_addr_t align, phys_addr_t min_addr, phys_addr_t max_addr, int nid)

    allocate boot memory block without zeroing memory and without panicking

    :param size:
        size of memory block to be allocated in bytes
    :type size: phys_addr_t

    :param align:
        alignment of the region and block's size
    :type align: phys_addr_t

    :param min_addr:
        the lower bound of the memory region from where the allocation
        is preferred (phys address)
    :type min_addr: phys_addr_t

    :param max_addr:
        the upper bound of the memory region from where the allocation
        is preferred (phys address), or \ ``MEMBLOCK_ALLOC_ACCESSIBLE``\  to
        allocate only from memory limited by memblock.current_limit value
    :type max_addr: phys_addr_t

    :param nid:
        nid of the free area to find, \ ``NUMA_NO_NODE``\  for any node
    :type nid: int

.. _`memblock_alloc_try_nid_raw.description`:

Description
-----------

Public function, provides additional debug information (including caller
info), if enabled. Does not zero allocated memory, does not panic if request
cannot be satisfied.

.. _`memblock_alloc_try_nid_raw.return`:

Return
------

Virtual address of allocated memory block on success, NULL on failure.

.. _`memblock_alloc_try_nid_nopanic`:

memblock_alloc_try_nid_nopanic
==============================

.. c:function:: void *memblock_alloc_try_nid_nopanic(phys_addr_t size, phys_addr_t align, phys_addr_t min_addr, phys_addr_t max_addr, int nid)

    allocate boot memory block

    :param size:
        size of memory block to be allocated in bytes
    :type size: phys_addr_t

    :param align:
        alignment of the region and block's size
    :type align: phys_addr_t

    :param min_addr:
        the lower bound of the memory region from where the allocation
        is preferred (phys address)
    :type min_addr: phys_addr_t

    :param max_addr:
        the upper bound of the memory region from where the allocation
        is preferred (phys address), or \ ``MEMBLOCK_ALLOC_ACCESSIBLE``\  to
        allocate only from memory limited by memblock.current_limit value
    :type max_addr: phys_addr_t

    :param nid:
        nid of the free area to find, \ ``NUMA_NO_NODE``\  for any node
    :type nid: int

.. _`memblock_alloc_try_nid_nopanic.description`:

Description
-----------

Public function, provides additional debug information (including caller
info), if enabled. This function zeroes the allocated memory.

.. _`memblock_alloc_try_nid_nopanic.return`:

Return
------

Virtual address of allocated memory block on success, NULL on failure.

.. _`memblock_alloc_try_nid`:

memblock_alloc_try_nid
======================

.. c:function:: void *memblock_alloc_try_nid(phys_addr_t size, phys_addr_t align, phys_addr_t min_addr, phys_addr_t max_addr, int nid)

    allocate boot memory block with panicking

    :param size:
        size of memory block to be allocated in bytes
    :type size: phys_addr_t

    :param align:
        alignment of the region and block's size
    :type align: phys_addr_t

    :param min_addr:
        the lower bound of the memory region from where the allocation
        is preferred (phys address)
    :type min_addr: phys_addr_t

    :param max_addr:
        the upper bound of the memory region from where the allocation
        is preferred (phys address), or \ ``MEMBLOCK_ALLOC_ACCESSIBLE``\  to
        allocate only from memory limited by memblock.current_limit value
    :type max_addr: phys_addr_t

    :param nid:
        nid of the free area to find, \ ``NUMA_NO_NODE``\  for any node
    :type nid: int

.. _`memblock_alloc_try_nid.description`:

Description
-----------

Public panicking version of \ :c:func:`memblock_alloc_try_nid_nopanic`\ 
which provides debug information (including caller info), if enabled,
and panics if the request can not be satisfied.

.. _`memblock_alloc_try_nid.return`:

Return
------

Virtual address of allocated memory block on success, NULL on failure.

.. _`__memblock_free_early`:

__memblock_free_early
=====================

.. c:function:: void __memblock_free_early(phys_addr_t base, phys_addr_t size)

    free boot memory block

    :param base:
        phys starting address of the  boot memory block
    :type base: phys_addr_t

    :param size:
        size of the boot memory block in bytes
    :type size: phys_addr_t

.. _`__memblock_free_early.description`:

Description
-----------

Free boot memory block previously allocated by \ :c:func:`memblock_alloc_xx`\  API.
The freeing memory will not be released to the buddy allocator.

.. _`__memblock_free_late`:

__memblock_free_late
====================

.. c:function:: void __memblock_free_late(phys_addr_t base, phys_addr_t size)

    free bootmem block pages directly to buddy allocator

    :param base:
        phys starting address of the  boot memory block
    :type base: phys_addr_t

    :param size:
        size of the boot memory block in bytes
    :type size: phys_addr_t

.. _`__memblock_free_late.description`:

Description
-----------

This is only useful when the bootmem allocator has already been torn
down, but we are still initializing the system.  Pages are released directly
to the buddy allocator, no bootmem metadata is updated because it is gone.

.. _`memblock_is_region_memory`:

memblock_is_region_memory
=========================

.. c:function:: bool __init_memblock memblock_is_region_memory(phys_addr_t base, phys_addr_t size)

    check if a region is a subset of memory

    :param base:
        base of region to check
    :type base: phys_addr_t

    :param size:
        size of region to check
    :type size: phys_addr_t

.. _`memblock_is_region_memory.description`:

Description
-----------

Check if the region [@base, \ ``base``\  + \ ``size``\ ) is a subset of a memory block.

.. _`memblock_is_region_memory.return`:

Return
------

0 if false, non-zero if true

.. _`memblock_is_region_reserved`:

memblock_is_region_reserved
===========================

.. c:function:: bool __init_memblock memblock_is_region_reserved(phys_addr_t base, phys_addr_t size)

    check if a region intersects reserved memory

    :param base:
        base of region to check
    :type base: phys_addr_t

    :param size:
        size of region to check
    :type size: phys_addr_t

.. _`memblock_is_region_reserved.description`:

Description
-----------

Check if the region [@base, \ ``base``\  + \ ``size``\ ) intersects a reserved
memory block.

.. _`memblock_is_region_reserved.return`:

Return
------

True if they intersect, false if not.

.. _`memblock_free_all`:

memblock_free_all
=================

.. c:function:: unsigned long memblock_free_all( void)

    release free pages to the buddy allocator

    :param void:
        no arguments
    :type void: 

.. _`memblock_free_all.return`:

Return
------

the number of pages actually released.

.. This file was automatic generated / don't edit.

