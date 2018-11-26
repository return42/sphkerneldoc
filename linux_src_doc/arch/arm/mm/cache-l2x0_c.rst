.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mm/cache-l2x0.c

.. _`l2x0_cache_size_of_parse`:

l2x0_cache_size_of_parse
========================

.. c:function:: int l2x0_cache_size_of_parse(const struct device_node *np, u32 *aux_val, u32 *aux_mask, u32 *associativity, u32 max_way_size)

    read cache size parameters from DT

    :param np:
        the device tree node for the l2 cache
    :type np: const struct device_node \*

    :param aux_val:
        pointer to machine-supplied auxilary register value, to
        be augmented by the call (bits to be set to 1)
    :type aux_val: u32 \*

    :param aux_mask:
        pointer to machine-supplied auxilary register mask, to
        be augmented by the call (bits to be set to 0)
    :type aux_mask: u32 \*

    :param associativity:
        variable to return the calculated associativity in
    :type associativity: u32 \*

    :param max_way_size:
        the maximum size in bytes for the cache ways
    :type max_way_size: u32

.. This file was automatic generated / don't edit.

