.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/ia64/mm/contig.c

.. _`per_cpu_init`:

per_cpu_init
============

.. c:function:: void *per_cpu_init( void)

    setup per-cpu variables

    :param void:
        no arguments
    :type void: 

.. _`per_cpu_init.description`:

Description
-----------

Allocate and setup per-cpu data areas.

.. _`setup_per_cpu_areas`:

setup_per_cpu_areas
===================

.. c:function:: void setup_per_cpu_areas( void)

    setup percpu areas

    :param void:
        no arguments
    :type void: 

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

    :param void:
        no arguments
    :type void: 

.. _`find_memory.description`:

Description
-----------

Walk the EFI memory map and find usable memory for the system, taking
into account reserved areas.

.. This file was automatic generated / don't edit.

