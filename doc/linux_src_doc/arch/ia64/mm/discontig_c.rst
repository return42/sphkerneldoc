.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/ia64/mm/discontig.c

.. _`build_node_maps`:

build_node_maps
===============

.. c:function:: int build_node_maps(unsigned long start, unsigned long len, int node)

    callback to setup bootmem structs for each node

    :param unsigned long start:
        physical start of range

    :param unsigned long len:
        length of range

    :param int node:
        node where this range resides

.. _`build_node_maps.description`:

Description
-----------

We allocate a struct bootmem_data for each piece of memory that we wish to
treat as a virtually contiguous block (i.e. each node). Each such block
must start on an \ ``IA64_GRANULE_SIZE``\  boundary, so we round the address down
if necessary.  Any non-existent pages will simply be part of the virtual
memmap.  We also update min_low_pfn and max_low_pfn here as we receive
memory ranges from the caller.

.. _`early_nr_cpus_node`:

early_nr_cpus_node
==================

.. c:function:: int early_nr_cpus_node(int node)

    return number of cpus on a given node

    :param int node:
        node to check

.. _`early_nr_cpus_node.description`:

Description
-----------

Count the number of cpus on \ ``node``\ .  We can't use \ :c:func:`nr_cpus_node`\  yet because
\ :c:func:`acpi_boot_init`\  (which builds the node_to_cpu_mask array) hasn't been
called yet.  Note that node 0 will also count all non-existent cpus.

.. _`compute_pernodesize`:

compute_pernodesize
===================

.. c:function:: unsigned long compute_pernodesize(int node)

    compute size of pernode data

    :param int node:
        the node id.

.. _`per_cpu_node_setup`:

per_cpu_node_setup
==================

.. c:function:: void *per_cpu_node_setup(void *cpu_data, int node)

    setup per-cpu areas on each node

    :param void \*cpu_data:
        per-cpu area on this node

    :param int node:
        node to setup

.. _`per_cpu_node_setup.description`:

Description
-----------

Copy the static per-cpu data into the region we just set aside and then
setup \__per_cpu_offset for each CPU on this node.  Return a pointer to
the end of the area.

.. _`setup_per_cpu_areas`:

setup_per_cpu_areas
===================

.. c:function:: void setup_per_cpu_areas( void)

    setup percpu areas

    :param  void:
        no arguments

.. _`setup_per_cpu_areas.description`:

Description
-----------

Arch code has already allocated and initialized percpu areas.  All
this function has to do is to teach the determined layout to the
dynamic percpu allocator, which happens to be more complex than
creating whole new ones using helpers.

.. _`fill_pernode`:

fill_pernode
============

.. c:function:: void fill_pernode(int node, unsigned long pernode, unsigned long pernodesize)

    initialize pernode data.

    :param int node:
        the node id.

    :param unsigned long pernode:
        physical address of pernode data

    :param unsigned long pernodesize:
        size of the pernode data

.. _`find_pernode_space`:

find_pernode_space
==================

.. c:function:: int find_pernode_space(unsigned long start, unsigned long len, int node)

    allocate memory for memory map and per-node structures

    :param unsigned long start:
        physical start of range

    :param unsigned long len:
        length of range

    :param int node:
        node where this range resides

.. _`find_pernode_space.description`:

Description
-----------

This routine reserves space for the per-cpu data struct, the list of
pg_data_ts and the per-node data struct.  Each node will have something like
the following in the first chunk of addr. space large enough to hold it.

\_______________________\_
\|                        \|
\|~~~~~~~~~~~~~~~~~~~~~~~~\| <-- NODEDATA_ALIGN(start, node) for the first
\|    PERCPU_PAGE_SIZE \*  \|     start and length big enough
\|    cpus_on_this_node   \| Node 0 will also have entries for all non-existent cpus.
\|------------------------\|
\|   local pg_data_t \*    \|
\|------------------------\|
\|  local ia64_node_data  \|
\|------------------------\|
\|          ???           \|
\|________________________\|

Once this space has been set aside, the bootmem maps are initialized.  We
could probably move the allocation of the per-cpu and ia64_node_data space
outside of this function and use \ :c:func:`alloc_bootmem_node`\ , but doing it here
is straightforward and we get the alignments we want so...

.. _`free_node_bootmem`:

free_node_bootmem
=================

.. c:function:: int free_node_bootmem(unsigned long start, unsigned long len, int node)

    free bootmem allocator memory for use

    :param unsigned long start:
        physical start of range

    :param unsigned long len:
        length of range

    :param int node:
        node where this range resides

.. _`free_node_bootmem.description`:

Description
-----------

Simply calls the bootmem allocator to free the specified ranged from
the given pg_data_t's bdata struct.  After this function has been called
for all the entries in the EFI memory map, the bootmem allocator will
be ready to service allocation requests.

.. _`reserve_pernode_space`:

reserve_pernode_space
=====================

.. c:function:: void reserve_pernode_space( void)

    reserve memory for per-node space

    :param  void:
        no arguments

.. _`reserve_pernode_space.description`:

Description
-----------

Reserve the space used by the bootmem maps & per-node space in the boot
allocator so that when we actually create the real mem maps we don't
use their memory.

.. _`initialize_pernode_data`:

initialize_pernode_data
=======================

.. c:function:: void initialize_pernode_data( void)

    fixup per-cpu & per-node pointers

    :param  void:
        no arguments

.. _`initialize_pernode_data.description`:

Description
-----------

Each node's per-node area has a copy of the global pg_data_t list, so
we copy that to each node here, as well as setting the per-cpu pointer
to the local node data structure.  The active_cpus field of the per-node
structure gets setup by the \ :c:func:`platform_cpu_init`\  function later.

.. _`memory_less_node_alloc`:

memory_less_node_alloc
======================

.. c:function:: void *memory_less_node_alloc(int nid, unsigned long pernodesize)

    \* attempt to allocate memory on the best NUMA slit node but fall back to any other node when \__alloc_bootmem_node fails for best.

    :param int nid:
        node id

    :param unsigned long pernodesize:
        size of this node's pernode data

.. _`memory_less_nodes`:

memory_less_nodes
=================

.. c:function:: void memory_less_nodes( void)

    allocate and initialize CPU only nodes pernode information.

    :param  void:
        no arguments

.. _`find_memory`:

find_memory
===========

.. c:function:: void find_memory( void)

    walk the EFI memory map and setup the bootmem allocator

    :param  void:
        no arguments

.. _`find_memory.description`:

Description
-----------

Called early in boot to setup the bootmem allocator, and to
allocate the per-cpu and per-node structures.

.. _`per_cpu_init`:

per_cpu_init
============

.. c:function:: void *per_cpu_init( void)

    setup per-cpu variables

    :param  void:
        no arguments

.. _`per_cpu_init.description`:

Description
-----------

\ :c:func:`find_pernode_space`\  does most of this already, we just need to set
local_per_cpu_offset

.. _`call_pernode_memory`:

call_pernode_memory
===================

.. c:function:: void call_pernode_memory(unsigned long start, unsigned long len, void *arg)

    use SRAT to call callback functions with node info

    :param unsigned long start:
        physical start of range

    :param unsigned long len:
        length of range

    :param void \*arg:
        function to call for each range

.. _`call_pernode_memory.description`:

Description
-----------

\ :c:func:`efi_memmap_walk`\  knows nothing about layout of memory across nodes. Find
out to which node a block of memory belongs.  Ignore memory that we cannot
identify, and split blocks that run across multiple nodes.

Take this opportunity to round the start address up and the end address
down to page boundaries.

.. _`count_node_pages`:

count_node_pages
================

.. c:function:: int count_node_pages(unsigned long start, unsigned long len, int node)

    callback to build per-node memory info structures

    :param unsigned long start:
        physical start of range

    :param unsigned long len:
        length of range

    :param int node:
        node where this range resides

.. _`count_node_pages.description`:

Description
-----------

Each node has it's own number of physical pages, DMAable pages, start, and
end page frame number.  This routine will be called by \ :c:func:`call_pernode_memory`\ 
for each piece of usable memory and will setup these values for each node.
Very similar to \ :c:func:`build_maps`\ .

.. _`paging_init`:

paging_init
===========

.. c:function:: void paging_init( void)

    setup page tables

    :param  void:
        no arguments

.. _`paging_init.description`:

Description
-----------

\ :c:func:`paging_init`\  sets up the page tables for each node of the system and frees
the bootmem allocator memory for general use.

.. This file was automatic generated / don't edit.

