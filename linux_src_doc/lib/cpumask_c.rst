.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/cpumask.c

.. _`cpumask_next_and`:

cpumask_next_and
================

.. c:function:: int cpumask_next_and(int n, const struct cpumask *src1p, const struct cpumask *src2p)

    get the next cpu in \*src1p & \*src2p

    :param int n:
        the cpu prior to the place to search (ie. return will be > \ ``n``\ )

    :param const struct cpumask \*src1p:
        the first cpumask pointer

    :param const struct cpumask \*src2p:
        the second cpumask pointer

.. _`cpumask_next_and.description`:

Description
-----------

Returns >= nr_cpu_ids if no further cpus set in both.

.. _`cpumask_any_but`:

cpumask_any_but
===============

.. c:function:: int cpumask_any_but(const struct cpumask *mask, unsigned int cpu)

    return a "random" in a cpumask, but not this one.

    :param const struct cpumask \*mask:
        the cpumask to search

    :param unsigned int cpu:
        the cpu to ignore.

.. _`cpumask_any_but.description`:

Description
-----------

Often used to find any cpu but \ :c:func:`smp_processor_id`\  in a mask.
Returns >= nr_cpu_ids if no cpus set.

.. _`cpumask_next_wrap`:

cpumask_next_wrap
=================

.. c:function:: int cpumask_next_wrap(int n, const struct cpumask *mask, int start, bool wrap)

    helper to implement for_each_cpu_wrap

    :param int n:
        the cpu prior to the place to search

    :param const struct cpumask \*mask:
        the cpumask pointer

    :param int start:
        the start point of the iteration

    :param bool wrap:
        assume \ ``n``\  crossing \ ``start``\  terminates the iteration

.. _`cpumask_next_wrap.description`:

Description
-----------

Returns >= nr_cpu_ids on completion

.. _`cpumask_next_wrap.note`:

Note
----

the \ ``wrap``\  argument is required for the start condition when
we cannot assume \ ``start``\  is set in \ ``mask``\ .

.. _`alloc_cpumask_var_node`:

alloc_cpumask_var_node
======================

.. c:function:: bool alloc_cpumask_var_node(cpumask_var_t *mask, gfp_t flags, int node)

    allocate a struct cpumask on a given node

    :param cpumask_var_t \*mask:
        pointer to cpumask_var_t where the cpumask is returned

    :param gfp_t flags:
        GFP\_ flags

    :param int node:
        *undescribed*

.. _`alloc_cpumask_var_node.description`:

Description
-----------

Only defined when CONFIG_CPUMASK_OFFSTACK=y, otherwise is
a nop returning a constant 1 (in <linux/cpumask.h>)
Returns TRUE if memory allocation succeeded, FALSE otherwise.

In addition, mask will be NULL if this fails.  Note that gcc is
usually smart enough to know that mask can never be NULL if
CONFIG_CPUMASK_OFFSTACK=n, so does code elimination in that case
too.

.. _`alloc_cpumask_var`:

alloc_cpumask_var
=================

.. c:function:: bool alloc_cpumask_var(cpumask_var_t *mask, gfp_t flags)

    allocate a struct cpumask

    :param cpumask_var_t \*mask:
        pointer to cpumask_var_t where the cpumask is returned

    :param gfp_t flags:
        GFP\_ flags

.. _`alloc_cpumask_var.description`:

Description
-----------

Only defined when CONFIG_CPUMASK_OFFSTACK=y, otherwise is
a nop returning a constant 1 (in <linux/cpumask.h>).

See alloc_cpumask_var_node.

.. _`alloc_bootmem_cpumask_var`:

alloc_bootmem_cpumask_var
=========================

.. c:function:: void alloc_bootmem_cpumask_var(cpumask_var_t *mask)

    allocate a struct cpumask from the bootmem arena.

    :param cpumask_var_t \*mask:
        pointer to cpumask_var_t where the cpumask is returned

.. _`alloc_bootmem_cpumask_var.description`:

Description
-----------

Only defined when CONFIG_CPUMASK_OFFSTACK=y, otherwise is
a nop (in <linux/cpumask.h>).
Either returns an allocated (zero-filled) cpumask, or causes the
system to panic.

.. _`free_cpumask_var`:

free_cpumask_var
================

.. c:function:: void free_cpumask_var(cpumask_var_t mask)

    frees memory allocated for a struct cpumask.

    :param cpumask_var_t mask:
        cpumask to free

.. _`free_cpumask_var.description`:

Description
-----------

This is safe on a NULL mask.

.. _`free_bootmem_cpumask_var`:

free_bootmem_cpumask_var
========================

.. c:function:: void free_bootmem_cpumask_var(cpumask_var_t mask)

    frees result of alloc_bootmem_cpumask_var

    :param cpumask_var_t mask:
        cpumask to free

.. _`cpumask_local_spread`:

cpumask_local_spread
====================

.. c:function:: unsigned int cpumask_local_spread(unsigned int i, int node)

    select the i'th cpu with local numa cpu's first

    :param unsigned int i:
        index number

    :param int node:
        local numa_node

.. _`cpumask_local_spread.description`:

Description
-----------

This function selects an online CPU according to a numa aware policy;
local cpus are returned first, followed by non-local ones, then it
wraps around.

It's not very efficient, but useful for setup.

.. This file was automatic generated / don't edit.

