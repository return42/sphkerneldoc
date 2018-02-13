.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mm/cache-uniphier.c

.. _`__uniphier_cache_sync`:

\__uniphier_cache_sync
======================

.. c:function:: void __uniphier_cache_sync(struct uniphier_cache_data *data)

    perform a sync point for a particular cache level

    :param struct uniphier_cache_data \*data:
        cache controller specific data

.. _`__uniphier_cache_maint_common`:

\__uniphier_cache_maint_common
==============================

.. c:function:: void __uniphier_cache_maint_common(struct uniphier_cache_data *data, unsigned long start, unsigned long size, u32 operation)

    run a queue operation for a particular level

    :param struct uniphier_cache_data \*data:
        cache controller specific data

    :param unsigned long start:
        start address of range operation (don't care for "all" operation)

    :param unsigned long size:
        data size of range operation (don't care for "all" operation)

    :param u32 operation:
        flags to specify the desired cache operation

.. This file was automatic generated / don't edit.

