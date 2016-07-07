.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/ia64/mm/contig.c

.. _`find_bootmap_location`:

find_bootmap_location
=====================

.. c:function:: int find_bootmap_location(u64 start, u64 end, void *arg)

    callback to find a memory area for the bootmap

    :param u64 start:
        start of region

    :param u64 end:
        end of region

    :param void \*arg:
        unused callback data

.. _`find_bootmap_location.description`:

Description
-----------

Find a place to put the bootmap and return its starting address in
bootmap_start.  This address must be page-aligned.

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

Allocate and setup per-cpu data areas.

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

.. _`find_memory`:

find_memory
===========

.. c:function:: void find_memory( void)

    setup memory map

    :param  void:
        no arguments

.. _`find_memory.description`:

Description
-----------

Walk the EFI memory map and find usable memory for the system, taking
into account reserved areas.

.. This file was automatic generated / don't edit.

