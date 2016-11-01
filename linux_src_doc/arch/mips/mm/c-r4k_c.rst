.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/mips/mm/c-r4k.c

.. _`r4k_op_needs_ipi`:

r4k_op_needs_ipi
================

.. c:function:: bool r4k_op_needs_ipi(unsigned int type)

    Decide if a cache op needs to be done on every core.

    :param unsigned int type:
        Type of cache operations (R4K_HIT or R4K_INDEX).

.. _`r4k_op_needs_ipi.description`:

Description
-----------

Decides whether a cache op needs to be performed on every core in the system.
This may change depending on the \ ``type``\  of cache operation, as well as the set
of online CPUs, so preemption should be disabled by the caller to prevent CPU
hotplug from changing the result.

.. _`r4k_op_needs_ipi.return`:

Return
------

1 if the cache operation \ ``type``\  should be done on every core in
the system.
0 if the cache operation \ ``type``\  is globalized and only needs to
be performed on a simple CPU.

.. _`has_valid_asid`:

has_valid_asid
==============

.. c:function:: int has_valid_asid(const struct mm_struct *mm, unsigned int type)

    Determine if an mm already has an ASID.

    :param const struct mm_struct \*mm:
        Memory map.

    :param unsigned int type:
        R4K_HIT or R4K_INDEX, type of cache op.

.. _`has_valid_asid.description`:

Description
-----------

Determines whether \ ``mm``\  already has an ASID on any of the CPUs which cache ops
of type \ ``type``\  within an \ :c:func:`r4k_on_each_cpu`\  call will affect. If
\ :c:func:`r4k_on_each_cpu`\  does an SMP call to a single VPE in each core, then the
scope of the operation is confined to sibling CPUs, otherwise all online CPUs
will need to be checked.

Must be called in non-preemptive context.

.. _`has_valid_asid.return`:

Return
------

1 if the CPUs affected by \ ``type``\  cache ops have an ASID for \ ``mm``\ .
0 otherwise.

.. This file was automatic generated / don't edit.

