.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/mm/init.c

.. _`memory_map_top_down`:

memory_map_top_down
===================

.. c:function:: void memory_map_top_down(unsigned long map_start, unsigned long map_end)

    Map [map_start, map_end) top down

    :param map_start:
        start address of the target memory range
    :type map_start: unsigned long

    :param map_end:
        end address of the target memory range
    :type map_end: unsigned long

.. _`memory_map_top_down.description`:

Description
-----------

This function will setup direct mapping for memory range
[map_start, map_end) in top-down. That said, the page tables
will be allocated at the end of the memory, and we map the
memory in top-down.

.. _`memory_map_bottom_up`:

memory_map_bottom_up
====================

.. c:function:: void memory_map_bottom_up(unsigned long map_start, unsigned long map_end)

    Map [map_start, map_end) bottom up

    :param map_start:
        start address of the target memory range
    :type map_start: unsigned long

    :param map_end:
        end address of the target memory range
    :type map_end: unsigned long

.. _`memory_map_bottom_up.description`:

Description
-----------

This function will setup direct mapping for memory range
[map_start, map_end) in bottom-up. Since we have limited the
bottom-up allocation above the kernel, the page tables will
be allocated just above the kernel and we map the memory
in [map_start, map_end) in bottom-up.

.. This file was automatic generated / don't edit.

