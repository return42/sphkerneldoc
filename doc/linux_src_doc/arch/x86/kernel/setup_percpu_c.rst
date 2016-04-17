.. -*- coding: utf-8; mode: rst -*-

==============
setup_percpu.c
==============


.. _`pcpu_need_numa`:

pcpu_need_numa
==============

.. c:function:: bool pcpu_need_numa ( void)

    determine percpu allocation needs to consider NUMA

    :param void:
        no arguments



.. _`pcpu_need_numa.description`:

Description
-----------


If NUMA is not configured or there is only one NUMA node available,
there is no reason to consider NUMA.  This function determines
whether percpu allocation should consider NUMA or not.



.. _`pcpu_need_numa.returns`:

RETURNS
-------

true if NUMA should be considered; otherwise, false.



.. _`pcpu_alloc_bootmem`:

pcpu_alloc_bootmem
==================

.. c:function:: void *pcpu_alloc_bootmem (unsigned int cpu, unsigned long size, unsigned long align)

    NUMA friendly alloc_bootmem wrapper for percpu

    :param unsigned int cpu:
        cpu to allocate for

    :param unsigned long size:
        size allocation in bytes

    :param unsigned long align:
        alignment



.. _`pcpu_alloc_bootmem.description`:

Description
-----------

Allocate ``size`` bytes aligned at ``align`` for cpu ``cpu``\ .  This wrapper
does the right thing for NUMA regardless of the current
configuration.



.. _`pcpu_alloc_bootmem.returns`:

RETURNS
-------

Pointer to the allocated area on success, NULL on failure.

