.. -*- coding: utf-8; mode: rst -*-

=============
mpc5200_dma.c
=============


.. _`psc_dma_bcom_enqueue_next_buffer`:

psc_dma_bcom_enqueue_next_buffer
================================

.. c:function:: void psc_dma_bcom_enqueue_next_buffer (struct psc_dma_stream *s)

    Enqueue another audio buffer

    :param struct psc_dma_stream \*s:
        pointer to stream private data structure



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

.. c:function:: int psc_dma_trigger (struct snd_pcm_substream *substream, int cmd)

    :param struct snd_pcm_substream \*substream:

        *undescribed*

    :param int cmd:

        *undescribed*



.. _`psc_dma_trigger.description`:

Description
-----------


This function is called by ALSA to start, stop, pause, and resume the DMA
transfer of data.

