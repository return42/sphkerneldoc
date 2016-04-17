.. -*- coding: utf-8; mode: rst -*-

==========
memblock.h
==========


.. _`for_each_mem_range`:

for_each_mem_range
==================

.. c:function:: for_each_mem_range ( i,  type_a,  type_b,  nid,  flags,  p_start,  p_end,  p_nid)

    iterate through memblock areas from type_a and not included in type_b. Or just type_a if type_b is NULL.

    :param i:
        u64 used as loop variable

    :param type_a:
        ptr to memblock_type to iterate

    :param type_b:
        ptr to memblock_type which excludes from the iteration

    :param nid:
        node selector, ``NUMA_NO_NODE`` for all nodes

    :param flags:
        pick from blocks based on memory attributes

    :param p_start:
        ptr to phys_addr_t for start address of the range, can be ``NULL``

    :param p_end:
        ptr to phys_addr_t for end address of the range, can be ``NULL``

    :param p_nid:
        ptr to int for nid of the range, can be ``NULL``



.. _`for_each_mem_range_rev`:

for_each_mem_range_rev
======================

.. c:function:: for_each_mem_range_rev ( i,  type_a,  type_b,  nid,  flags,  p_start,  p_end,  p_nid)

    reverse iterate through memblock areas from type_a and not included in type_b. Or just type_a if type_b is NULL.

    :param i:
        u64 used as loop variable

    :param type_a:
        ptr to memblock_type to iterate

    :param type_b:
        ptr to memblock_type which excludes from the iteration

    :param nid:
        node selector, ``NUMA_NO_NODE`` for all nodes

    :param flags:
        pick from blocks based on memory attributes

    :param p_start:
        ptr to phys_addr_t for start address of the range, can be ``NULL``

    :param p_end:
        ptr to phys_addr_t for end address of the range, can be ``NULL``

    :param p_nid:
        ptr to int for nid of the range, can be ``NULL``



.. _`for_each_reserved_mem_region`:

for_each_reserved_mem_region
============================

.. c:function:: for_each_reserved_mem_region ( i,  p_start,  p_end)

    iterate over all reserved memblock areas

    :param i:
        u64 used as loop variable

    :param p_start:
        ptr to phys_addr_t for start address of the range, can be ``NULL``

    :param p_end:
        ptr to phys_addr_t for end address of the range, can be ``NULL``



.. _`for_each_reserved_mem_region.description`:

Description
-----------

Walks over reserved areas of memblock. Available as soon as memblock
is initialized.



.. _`for_each_mem_pfn_range`:

for_each_mem_pfn_range
======================

.. c:function:: for_each_mem_pfn_range ( i,  nid,  p_start,  p_end,  p_nid)

    early memory pfn range iterator

    :param i:
        an integer used as loop variable

    :param nid:
        node selector, ``MAX_NUMNODES`` for all nodes

    :param p_start:
        ptr to ulong for start pfn of the range, can be ``NULL``

    :param p_end:
        ptr to ulong for end pfn of the range, can be ``NULL``

    :param p_nid:
        ptr to int for nid of the range, can be ``NULL``



.. _`for_each_mem_pfn_range.description`:

Description
-----------

Walks over configured memory ranges.



.. _`for_each_free_mem_range`:

for_each_free_mem_range
=======================

.. c:function:: for_each_free_mem_range ( i,  nid,  flags,  p_start,  p_end,  p_nid)

    iterate through free memblock areas

    :param i:
        u64 used as loop variable

    :param nid:
        node selector, ``NUMA_NO_NODE`` for all nodes

    :param flags:
        pick from blocks based on memory attributes

    :param p_start:
        ptr to phys_addr_t for start address of the range, can be ``NULL``

    :param p_end:
        ptr to phys_addr_t for end address of the range, can be ``NULL``

    :param p_nid:
        ptr to int for nid of the range, can be ``NULL``



.. _`for_each_free_mem_range.description`:

Description
-----------

Walks over free (memory && !reserved) areas of memblock.  Available as
soon as memblock is initialized.



.. _`for_each_free_mem_range_reverse`:

for_each_free_mem_range_reverse
===============================

.. c:function:: for_each_free_mem_range_reverse ( i,  nid,  flags,  p_start,  p_end,  p_nid)

    rev-iterate through free memblock areas

    :param i:
        u64 used as loop variable

    :param nid:
        node selector, ``NUMA_NO_NODE`` for all nodes

    :param flags:
        pick from blocks based on memory attributes

    :param p_start:
        ptr to phys_addr_t for start address of the range, can be ``NULL``

    :param p_end:
        ptr to phys_addr_t for end address of the range, can be ``NULL``

    :param p_nid:
        ptr to int for nid of the range, can be ``NULL``



.. _`for_each_free_mem_range_reverse.description`:

Description
-----------

Walks over free (memory && !reserved) areas of memblock in reverse
order.  Available as soon as memblock is initialized.



.. _`memblock_set_current_limit`:

memblock_set_current_limit
==========================

.. c:function:: void memblock_set_current_limit (phys_addr_t limit)

    Set the current allocation limit to allow limiting allocations to what is currently accessible during boot

    :param phys_addr_t limit:
        New limit value (physical address)



.. _`memblock_region_memory_base_pfn`:

memblock_region_memory_base_pfn
===============================

.. c:function:: unsigned long memblock_region_memory_base_pfn (const struct memblock_region *reg)

    Return the lowest pfn intersecting with the memory region

    :param const struct memblock_region \*reg:
        memblock_region structure



.. _`memblock_region_memory_end_pfn`:

memblock_region_memory_end_pfn
==============================

.. c:function:: unsigned long memblock_region_memory_end_pfn (const struct memblock_region *reg)

    Return the end_pfn this region

    :param const struct memblock_region \*reg:
        memblock_region structure



.. _`memblock_region_reserved_base_pfn`:

memblock_region_reserved_base_pfn
=================================

.. c:function:: unsigned long memblock_region_reserved_base_pfn (const struct memblock_region *reg)

    Return the lowest pfn intersecting with the reserved region

    :param const struct memblock_region \*reg:
        memblock_region structure



.. _`memblock_region_reserved_end_pfn`:

memblock_region_reserved_end_pfn
================================

.. c:function:: unsigned long memblock_region_reserved_end_pfn (const struct memblock_region *reg)

    Return the end_pfn this region

    :param const struct memblock_region \*reg:
        memblock_region structure

