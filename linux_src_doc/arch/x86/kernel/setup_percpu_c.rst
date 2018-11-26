.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/kernel/setup_percpu.c

.. _`pcpu_need_numa`:

pcpu_need_numa
==============

.. c:function:: bool pcpu_need_numa( void)

    determine percpu allocation needs to consider NUMA

    :param void:
        no arguments
    :type void: 

.. _`pcpu_need_numa.description`:

Description
-----------

If NUMA is not configured or there is only one NUMA node available,
there is no reason to consider NUMA.  This function determines
whether percpu allocation should consider NUMA or not.

.. _`pcpu_need_numa.return`:

Return
------

true if NUMA should be considered; otherwise, false.

.. _`pcpu_alloc_bootmem`:

pcpu_alloc_bootmem
==================

.. c:function:: void *pcpu_alloc_bootmem(unsigned int cpu, unsigned long size, unsigned long align)

    NUMA friendly alloc_bootmem wrapper for percpu

    :param cpu:
        cpu to allocate for
    :type cpu: unsigned int

    :param size:
        size allocation in bytes
    :type size: unsigned long

    :param align:
        alignment
    :type align: unsigned long

.. _`pcpu_alloc_bootmem.description`:

Description
-----------

Allocate \ ``size``\  bytes aligned at \ ``align``\  for cpu \ ``cpu``\ .  This wrapper
does the right thing for NUMA regardless of the current
configuration.

.. _`pcpu_alloc_bootmem.return`:

Return
------

Pointer to the allocated area on success, NULL on failure.

.. This file was automatic generated / don't edit.

