.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/acpi/pptt.c

.. _`acpi_pptt_walk_cache`:

acpi_pptt_walk_cache
====================

.. c:function:: int acpi_pptt_walk_cache(struct acpi_table_header *table_hdr, int local_level, struct acpi_subtable_header *res, struct acpi_pptt_cache **found, int level, int type)

    Attempt to find the requested acpi_pptt_cache

    :param table_hdr:
        Pointer to the head of the PPTT table
    :type table_hdr: struct acpi_table_header \*

    :param local_level:
        passed res reflects this cache level
    :type local_level: int

    :param res:
        cache resource in the PPTT we want to walk
    :type res: struct acpi_subtable_header \*

    :param found:
        returns a pointer to the requested level if found
    :type found: struct acpi_pptt_cache \*\*

    :param level:
        the requested cache level
    :type level: int

    :param type:
        the requested cache type
    :type type: int

.. _`acpi_pptt_walk_cache.description`:

Description
-----------

Attempt to find a given cache level, while counting the max number
of cache levels for the cache node.

Given a pptt resource, verify that it is a cache node, then walk
down each level of caches, counting how many levels are found
as well as checking the cache type (icache, dcache, unified). If a
level & type match, then we set found, and continue the search.
Once the entire cache branch has been walked return its max
depth.

.. _`acpi_pptt_walk_cache.return`:

Return
------

The cache structure and the level we terminated with.

.. _`acpi_count_levels`:

acpi_count_levels
=================

.. c:function:: int acpi_count_levels(struct acpi_table_header *table_hdr, struct acpi_pptt_processor *cpu_node)

    Given a PPTT table, and a cpu node, count the caches

    :param table_hdr:
        Pointer to the head of the PPTT table
    :type table_hdr: struct acpi_table_header \*

    :param cpu_node:
        processor node we wish to count caches for
    :type cpu_node: struct acpi_pptt_processor \*

.. _`acpi_count_levels.description`:

Description
-----------

Given a processor node containing a processing unit, walk into it and count
how many levels exist solely for it, and then walk up each level until we hit
the root node (ignore the package level because it may be possible to have
caches that exist across packages). Count the number of cache levels that
exist at each level on the way up.

.. _`acpi_count_levels.return`:

Return
------

Total number of levels found.

.. _`acpi_pptt_leaf_node`:

acpi_pptt_leaf_node
===================

.. c:function:: int acpi_pptt_leaf_node(struct acpi_table_header *table_hdr, struct acpi_pptt_processor *node)

    Given a processor node, determine if its a leaf

    :param table_hdr:
        Pointer to the head of the PPTT table
    :type table_hdr: struct acpi_table_header \*

    :param node:
        passed node is checked to see if its a leaf
    :type node: struct acpi_pptt_processor \*

.. _`acpi_pptt_leaf_node.description`:

Description
-----------

Determine if the \*node parameter is a leaf node by iterating the
PPTT table, looking for nodes which reference it.

.. _`acpi_pptt_leaf_node.return`:

Return
------

0 if we find a node referencing the passed node (or table error),
or 1 if we don't.

.. _`acpi_find_processor_node`:

acpi_find_processor_node
========================

.. c:function:: struct acpi_pptt_processor *acpi_find_processor_node(struct acpi_table_header *table_hdr, u32 acpi_cpu_id)

    Given a PPTT table find the requested processor

    :param table_hdr:
        Pointer to the head of the PPTT table
    :type table_hdr: struct acpi_table_header \*

    :param acpi_cpu_id:
        cpu we are searching for
    :type acpi_cpu_id: u32

.. _`acpi_find_processor_node.description`:

Description
-----------

Find the subtable entry describing the provided processor.
This is done by iterating the PPTT table looking for processor nodes
which have an acpi_processor_id that matches the acpi_cpu_id parameter
passed into the function. If we find a node that matches this criteria
we verify that its a leaf node in the topology rather than depending
on the valid flag, which doesn't need to be set for leaf nodes.

.. _`acpi_find_processor_node.return`:

Return
------

NULL, or the processors acpi_pptt_processor\*

.. _`update_cache_properties`:

update_cache_properties
=======================

.. c:function:: void update_cache_properties(struct cacheinfo *this_leaf, struct acpi_pptt_cache *found_cache, struct acpi_pptt_processor *cpu_node)

    Update cacheinfo for the given processor

    :param this_leaf:
        Kernel cache info structure being updated
    :type this_leaf: struct cacheinfo \*

    :param found_cache:
        The PPTT node describing this cache instance
    :type found_cache: struct acpi_pptt_cache \*

    :param cpu_node:
        A unique reference to describe this cache instance
    :type cpu_node: struct acpi_pptt_processor \*

.. _`update_cache_properties.description`:

Description
-----------

The ACPI spec implies that the fields in the cache structures are used to
extend and correct the information probed from the hardware. Lets only
set fields that we determine are VALID.

.. _`update_cache_properties.return`:

Return
------

nothing. Side effect of updating the global cacheinfo

.. _`topology_get_acpi_cpu_tag`:

topology_get_acpi_cpu_tag
=========================

.. c:function:: int topology_get_acpi_cpu_tag(struct acpi_table_header *table, unsigned int cpu, int level, int flag)

    Find a unique topology value for a feature

    :param table:
        Pointer to the head of the PPTT table
    :type table: struct acpi_table_header \*

    :param cpu:
        Kernel logical cpu number
    :type cpu: unsigned int

    :param level:
        A level that terminates the search
    :type level: int

    :param flag:
        A flag which terminates the search
    :type flag: int

.. _`topology_get_acpi_cpu_tag.description`:

Description
-----------

Get a unique value given a cpu, and a topology level, that can be
matched to determine which cpus share common topological features
at that level.

.. _`topology_get_acpi_cpu_tag.return`:

Return
------

Unique value, or -ENOENT if unable to locate cpu

.. _`acpi_find_last_cache_level`:

acpi_find_last_cache_level
==========================

.. c:function:: int acpi_find_last_cache_level(unsigned int cpu)

    Determines the number of cache levels for a PE

    :param cpu:
        Kernel logical cpu number
    :type cpu: unsigned int

.. _`acpi_find_last_cache_level.description`:

Description
-----------

Given a logical cpu number, returns the number of levels of cache represented
in the PPTT. Errors caused by lack of a PPTT table, or otherwise, return 0
indicating we didn't find any cache levels.

.. _`acpi_find_last_cache_level.return`:

Return
------

Cache levels visible to this core.

.. _`cache_setup_acpi`:

cache_setup_acpi
================

.. c:function:: int cache_setup_acpi(unsigned int cpu)

    Override CPU cache topology with data from the PPTT

    :param cpu:
        Kernel logical cpu number
    :type cpu: unsigned int

.. _`cache_setup_acpi.description`:

Description
-----------

Updates the global cache info provided by \ :c:func:`cpu_get_cacheinfo`\ 
when there are valid properties in the acpi_pptt_cache nodes. A
successful parse may not result in any updates if none of the
cache levels have any valid flags set.  Futher, a unique value is
associated with each known CPU cache entry. This unique value
can be used to determine whether caches are shared between cpus.

.. _`cache_setup_acpi.return`:

Return
------

-ENOENT on failure to find table, or 0 on success

.. _`find_acpi_cpu_topology`:

find_acpi_cpu_topology
======================

.. c:function:: int find_acpi_cpu_topology(unsigned int cpu, int level)

    Determine a unique topology value for a given cpu

    :param cpu:
        Kernel logical cpu number
    :type cpu: unsigned int

    :param level:
        The topological level for which we would like a unique ID
    :type level: int

.. _`find_acpi_cpu_topology.description`:

Description
-----------

Determine a topology unique ID for each thread/core/cluster/mc_grouping
/socket/etc. This ID can then be used to group peers, which will have
matching ids.

The search terminates when either the requested level is found or
we reach a root node. Levels beyond the termination point will return the
same unique ID. The unique id for level 0 is the acpi processor id. All
other levels beyond this use a generated value to uniquely identify
a topological feature.

.. _`find_acpi_cpu_topology.return`:

Return
------

-ENOENT if the PPTT doesn't exist, or the cpu cannot be found.
Otherwise returns a value which represents a unique topological feature.

.. _`find_acpi_cpu_cache_topology`:

find_acpi_cpu_cache_topology
============================

.. c:function:: int find_acpi_cpu_cache_topology(unsigned int cpu, int level)

    Determine a unique cache topology value

    :param cpu:
        Kernel logical cpu number
    :type cpu: unsigned int

    :param level:
        The cache level for which we would like a unique ID
    :type level: int

.. _`find_acpi_cpu_cache_topology.description`:

Description
-----------

Determine a unique ID for each unified cache in the system

.. _`find_acpi_cpu_cache_topology.return`:

Return
------

-ENOENT if the PPTT doesn't exist, or the cpu cannot be found.
Otherwise returns a value which represents a unique topological feature.

.. _`find_acpi_cpu_topology_package`:

find_acpi_cpu_topology_package
==============================

.. c:function:: int find_acpi_cpu_topology_package(unsigned int cpu)

    Determine a unique cpu package value

    :param cpu:
        Kernel logical cpu number
    :type cpu: unsigned int

.. _`find_acpi_cpu_topology_package.description`:

Description
-----------

Determine a topology unique package ID for the given cpu.
This ID can then be used to group peers, which will have matching ids.

The search terminates when either a level is found with the PHYSICAL_PACKAGE
flag set or we reach a root node.

.. _`find_acpi_cpu_topology_package.return`:

Return
------

-ENOENT if the PPTT doesn't exist, or the cpu cannot be found.
Otherwise returns a value which represents the package for this cpu.

.. This file was automatic generated / don't edit.

