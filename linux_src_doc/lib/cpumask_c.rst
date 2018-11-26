.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/cpumask.c

.. _`cpumask_next`:

cpumask_next
============

.. c:function:: unsigned int cpumask_next(int n, const struct cpumask *srcp)

    get the next cpu in a cpumask

    :param n:
        the cpu prior to the place to search (ie. return will be > \ ``n``\ )
    :type n: int

    :param srcp:
        the cpumask pointer
    :type srcp: const struct cpumask \*

.. _`cpumask_next.description`:

Description
-----------

Returns >= nr_cpu_ids if no further cpus set.

.. _`cpumask_next_and`:

cpumask_next_and
================

.. c:function:: int cpumask_next_and(int n, const struct cpumask *src1p, const struct cpumask *src2p)

    get the next cpu in \*src1p & \*src2p

    :param n:
        the cpu prior to the place to search (ie. return will be > \ ``n``\ )
    :type n: int

    :param src1p:
        the first cpumask pointer
    :type src1p: const struct cpumask \*

    :param src2p:
        the second cpumask pointer
    :type src2p: const struct cpumask \*

.. _`cpumask_next_and.description`:

Description
-----------

Returns >= nr_cpu_ids if no further cpus set in both.

.. _`cpumask_any_but`:

cpumask_any_but
===============

.. c:function:: int cpumask_any_but(const struct cpumask *mask, unsigned int cpu)

    return a "random" in a cpumask, but not this one.

    :param mask:
        the cpumask to search
    :type mask: const struct cpumask \*

    :param cpu:
        the cpu to ignore.
    :type cpu: unsigned int

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

    :param n:
        the cpu prior to the place to search
    :type n: int

    :param mask:
        the cpumask pointer
    :type mask: const struct cpumask \*

    :param start:
        the start point of the iteration
    :type start: int

    :param wrap:
        assume \ ``n``\  crossing \ ``start``\  terminates the iteration
    :type wrap: bool

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

    :param mask:
        pointer to cpumask_var_t where the cpumask is returned
    :type mask: cpumask_var_t \*

    :param flags:
        GFP\_ flags
    :type flags: gfp_t

    :param node:
        *undescribed*
    :type node: int

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

    :param mask:
        pointer to cpumask_var_t where the cpumask is returned
    :type mask: cpumask_var_t \*

    :param flags:
        GFP\_ flags
    :type flags: gfp_t

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

    :param mask:
        pointer to cpumask_var_t where the cpumask is returned
    :type mask: cpumask_var_t \*

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

    :param mask:
        cpumask to free
    :type mask: cpumask_var_t

.. _`free_cpumask_var.description`:

Description
-----------

This is safe on a NULL mask.

.. _`free_bootmem_cpumask_var`:

free_bootmem_cpumask_var
========================

.. c:function:: void free_bootmem_cpumask_var(cpumask_var_t mask)

    frees result of alloc_bootmem_cpumask_var

    :param mask:
        cpumask to free
    :type mask: cpumask_var_t

.. _`cpumask_local_spread`:

cpumask_local_spread
====================

.. c:function:: unsigned int cpumask_local_spread(unsigned int i, int node)

    select the i'th cpu with local numa cpu's first

    :param i:
        index number
    :type i: unsigned int

    :param node:
        local numa_node
    :type node: int

.. _`cpumask_local_spread.description`:

Description
-----------

This function selects an online CPU according to a numa aware policy;
local cpus are returned first, followed by non-local ones, then it
wraps around.

It's not very efficient, but useful for setup.

.. This file was automatic generated / don't edit.

