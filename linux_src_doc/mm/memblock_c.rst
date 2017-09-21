.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/memblock.c

.. _`__memblock_find_range_top_down`:

__memblock_find_range_top_down
==============================

.. c:function:: phys_addr_t __init_memblock __memblock_find_range_top_down(phys_addr_t start, phys_addr_t end, phys_addr_t size, phys_addr_t align, int nid, ulong flags)

    find free area utility, in top-down

    :param phys_addr_t start:
        start of candidate range

    :param phys_addr_t end:
        end of candidate range, can be \ ``MEMBLOCK_ALLOC_``\ {ANYWHERE\|ACCESSIBLE}

    :param phys_addr_t size:
        size of free area to find

    :param phys_addr_t align:
        alignment of free area to find

    :param int nid:
        nid of the free area to find, \ ``NUMA_NO_NODE``\  for any node

    :param ulong flags:
        pick from blocks based on memory attributes

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

.. c:function:: phys_addr_t __init_memblock memblock_find_in_range_node(phys_addr_t size, phys_addr_t align, phys_addr_t start, phys_addr_t end, int nid, ulong flags)

    find free area in given range and node

    :param phys_addr_t size:
        size of free area to find

    :param phys_addr_t align:
        alignment of free area to find

    :param phys_addr_t start:
        start of candidate range

    :param phys_addr_t end:
        end of candidate range, can be \ ``MEMBLOCK_ALLOC_``\ {ANYWHERE\|ACCESSIBLE}

    :param int nid:
        nid of the free area to find, \ ``NUMA_NO_NODE``\  for any node

    :param ulong flags:
        pick from blocks based on memory attributes

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

    :param phys_addr_t start:
        start of candidate range

    :param phys_addr_t end:
        end of candidate range, can be \ ``MEMBLOCK_ALLOC_``\ {ANYWHERE\|ACCESSIBLE}

    :param phys_addr_t size:
        size of free area to find

    :param phys_addr_t align:
        alignment of free area to find

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

    :param  void:
        no arguments

.. _`memblock_double_array`:

memblock_double_array
=====================

.. c:function:: int __init_memblock memblock_double_array(struct memblock_type *type, phys_addr_t new_area_start, phys_addr_t new_area_size)

    double the size of the memblock regions array

    :param struct memblock_type \*type:
        memblock type of the regions array being doubled

    :param phys_addr_t new_area_start:
        starting address of memory range to avoid overlap with

    :param phys_addr_t new_area_size:
        size of memory range to avoid overlap with

.. _`memblock_double_array.description`:

Description
-----------

Double the size of the \ ``type``\  regions array. If memblock is being used to
allocate memory for a new reserved regions array and there is a previously
allocated memory range [@new_area_start,@new_area_start+@new_area_size]
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

    :param struct memblock_type \*type:
        memblock type to scan

.. _`memblock_merge_regions.description`:

Description
-----------

Scan \ ``type``\  and merge neighboring compatible regions.

.. _`memblock_insert_region`:

memblock_insert_region
======================

.. c:function:: void __init_memblock memblock_insert_region(struct memblock_type *type, int idx, phys_addr_t base, phys_addr_t size, int nid, unsigned long flags)

    insert new memblock region

    :param struct memblock_type \*type:
        memblock type to insert into

    :param int idx:
        index for the insertion point

    :param phys_addr_t base:
        base address of the new region

    :param phys_addr_t size:
        size of the new region

    :param int nid:
        node id of the new region

    :param unsigned long flags:
        flags of the new region

.. _`memblock_insert_region.description`:

Description
-----------

Insert new memblock region [@base,@base+@size) into \ ``type``\  at \ ``idx``\ .
\ ``type``\  must already have extra room to accommodate the new region.

.. _`memblock_add_range`:

memblock_add_range
==================

.. c:function:: int __init_memblock memblock_add_range(struct memblock_type *type, phys_addr_t base, phys_addr_t size, int nid, unsigned long flags)

    add new memblock region

    :param struct memblock_type \*type:
        memblock type to add new region into

    :param phys_addr_t base:
        base address of the new region

    :param phys_addr_t size:
        size of the new region

    :param int nid:
        nid of the new region

    :param unsigned long flags:
        flags of the new region

.. _`memblock_add_range.description`:

Description
-----------

Add new memblock region [@base,@base+@size) into \ ``type``\ .  The new region
is allowed to overlap with existing ones - overlaps don't affect already
existing regions.  \ ``type``\  is guaranteed to be minimal (all neighbouring
compatible regions are merged) after the addition.

.. _`memblock_add_range.return`:

Return
------

0 on success, -errno on failure.

.. _`memblock_isolate_range`:

memblock_isolate_range
======================

.. c:function:: int __init_memblock memblock_isolate_range(struct memblock_type *type, phys_addr_t base, phys_addr_t size, int *start_rgn, int *end_rgn)

    isolate given range into disjoint memblocks

    :param struct memblock_type \*type:
        memblock type to isolate range for

    :param phys_addr_t base:
        base of range to isolate

    :param phys_addr_t size:
        size of range to isolate

    :param int \*start_rgn:
        out parameter for the start of isolated region

    :param int \*end_rgn:
        out parameter for the end of isolated region

.. _`memblock_isolate_range.description`:

Description
-----------

Walk \ ``type``\  and ensure that regions don't cross the boundaries defined by
[@base,@base+@size).  Crossing regions are split at the boundaries,
which may create at most two more regions.  The index of the first
region inside the range is returned in \*@start_rgn and end in \*@end_rgn.

.. _`memblock_isolate_range.return`:

Return
------

0 on success, -errno on failure.

.. _`memblock_mark_hotplug`:

memblock_mark_hotplug
=====================

.. c:function:: int __init_memblock memblock_mark_hotplug(phys_addr_t base, phys_addr_t size)

    Mark hotpluggable memory with flag MEMBLOCK_HOTPLUG.

    :param phys_addr_t base:
        the base phys addr of the region

    :param phys_addr_t size:
        the size of the region

.. _`memblock_mark_hotplug.description`:

Description
-----------

Return 0 on success, -errno on failure.

.. _`memblock_clear_hotplug`:

memblock_clear_hotplug
======================

.. c:function:: int __init_memblock memblock_clear_hotplug(phys_addr_t base, phys_addr_t size)

    Clear flag MEMBLOCK_HOTPLUG for a specified region.

    :param phys_addr_t base:
        the base phys addr of the region

    :param phys_addr_t size:
        the size of the region

.. _`memblock_clear_hotplug.description`:

Description
-----------

Return 0 on success, -errno on failure.

.. _`memblock_mark_mirror`:

memblock_mark_mirror
====================

.. c:function:: int __init_memblock memblock_mark_mirror(phys_addr_t base, phys_addr_t size)

    Mark mirrored memory with flag MEMBLOCK_MIRROR.

    :param phys_addr_t base:
        the base phys addr of the region

    :param phys_addr_t size:
        the size of the region

.. _`memblock_mark_mirror.description`:

Description
-----------

Return 0 on success, -errno on failure.

.. _`memblock_mark_nomap`:

memblock_mark_nomap
===================

.. c:function:: int __init_memblock memblock_mark_nomap(phys_addr_t base, phys_addr_t size)

    Mark a memory region with flag MEMBLOCK_NOMAP.

    :param phys_addr_t base:
        the base phys addr of the region

    :param phys_addr_t size:
        the size of the region

.. _`memblock_mark_nomap.description`:

Description
-----------

Return 0 on success, -errno on failure.

.. _`memblock_clear_nomap`:

memblock_clear_nomap
====================

.. c:function:: int __init_memblock memblock_clear_nomap(phys_addr_t base, phys_addr_t size)

    Clear flag MEMBLOCK_NOMAP for a specified region.

    :param phys_addr_t base:
        the base phys addr of the region

    :param phys_addr_t size:
        the size of the region

.. _`memblock_clear_nomap.description`:

Description
-----------

Return 0 on success, -errno on failure.

.. _`__next_reserved_mem_region`:

__next_reserved_mem_region
==========================

.. c:function:: void __init_memblock __next_reserved_mem_region(u64 *idx, phys_addr_t *out_start, phys_addr_t *out_end)

    next function for \ :c:func:`for_each_reserved_region`\ 

    :param u64 \*idx:
        pointer to u64 loop variable

    :param phys_addr_t \*out_start:
        ptr to phys_addr_t for start address of the region, can be \ ``NULL``\ 

    :param phys_addr_t \*out_end:
        ptr to phys_addr_t for end address of the region, can be \ ``NULL``\ 

.. _`__next_reserved_mem_region.description`:

Description
-----------

Iterate over all reserved memory regions.

.. _`__next_mem_range`:

__next_mem_range
================

.. c:function:: void __init_memblock __next_mem_range(u64 *idx, int nid, ulong flags, struct memblock_type *type_a, struct memblock_type *type_b, phys_addr_t *out_start, phys_addr_t *out_end, int *out_nid)

    next function for \ :c:func:`for_each_free_mem_range`\  etc.

    :param u64 \*idx:
        pointer to u64 loop variable

    :param int nid:
        node selector, \ ``NUMA_NO_NODE``\  for all nodes

    :param ulong flags:
        pick from blocks based on memory attributes

    :param struct memblock_type \*type_a:
        pointer to memblock_type from where the range is taken

    :param struct memblock_type \*type_b:
        pointer to memblock_type which excludes memory from being taken

    :param phys_addr_t \*out_start:
        ptr to phys_addr_t for start address of the range, can be \ ``NULL``\ 

    :param phys_addr_t \*out_end:
        ptr to phys_addr_t for end address of the range, can be \ ``NULL``\ 

    :param int \*out_nid:
        ptr to int for nid of the range, can be \ ``NULL``\ 

.. _`__next_mem_range.description`:

Description
-----------

Find the first area from \*@idx which matches \ ``nid``\ , fill the out
parameters, and update \*@idx for the next iteration.  The lower 32bit of
\*@idx contains index into type_a and the upper 32bit indexes the
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

.. c:function:: void __init_memblock __next_mem_range_rev(u64 *idx, int nid, ulong flags, struct memblock_type *type_a, struct memblock_type *type_b, phys_addr_t *out_start, phys_addr_t *out_end, int *out_nid)

    generic next function for for_each\_\*\_range_rev()

    :param u64 \*idx:
        pointer to u64 loop variable

    :param int nid:
        node selector, \ ``NUMA_NO_NODE``\  for all nodes

    :param ulong flags:
        pick from blocks based on memory attributes

    :param struct memblock_type \*type_a:
        pointer to memblock_type from where the range is taken

    :param struct memblock_type \*type_b:
        pointer to memblock_type which excludes memory from being taken

    :param phys_addr_t \*out_start:
        ptr to phys_addr_t for start address of the range, can be \ ``NULL``\ 

    :param phys_addr_t \*out_end:
        ptr to phys_addr_t for end address of the range, can be \ ``NULL``\ 

    :param int \*out_nid:
        ptr to int for nid of the range, can be \ ``NULL``\ 

.. _`__next_mem_range_rev.description`:

Description
-----------

Finds the next range from type_a which is not marked as unsuitable
in type_b.

Reverse of \__next_mem_range().

.. _`memblock_set_node`:

memblock_set_node
=================

.. c:function:: int __init_memblock memblock_set_node(phys_addr_t base, phys_addr_t size, struct memblock_type *type, int nid)

    set node ID on memblock regions

    :param phys_addr_t base:
        base of area to set node ID for

    :param phys_addr_t size:
        size of area to set node ID for

    :param struct memblock_type \*type:
        memblock type to set node ID for

    :param int nid:
        node ID to set

.. _`memblock_set_node.description`:

Description
-----------

Set the nid of memblock \ ``type``\  regions in [@base,@base+@size) to \ ``nid``\ .
Regions which cross the area boundaries are split as necessary.

.. _`memblock_set_node.return`:

Return
------

0 on success, -errno on failure.

.. _`memblock_virt_alloc_internal`:

memblock_virt_alloc_internal
============================

.. c:function:: void *memblock_virt_alloc_internal(phys_addr_t size, phys_addr_t align, phys_addr_t min_addr, phys_addr_t max_addr, int nid)

    allocate boot memory block

    :param phys_addr_t size:
        size of memory block to be allocated in bytes

    :param phys_addr_t align:
        alignment of the region and block's size

    :param phys_addr_t min_addr:
        the lower bound of the memory region to allocate (phys address)

    :param phys_addr_t max_addr:
        the upper bound of the memory region to allocate (phys address)

    :param int nid:
        nid of the free area to find, \ ``NUMA_NO_NODE``\  for any node

.. _`memblock_virt_alloc_internal.description`:

Description
-----------

The \ ``min_addr``\  limit is dropped if it can not be satisfied and the allocation
will fall back to memory below \ ``min_addr``\ . Also, allocation may fall back
to any node in the system if the specified node can not
hold the requested memory.

The allocation is performed from memory region limited by
memblock.current_limit if \ ``max_addr``\  == \ ``BOOTMEM_ALLOC_ACCESSIBLE``\ .

The memory block is aligned on SMP_CACHE_BYTES if \ ``align``\  == 0.

The phys address of allocated boot memory block is converted to virtual and
allocated memory is reset to 0.

In addition, function sets the min_count to 0 using kmemleak_alloc for
allocated boot memory block, so that it is never reported as leaks.

.. _`memblock_virt_alloc_internal.return`:

Return
------

Virtual address of allocated memory block on success, NULL on failure.

.. _`memblock_virt_alloc_try_nid_nopanic`:

memblock_virt_alloc_try_nid_nopanic
===================================

.. c:function:: void *memblock_virt_alloc_try_nid_nopanic(phys_addr_t size, phys_addr_t align, phys_addr_t min_addr, phys_addr_t max_addr, int nid)

    allocate boot memory block

    :param phys_addr_t size:
        size of memory block to be allocated in bytes

    :param phys_addr_t align:
        alignment of the region and block's size

    :param phys_addr_t min_addr:
        the lower bound of the memory region from where the allocation
        is preferred (phys address)

    :param phys_addr_t max_addr:
        the upper bound of the memory region from where the allocation
        is preferred (phys address), or \ ``BOOTMEM_ALLOC_ACCESSIBLE``\  to
        allocate only from memory limited by memblock.current_limit value

    :param int nid:
        nid of the free area to find, \ ``NUMA_NO_NODE``\  for any node

.. _`memblock_virt_alloc_try_nid_nopanic.description`:

Description
-----------

Public version of \_memblock_virt_alloc_try_nid_nopanic() which provides
additional debug information (including caller info), if enabled.

.. _`memblock_virt_alloc_try_nid_nopanic.return`:

Return
------

Virtual address of allocated memory block on success, NULL on failure.

.. _`memblock_virt_alloc_try_nid`:

memblock_virt_alloc_try_nid
===========================

.. c:function:: void *memblock_virt_alloc_try_nid(phys_addr_t size, phys_addr_t align, phys_addr_t min_addr, phys_addr_t max_addr, int nid)

    allocate boot memory block with panicking

    :param phys_addr_t size:
        size of memory block to be allocated in bytes

    :param phys_addr_t align:
        alignment of the region and block's size

    :param phys_addr_t min_addr:
        the lower bound of the memory region from where the allocation
        is preferred (phys address)

    :param phys_addr_t max_addr:
        the upper bound of the memory region from where the allocation
        is preferred (phys address), or \ ``BOOTMEM_ALLOC_ACCESSIBLE``\  to
        allocate only from memory limited by memblock.current_limit value

    :param int nid:
        nid of the free area to find, \ ``NUMA_NO_NODE``\  for any node

.. _`memblock_virt_alloc_try_nid.description`:

Description
-----------

Public panicking version of \_memblock_virt_alloc_try_nid_nopanic()
which provides debug information (including caller info), if enabled,
and panics if the request can not be satisfied.

.. _`memblock_virt_alloc_try_nid.return`:

Return
------

Virtual address of allocated memory block on success, NULL on failure.

.. _`__memblock_free_early`:

__memblock_free_early
=====================

.. c:function:: void __memblock_free_early(phys_addr_t base, phys_addr_t size)

    free boot memory block

    :param phys_addr_t base:
        phys starting address of the  boot memory block

    :param phys_addr_t size:
        size of the boot memory block in bytes

.. _`__memblock_free_early.description`:

Description
-----------

Free boot memory block previously allocated by \ :c:func:`memblock_virt_alloc_xx`\  API.
The freeing memory will not be released to the buddy allocator.

.. _`memblock_is_region_memory`:

memblock_is_region_memory
=========================

.. c:function:: int __init_memblock memblock_is_region_memory(phys_addr_t base, phys_addr_t size)

    check if a region is a subset of memory

    :param phys_addr_t base:
        base of region to check

    :param phys_addr_t size:
        size of region to check

.. _`memblock_is_region_memory.description`:

Description
-----------

Check if the region [@base, \ ``base``\ +@size) is a subset of a memory block.

.. _`memblock_is_region_memory.return`:

Return
------

0 if false, non-zero if true

.. _`memblock_is_region_reserved`:

memblock_is_region_reserved
===========================

.. c:function:: bool __init_memblock memblock_is_region_reserved(phys_addr_t base, phys_addr_t size)

    check if a region intersects reserved memory

    :param phys_addr_t base:
        base of region to check

    :param phys_addr_t size:
        size of region to check

.. _`memblock_is_region_reserved.description`:

Description
-----------

Check if the region [@base, \ ``base``\ +@size) intersects a reserved memory block.

.. _`memblock_is_region_reserved.return`:

Return
------

True if they intersect, false if not.

.. This file was automatic generated / don't edit.

