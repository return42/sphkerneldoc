.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/x86/mm/numa_emulation.c

.. _`numa_emulation`:

numa_emulation
==============

.. c:function:: void numa_emulation(struct numa_meminfo *numa_meminfo, int numa_dist_cnt)

    Emulate NUMA nodes

    :param numa_meminfo:
        NUMA configuration to massage
    :type numa_meminfo: struct numa_meminfo \*

    :param numa_dist_cnt:
        The size of the physical NUMA distance table
    :type numa_dist_cnt: int

.. _`numa_emulation.description`:

Description
-----------

Emulate NUMA nodes according to the numa=fake kernel parameter.
\ ``numa_meminfo``\  contains the physical memory configuration and is modified
to reflect the emulated configuration on success.  \ ``numa_dist_cnt``\  is
used to determine the size of the physical distance table.

On success, the following modifications are made.

- \ ``numa_meminfo``\  is updated to reflect the emulated nodes.

- \__apicid_to_node[] is updated such that APIC IDs are mapped to the
emulated nodes.

- NUMA distance table is rebuilt to represent distances between emulated
nodes.  The distances are determined considering how emulated nodes
are mapped to physical nodes and match the actual distances.

- emu_nid_to_phys[] reflects how emulated nodes are mapped to physical
nodes.  This is used by \ :c:func:`numa_add_cpu`\  and \ :c:func:`numa_remove_cpu`\ .

If emulation is not enabled or fails, emu_nid_to_phys[] is filled with
identity mapping and no other modification is made.

.. This file was automatic generated / don't edit.

