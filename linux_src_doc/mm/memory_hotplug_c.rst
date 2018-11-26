.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/memory_hotplug.c

.. _`__remove_pages`:

\__remove_pages
===============

.. c:function:: int __remove_pages(struct zone *zone, unsigned long phys_start_pfn, unsigned long nr_pages, struct vmem_altmap *altmap)

    remove sections of pages from a zone

    :param zone:
        zone from which pages need to be removed
    :type zone: struct zone \*

    :param phys_start_pfn:
        starting pageframe (must be aligned to start of a section)
    :type phys_start_pfn: unsigned long

    :param nr_pages:
        number of pages to remove (must be multiple of section size)
    :type nr_pages: unsigned long

    :param altmap:
        alternative device page map or \ ``NULL``\  if default memmap is used
    :type altmap: struct vmem_altmap \*

.. _`__remove_pages.description`:

Description
-----------

Generic helper function to remove section mappings and sysfs entries
for the section of the memory we are removing. Caller needs to make
sure that pages are marked reserved and zones are adjust properly by
calling \ :c:func:`offline_pages`\ .

.. _`__try_online_node`:

\__try_online_node
==================

.. c:function:: int __try_online_node(int nid, u64 start, bool set_node_online)

    online a node if offlined

    :param nid:
        the node ID
    :type nid: int

    :param start:
        start addr of the node
    :type start: u64

    :param set_node_online:
        Whether we want to online the node
        called by \ :c:func:`cpu_up`\  to online a node without onlined memory.
    :type set_node_online: bool

.. _`__try_online_node.return`:

Return
------

1 -> a new node has been allocated
0 -> the node is already online
-ENOMEM -> the node could not be allocated

.. _`walk_memory_range`:

walk_memory_range
=================

.. c:function:: int walk_memory_range(unsigned long start_pfn, unsigned long end_pfn, void *arg, int (*func)(struct memory_block *, void *))

    walks through all mem sections in [start_pfn, end_pfn)

    :param start_pfn:
        start pfn of the memory range
    :type start_pfn: unsigned long

    :param end_pfn:
        end pfn of the memory range
    :type end_pfn: unsigned long

    :param arg:
        argument passed to func
    :type arg: void \*

    :param int (\*func)(struct memory_block \*, void \*):
        callback for each memory section walked

.. _`walk_memory_range.description`:

Description
-----------

This function walks through all present mem sections in range
[start_pfn, end_pfn) and call func on each mem section.

Returns the return value of func.

.. _`try_offline_node`:

try_offline_node
================

.. c:function:: void try_offline_node(int nid)

    :param nid:
        the node ID
    :type nid: int

.. _`try_offline_node.description`:

Description
-----------

Offline a node if all memory sections and cpus of the node are removed.

.. _`try_offline_node.note`:

NOTE
----

The caller must call \ :c:func:`lock_device_hotplug`\  to serialize hotplug
and online/offline operations before this call.

.. _`__remove_memory`:

\__remove_memory
================

.. c:function:: void __ref __remove_memory(int nid, u64 start, u64 size)

    :param nid:
        the node ID
    :type nid: int

    :param start:
        physical address of the region to remove
    :type start: u64

    :param size:
        size of the region to remove
    :type size: u64

.. _`__remove_memory.note`:

NOTE
----

The caller must call \ :c:func:`lock_device_hotplug`\  to serialize hotplug
and online/offline operations before this call, as required by
\ :c:func:`try_offline_node`\ .

.. This file was automatic generated / don't edit.

