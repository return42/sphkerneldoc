.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/sparc/kernel/smp_64.c

.. _`pcpu_alloc_bootmem`:

pcpu_alloc_bootmem
==================

.. c:function:: void *pcpu_alloc_bootmem(unsigned int cpu, size_t size, size_t align)

    NUMA friendly alloc_bootmem wrapper for percpu

    :param unsigned int cpu:
        cpu to allocate for

    :param size_t size:
        size allocation in bytes

    :param size_t align:
        alignment

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

