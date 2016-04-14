.. -*- coding: utf-8; mode: rst -*-

========
isadma.c
========

.. _`snd_dma_program`:

snd_dma_program
===============

.. c:function:: void snd_dma_program (unsigned long dma, unsigned long addr, unsigned int size, unsigned short mode)

    program an ISA DMA transfer

    :param unsigned long dma:
        the dma number

    :param unsigned long addr:
        the physical address of the buffer

    :param unsigned int size:
        the DMA transfer size

    :param unsigned short mode:
        the DMA transfer mode, DMA_MODE_XXX


.. _`snd_dma_program.description`:

Description
-----------

Programs an ISA DMA transfer for the given buffer.


.. _`snd_dma_disable`:

snd_dma_disable
===============

.. c:function:: void snd_dma_disable (unsigned long dma)

    stop the ISA DMA transfer

    :param unsigned long dma:
        the dma number


.. _`snd_dma_disable.description`:

Description
-----------

Stops the ISA DMA transfer.


.. _`snd_dma_pointer`:

snd_dma_pointer
===============

.. c:function:: unsigned int snd_dma_pointer (unsigned long dma, unsigned int size)

    return the current pointer to DMA transfer buffer in bytes

    :param unsigned long dma:
        the dma number

    :param unsigned int size:
        the dma transfer size


.. _`snd_dma_pointer.description`:

Description
-----------

Return: The current pointer in DMA transfer buffer in bytes.

