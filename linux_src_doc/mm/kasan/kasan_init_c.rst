.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/kasan/kasan_init.c

.. _`kasan_populate_zero_shadow`:

kasan_populate_zero_shadow
==========================

.. c:function:: int __ref kasan_populate_zero_shadow(const void *shadow_start, const void *shadow_end)

    populate shadow memory region with kasan_zero_page \ ``shadow_start``\  - start of the memory range to populate \ ``shadow_end``\    - end of the memory range to populate

    :param shadow_start:
        *undescribed*
    :type shadow_start: const void \*

    :param shadow_end:
        *undescribed*
    :type shadow_end: const void \*

.. This file was automatic generated / don't edit.

