.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soc/fsl/qe/qe_common.c

.. _`cpm_muram_free`:

cpm_muram_free
==============

.. c:function:: int cpm_muram_free(unsigned long offset)

    free a chunk of multi-user ram

    :param unsigned long offset:
        The beginning of the chunk as returned by \ :c:func:`cpm_muram_alloc`\ .

.. _`cpm_muram_addr`:

cpm_muram_addr
==============

.. c:function:: void __iomem *cpm_muram_addr(unsigned long offset)

    turn a muram offset into a virtual address

    :param unsigned long offset:
        muram offset to convert

.. _`cpm_muram_dma`:

cpm_muram_dma
=============

.. c:function:: dma_addr_t cpm_muram_dma(void __iomem *addr)

    turn a muram virtual address into a DMA address

    :param void __iomem \*addr:
        *undescribed*

.. This file was automatic generated / don't edit.

