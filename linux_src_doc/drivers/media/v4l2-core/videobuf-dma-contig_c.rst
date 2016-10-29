.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/v4l2-core/videobuf-dma-contig.c

.. _`videobuf_dma_contig_user_put`:

videobuf_dma_contig_user_put
============================

.. c:function:: void videobuf_dma_contig_user_put(struct videobuf_dma_contig_memory *mem)

    reset pointer to user space buffer

    :param struct videobuf_dma_contig_memory \*mem:
        per-buffer private videobuf-dma-contig data

.. _`videobuf_dma_contig_user_put.description`:

Description
-----------

This function resets the user space pointer

.. _`videobuf_dma_contig_user_get`:

videobuf_dma_contig_user_get
============================

.. c:function:: int videobuf_dma_contig_user_get(struct videobuf_dma_contig_memory *mem, struct videobuf_buffer *vb)

    setup user space memory pointer

    :param struct videobuf_dma_contig_memory \*mem:
        per-buffer private videobuf-dma-contig data

    :param struct videobuf_buffer \*vb:
        video buffer to map

.. _`videobuf_dma_contig_user_get.description`:

Description
-----------

This function validates and sets up a pointer to user space memory.
Only physically contiguous pfn-mapped memory is accepted.

Returns 0 if successful.

.. This file was automatic generated / don't edit.
