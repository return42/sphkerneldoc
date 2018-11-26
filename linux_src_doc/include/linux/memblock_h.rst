.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/memblock.h

.. _`memblock_flags`:

enum memblock_flags
===================

.. c:type:: enum memblock_flags

    definition of memory region attributes

.. _`memblock_flags.definition`:

Definition
----------

.. code-block:: c

    enum memblock_flags {
        MEMBLOCK_NONE,
        MEMBLOCK_HOTPLUG,
        MEMBLOCK_MIRROR,
        MEMBLOCK_NOMAP
    };

.. _`memblock_flags.constants`:

Constants
---------

MEMBLOCK_NONE
    no special request

MEMBLOCK_HOTPLUG
    hotpluggable region

MEMBLOCK_MIRROR
    mirrored region

MEMBLOCK_NOMAP
    don't add to kernel direct mapping

.. _`memblock_region`:

struct memblock_region
======================

.. c:type:: struct memblock_region

    represents a memory region

.. _`memblock_region.definition`:

Definition
----------

.. code-block:: c

    struct memblock_region {
        phys_addr_t base;
        phys_addr_t size;
        enum memblock_flags flags;
    #ifdef CONFIG_HAVE_MEMBLOCK_NODE_MAP
        int nid;
    #endif
    }

.. _`memblock_region.members`:

Members
-------

base
    physical address of the region

size
    size of the region

flags
    memory region attributes

nid
    NUMA node id

.. _`memblock_type`:

struct memblock_type
====================

.. c:type:: struct memblock_type

    collection of memory regions of certain type

.. _`memblock_type.definition`:

Definition
----------

.. code-block:: c

    struct memblock_type {
        unsigned long cnt;
        unsigned long max;
        phys_addr_t total_size;
        struct memblock_region *regions;
        char *name;
    }

.. _`memblock_type.members`:

Members
-------

cnt
    number of regions

max
    size of the allocated array

total_size
    size of all regions

regions
    array of regions

name
    the memory type symbolic name

.. _`memblock`:

struct memblock
===============

.. c:type:: struct memblock

    memblock allocator metadata

.. _`memblock.definition`:

Definition
----------

.. code-block:: c

    struct memblock {
        bool bottom_up;
        phys_addr_t current_limit;
        struct memblock_type memory;
        struct memblock_type reserved;
    #ifdef CONFIG_HAVE_MEMBLOCK_PHYS_MAP
        struct memblock_type physmem;
    #endif
    }

.. _`memblock.members`:

Members
-------

bottom_up
    is bottom up direction?

current_limit
    physical address of the current allocation limit

memory
    usabe memory regions

reserved
    reserved memory regions

physmem
    all physical memory

.. _`for_each_reserved_mem_region`:

for_each_reserved_mem_region
============================

.. c:function::  for_each_reserved_mem_region( i,  p_start,  p_end)

    iterate over all reserved memblock areas

    :param i:
        u64 used as loop variable
    :type i: 

    :param p_start:
        ptr to phys_addr_t for start address of the range, can be \ ``NULL``\ 
    :type p_start: 

    :param p_end:
        ptr to phys_addr_t for end address of the range, can be \ ``NULL``\ 
    :type p_end: 

.. _`for_each_reserved_mem_region.description`:

Description
-----------

Walks over reserved areas of memblock. Available as soon as memblock
is initialized.

.. _`for_each_mem_pfn_range`:

for_each_mem_pfn_range
======================

.. c:function::  for_each_mem_pfn_range( i,  nid,  p_start,  p_end,  p_nid)

    early memory pfn range iterator

    :param i:
        an integer used as loop variable
    :type i: 

    :param nid:
        node selector, \ ``MAX_NUMNODES``\  for all nodes
    :type nid: 

    :param p_start:
        ptr to ulong for start pfn of the range, can be \ ``NULL``\ 
    :type p_start: 

    :param p_end:
        ptr to ulong for end pfn of the range, can be \ ``NULL``\ 
    :type p_end: 

    :param p_nid:
        ptr to int for nid of the range, can be \ ``NULL``\ 
    :type p_nid: 

.. _`for_each_mem_pfn_range.description`:

Description
-----------

Walks over configured memory ranges.

.. _`for_each_free_mem_range`:

for_each_free_mem_range
=======================

.. c:function::  for_each_free_mem_range( i,  nid,  flags,  p_start,  p_end,  p_nid)

    iterate through free memblock areas

    :param i:
        u64 used as loop variable
    :type i: 

    :param nid:
        node selector, \ ``NUMA_NO_NODE``\  for all nodes
    :type nid: 

    :param flags:
        pick from blocks based on memory attributes
    :type flags: 

    :param p_start:
        ptr to phys_addr_t for start address of the range, can be \ ``NULL``\ 
    :type p_start: 

    :param p_end:
        ptr to phys_addr_t for end address of the range, can be \ ``NULL``\ 
    :type p_end: 

    :param p_nid:
        ptr to int for nid of the range, can be \ ``NULL``\ 
    :type p_nid: 

.. _`for_each_free_mem_range.description`:

Description
-----------

Walks over free (memory && !reserved) areas of memblock.  Available as
soon as memblock is initialized.

.. _`memblock_set_current_limit`:

memblock_set_current_limit
==========================

.. c:function:: void memblock_set_current_limit(phys_addr_t limit)

    Set the current allocation limit to allow limiting allocations to what is currently accessible during boot

    :param limit:
        New limit value (physical address)
    :type limit: phys_addr_t

.. _`memblock_region_memory_base_pfn`:

memblock_region_memory_base_pfn
===============================

.. c:function:: unsigned long memblock_region_memory_base_pfn(const struct memblock_region *reg)

    get the lowest pfn of the memory region

    :param reg:
        memblock_region structure
    :type reg: const struct memblock_region \*

.. _`memblock_region_memory_base_pfn.return`:

Return
------

the lowest pfn intersecting with the memory region

.. _`memblock_region_memory_end_pfn`:

memblock_region_memory_end_pfn
==============================

.. c:function:: unsigned long memblock_region_memory_end_pfn(const struct memblock_region *reg)

    get the end pfn of the memory region

    :param reg:
        memblock_region structure
    :type reg: const struct memblock_region \*

.. _`memblock_region_memory_end_pfn.return`:

Return
------

the end_pfn of the reserved region

.. _`memblock_region_reserved_base_pfn`:

memblock_region_reserved_base_pfn
=================================

.. c:function:: unsigned long memblock_region_reserved_base_pfn(const struct memblock_region *reg)

    get the lowest pfn of the reserved region

    :param reg:
        memblock_region structure
    :type reg: const struct memblock_region \*

.. _`memblock_region_reserved_base_pfn.return`:

Return
------

the lowest pfn intersecting with the reserved region

.. _`memblock_region_reserved_end_pfn`:

memblock_region_reserved_end_pfn
================================

.. c:function:: unsigned long memblock_region_reserved_end_pfn(const struct memblock_region *reg)

    get the end pfn of the reserved region

    :param reg:
        memblock_region structure
    :type reg: const struct memblock_region \*

.. _`memblock_region_reserved_end_pfn.return`:

Return
------

the end_pfn of the reserved region

.. This file was automatic generated / don't edit.

