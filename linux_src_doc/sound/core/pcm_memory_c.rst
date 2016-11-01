.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/core/pcm_memory.c

.. _`snd_pcm_lib_preallocate_free`:

snd_pcm_lib_preallocate_free
============================

.. c:function:: int snd_pcm_lib_preallocate_free(struct snd_pcm_substream *substream)

    release the preallocated buffer of the specified substream.

    :param struct snd_pcm_substream \*substream:
        the pcm substream instance

.. _`snd_pcm_lib_preallocate_free.description`:

Description
-----------

Releases the pre-allocated buffer of the given substream.

.. _`snd_pcm_lib_preallocate_free.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. _`snd_pcm_lib_preallocate_free_for_all`:

snd_pcm_lib_preallocate_free_for_all
====================================

.. c:function:: int snd_pcm_lib_preallocate_free_for_all(struct snd_pcm *pcm)

    release all pre-allocated buffers on the pcm

    :param struct snd_pcm \*pcm:
        the pcm instance

.. _`snd_pcm_lib_preallocate_free_for_all.description`:

Description
-----------

Releases all the pre-allocated buffers on the given pcm.

.. _`snd_pcm_lib_preallocate_free_for_all.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. _`snd_pcm_lib_preallocate_pages`:

snd_pcm_lib_preallocate_pages
=============================

.. c:function:: int snd_pcm_lib_preallocate_pages(struct snd_pcm_substream *substream, int type, struct device *data, size_t size, size_t max)

    pre-allocation for the given DMA type

    :param struct snd_pcm_substream \*substream:
        the pcm substream instance

    :param int type:
        DMA type (SNDRV_DMA_TYPE_*)

    :param struct device \*data:
        DMA type dependent data

    :param size_t size:
        the requested pre-allocation size in bytes

    :param size_t max:
        the max. allowed pre-allocation size

.. _`snd_pcm_lib_preallocate_pages.description`:

Description
-----------

Do pre-allocation for the given DMA buffer type.

.. _`snd_pcm_lib_preallocate_pages.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. _`snd_pcm_lib_preallocate_pages_for_all`:

snd_pcm_lib_preallocate_pages_for_all
=====================================

.. c:function:: int snd_pcm_lib_preallocate_pages_for_all(struct snd_pcm *pcm, int type, void *data, size_t size, size_t max)

    pre-allocation for continuous memory type (all substreams)

    :param struct snd_pcm \*pcm:
        the pcm instance

    :param int type:
        DMA type (SNDRV_DMA_TYPE_*)

    :param void \*data:
        DMA type dependent data

    :param size_t size:
        the requested pre-allocation size in bytes

    :param size_t max:
        the max. allowed pre-allocation size

.. _`snd_pcm_lib_preallocate_pages_for_all.description`:

Description
-----------

Do pre-allocation to all substreams of the given pcm for the
specified DMA type.

.. _`snd_pcm_lib_preallocate_pages_for_all.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. _`snd_pcm_sgbuf_ops_page`:

snd_pcm_sgbuf_ops_page
======================

.. c:function:: struct page *snd_pcm_sgbuf_ops_page(struct snd_pcm_substream *substream, unsigned long offset)

    get the page struct at the given offset

    :param struct snd_pcm_substream \*substream:
        the pcm substream instance

    :param unsigned long offset:
        the buffer offset

.. _`snd_pcm_sgbuf_ops_page.description`:

Description
-----------

Used as the page callback of PCM ops.

.. _`snd_pcm_sgbuf_ops_page.return`:

Return
------

The page struct at the given buffer offset. \ ``NULL``\  on failure.

.. _`snd_pcm_lib_malloc_pages`:

snd_pcm_lib_malloc_pages
========================

.. c:function:: int snd_pcm_lib_malloc_pages(struct snd_pcm_substream *substream, size_t size)

    allocate the DMA buffer

    :param struct snd_pcm_substream \*substream:
        the substream to allocate the DMA buffer to

    :param size_t size:
        the requested buffer size in bytes

.. _`snd_pcm_lib_malloc_pages.description`:

Description
-----------

Allocates the DMA buffer on the BUS type given earlier to
\ :c:func:`snd_pcm_lib_preallocate_xxx_pages`\ .

.. _`snd_pcm_lib_malloc_pages.return`:

Return
------

1 if the buffer is changed, 0 if not changed, or a negative
code on failure.

.. _`snd_pcm_lib_free_pages`:

snd_pcm_lib_free_pages
======================

.. c:function:: int snd_pcm_lib_free_pages(struct snd_pcm_substream *substream)

    release the allocated DMA buffer.

    :param struct snd_pcm_substream \*substream:
        the substream to release the DMA buffer

.. _`snd_pcm_lib_free_pages.description`:

Description
-----------

Releases the DMA buffer allocated via \ :c:func:`snd_pcm_lib_malloc_pages`\ .

.. _`snd_pcm_lib_free_pages.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. _`snd_pcm_lib_free_vmalloc_buffer`:

snd_pcm_lib_free_vmalloc_buffer
===============================

.. c:function:: int snd_pcm_lib_free_vmalloc_buffer(struct snd_pcm_substream *substream)

    free vmalloc buffer

    :param struct snd_pcm_substream \*substream:
        the substream with a buffer allocated by
        \ :c:func:`snd_pcm_lib_alloc_vmalloc_buffer`\ 

.. _`snd_pcm_lib_free_vmalloc_buffer.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. _`snd_pcm_lib_get_vmalloc_page`:

snd_pcm_lib_get_vmalloc_page
============================

.. c:function:: struct page *snd_pcm_lib_get_vmalloc_page(struct snd_pcm_substream *substream, unsigned long offset)

    map vmalloc buffer offset to page struct

    :param struct snd_pcm_substream \*substream:
        the substream with a buffer allocated by
        \ :c:func:`snd_pcm_lib_alloc_vmalloc_buffer`\ 

    :param unsigned long offset:
        offset in the buffer

.. _`snd_pcm_lib_get_vmalloc_page.description`:

Description
-----------

This function is to be used as the page callback in the PCM ops.

.. _`snd_pcm_lib_get_vmalloc_page.return`:

Return
------

The page struct, or \ ``NULL``\  on failure.

.. This file was automatic generated / don't edit.

