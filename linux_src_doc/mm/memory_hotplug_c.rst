.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/memory_hotplug.c

.. _`__remove_pages`:

__remove_pages
==============

.. c:function:: int __remove_pages(struct zone *zone, unsigned long phys_start_pfn, unsigned long nr_pages, struct vmem_altmap *altmap)

    remove sections of pages from a zone

    :param struct zone \*zone:
        zone from which pages need to be removed

    :param unsigned long phys_start_pfn:
        starting pageframe (must be aligned to start of a section)

    :param unsigned long nr_pages:
        number of pages to remove (must be multiple of section size)

    :param struct vmem_altmap \*altmap:
        *undescribed*

.. _`__remove_pages.description`:

Description
-----------

Generic helper function to remove section mappings and sysfs entries
for the section of the memory we are removing. Caller needs to make
sure that pages are marked reserved and zones are adjust properly by
calling \ :c:func:`offline_pages`\ .

.. _`try_online_node`:

try_online_node
===============

.. c:function:: int try_online_node(int nid)

    online a node if offlined

    :param int nid:
        *undescribed*

.. _`try_online_node.description`:

Description
-----------

called by \ :c:func:`cpu_up`\  to online a node without onlined memory.

.. _`walk_memory_range`:

walk_memory_range
=================

.. c:function:: int walk_memory_range(unsigned long start_pfn, unsigned long end_pfn, void *arg, int (*func)(struct memory_block *, void *))

    walks through all mem sections in [start_pfn, end_pfn)

    :param unsigned long start_pfn:
        start pfn of the memory range

    :param unsigned long end_pfn:
        end pfn of the memory range

    :param void \*arg:
        argument passed to func

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

    :param int nid:
        *undescribed*

.. _`try_offline_node.description`:

Description
-----------

Offline a node if all memory sections and cpus of the node are removed.

.. _`try_offline_node.note`:

NOTE
----

The caller must call \ :c:func:`lock_device_hotplug`\  to serialize hotplug
and online/offline operations before this call.

.. _`remove_memory`:

remove_memory
=============

.. c:function:: void __ref remove_memory(int nid, u64 start, u64 size)

    :param int nid:
        *undescribed*

    :param u64 start:
        *undescribed*

    :param u64 size:
        *undescribed*

.. _`remove_memory.note`:

NOTE
----

The caller must call \ :c:func:`lock_device_hotplug`\  to serialize hotplug
and online/offline operations before this call, as required by
\ :c:func:`try_offline_node`\ .

.. This file was automatic generated / don't edit.

