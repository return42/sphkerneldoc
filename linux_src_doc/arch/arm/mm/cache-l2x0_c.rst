.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mm/cache-l2x0.c

.. _`l2x0_cache_size_of_parse`:

l2x0_cache_size_of_parse
========================

.. c:function:: int l2x0_cache_size_of_parse(const struct device_node *np, u32 *aux_val, u32 *aux_mask, u32 *associativity, u32 max_way_size)

    read cache size parameters from DT

    :param const struct device_node \*np:
        the device tree node for the l2 cache

    :param u32 \*aux_val:
        pointer to machine-supplied auxilary register value, to
        be augmented by the call (bits to be set to 1)

    :param u32 \*aux_mask:
        pointer to machine-supplied auxilary register mask, to
        be augmented by the call (bits to be set to 0)

    :param u32 \*associativity:
        variable to return the calculated associativity in

    :param u32 max_way_size:
        the maximum size in bytes for the cache ways

.. This file was automatic generated / don't edit.

