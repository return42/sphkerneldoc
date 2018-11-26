.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/core/isadma.c

.. _`snd_dma_program`:

snd_dma_program
===============

.. c:function:: void snd_dma_program(unsigned long dma, unsigned long addr, unsigned int size, unsigned short mode)

    program an ISA DMA transfer

    :param dma:
        the dma number
    :type dma: unsigned long

    :param addr:
        the physical address of the buffer
    :type addr: unsigned long

    :param size:
        the DMA transfer size
    :type size: unsigned int

    :param mode:
        the DMA transfer mode, DMA_MODE_XXX
    :type mode: unsigned short

.. _`snd_dma_program.description`:

Description
-----------

Programs an ISA DMA transfer for the given buffer.

.. _`snd_dma_disable`:

snd_dma_disable
===============

.. c:function:: void snd_dma_disable(unsigned long dma)

    stop the ISA DMA transfer

    :param dma:
        the dma number
    :type dma: unsigned long

.. _`snd_dma_disable.description`:

Description
-----------

Stops the ISA DMA transfer.

.. _`snd_dma_pointer`:

snd_dma_pointer
===============

.. c:function:: unsigned int snd_dma_pointer(unsigned long dma, unsigned int size)

    return the current pointer to DMA transfer buffer in bytes

    :param dma:
        the dma number
    :type dma: unsigned long

    :param size:
        the dma transfer size
    :type size: unsigned int

.. _`snd_dma_pointer.return`:

Return
------

The current pointer in DMA transfer buffer in bytes.

.. This file was automatic generated / don't edit.

