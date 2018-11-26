.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/fsl/mpc5200_dma.c

.. _`psc_dma_bcom_enqueue_next_buffer`:

psc_dma_bcom_enqueue_next_buffer
================================

.. c:function:: void psc_dma_bcom_enqueue_next_buffer(struct psc_dma_stream *s)

    Enqueue another audio buffer

    :param s:
        pointer to stream private data structure
    :type s: struct psc_dma_stream \*

.. _`psc_dma_bcom_enqueue_next_buffer.description`:

Description
-----------

Enqueues another audio period buffer into the bestcomm queue.

.. _`psc_dma_bcom_enqueue_next_buffer.note`:

Note
----

The routine must only be called when there is space available in
the queue.  Otherwise the enqueue will fail and the audio ring buffer
will get out of sync

.. _`psc_dma_trigger`:

psc_dma_trigger
===============

.. c:function:: int psc_dma_trigger(struct snd_pcm_substream *substream, int cmd)

    start and stop the DMA transfer.

    :param substream:
        *undescribed*
    :type substream: struct snd_pcm_substream \*

    :param cmd:
        *undescribed*
    :type cmd: int

.. _`psc_dma_trigger.description`:

Description
-----------

This function is called by ALSA to start, stop, pause, and resume the DMA
transfer of data.

.. This file was automatic generated / don't edit.

