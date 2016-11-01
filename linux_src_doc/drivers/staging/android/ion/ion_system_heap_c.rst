.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/android/ion/ion_system_heap.c

.. _`alloc_buffer_page`:

alloc_buffer_page
=================

.. c:function:: struct page *alloc_buffer_page(struct ion_system_heap *heap, struct ion_buffer *buffer, unsigned long order)

    pool are all zeroed before. We need do cache clean for cached buffer. The uncached buffer are always non-cached since it's allocated. So no need for non-cached pages.

    :param struct ion_system_heap \*heap:
        *undescribed*

    :param struct ion_buffer \*buffer:
        *undescribed*

    :param unsigned long order:
        *undescribed*

.. This file was automatic generated / don't edit.

