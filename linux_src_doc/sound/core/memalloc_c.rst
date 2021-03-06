.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/core/memalloc.c

.. _`snd_malloc_pages`:

snd_malloc_pages
================

.. c:function:: void *snd_malloc_pages(size_t size, gfp_t gfp_flags)

    allocate pages with the given size

    :param size:
        the size to allocate in bytes
    :type size: size_t

    :param gfp_flags:
        the allocation conditions, GFP_XXX
    :type gfp_flags: gfp_t

.. _`snd_malloc_pages.description`:

Description
-----------

Allocates the physically contiguous pages with the given size.

.. _`snd_malloc_pages.return`:

Return
------

The pointer of the buffer, or \ ``NULL``\  if no enough memory.

.. _`snd_free_pages`:

snd_free_pages
==============

.. c:function:: void snd_free_pages(void *ptr, size_t size)

    release the pages

    :param ptr:
        the buffer pointer to release
    :type ptr: void \*

    :param size:
        the allocated buffer size
    :type size: size_t

.. _`snd_free_pages.description`:

Description
-----------

Releases the buffer allocated via \ :c:func:`snd_malloc_pages`\ .

.. _`snd_malloc_dev_iram`:

snd_malloc_dev_iram
===================

.. c:function:: void snd_malloc_dev_iram(struct snd_dma_buffer *dmab, size_t size)

    allocate memory from on-chip internal ram

    :param dmab:
        buffer allocation record to store the allocated data
    :type dmab: struct snd_dma_buffer \*

    :param size:
        number of bytes to allocate from the iram
    :type size: size_t

.. _`snd_malloc_dev_iram.description`:

Description
-----------

This function requires iram phandle provided via of_node

.. _`snd_free_dev_iram`:

snd_free_dev_iram
=================

.. c:function:: void snd_free_dev_iram(struct snd_dma_buffer *dmab)

    free allocated specific memory from on-chip internal ram

    :param dmab:
        buffer allocation record to store the allocated data
    :type dmab: struct snd_dma_buffer \*

.. _`snd_dma_alloc_pages`:

snd_dma_alloc_pages
===================

.. c:function:: int snd_dma_alloc_pages(int type, struct device *device, size_t size, struct snd_dma_buffer *dmab)

    allocate the buffer area according to the given type

    :param type:
        the DMA buffer type
    :type type: int

    :param device:
        the device pointer
    :type device: struct device \*

    :param size:
        the buffer size to allocate
    :type size: size_t

    :param dmab:
        buffer allocation record to store the allocated data
    :type dmab: struct snd_dma_buffer \*

.. _`snd_dma_alloc_pages.description`:

Description
-----------

Calls the memory-allocator function for the corresponding
buffer type.

.. _`snd_dma_alloc_pages.return`:

Return
------

Zero if the buffer with the given size is allocated successfully,
otherwise a negative value on error.

.. _`snd_dma_alloc_pages_fallback`:

snd_dma_alloc_pages_fallback
============================

.. c:function:: int snd_dma_alloc_pages_fallback(int type, struct device *device, size_t size, struct snd_dma_buffer *dmab)

    allocate the buffer area according to the given type with fallback

    :param type:
        the DMA buffer type
    :type type: int

    :param device:
        the device pointer
    :type device: struct device \*

    :param size:
        the buffer size to allocate
    :type size: size_t

    :param dmab:
        buffer allocation record to store the allocated data
    :type dmab: struct snd_dma_buffer \*

.. _`snd_dma_alloc_pages_fallback.description`:

Description
-----------

Calls the memory-allocator function for the corresponding
buffer type.  When no space is left, this function reduces the size and
tries to allocate again.  The size actually allocated is stored in
res_size argument.

.. _`snd_dma_alloc_pages_fallback.return`:

Return
------

Zero if the buffer with the given size is allocated successfully,
otherwise a negative value on error.

.. _`snd_dma_free_pages`:

snd_dma_free_pages
==================

.. c:function:: void snd_dma_free_pages(struct snd_dma_buffer *dmab)

    release the allocated buffer

    :param dmab:
        the buffer allocation record to release
    :type dmab: struct snd_dma_buffer \*

.. _`snd_dma_free_pages.description`:

Description
-----------

Releases the allocated buffer via \ :c:func:`snd_dma_alloc_pages`\ .

.. This file was automatic generated / don't edit.

