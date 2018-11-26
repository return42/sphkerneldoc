.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/atmel/atmel-pcm-dma.c

.. _`atmel_pcm_dma_irq`:

atmel_pcm_dma_irq
=================

.. c:function:: void atmel_pcm_dma_irq(u32 ssc_sr, struct snd_pcm_substream *substream)

    SSC interrupt handler for DMAENGINE enabled SSC

    :param ssc_sr:
        *undescribed*
    :type ssc_sr: u32

    :param substream:
        *undescribed*
    :type substream: struct snd_pcm_substream \*

.. _`atmel_pcm_dma_irq.description`:

Description
-----------

We use DMAENGINE to send/receive data to/from SSC so this ISR is only to
check if any overrun occured.

.. This file was automatic generated / don't edit.

