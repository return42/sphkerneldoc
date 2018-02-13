.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/fsl/fsl_ssi.c

.. _`fslssi_i2s_formats`:

FSLSSI_I2S_FORMATS
==================

.. c:function::  FSLSSI_I2S_FORMATS()

    audio formats supported by the SSI

.. _`fslssi_i2s_formats.description`:

Description
-----------

The SSI has a limitation in that the samples must be in the same byte
order as the host CPU.  This is because when multiple bytes are written
to the STX register, the bytes and bits must be written in the same
order.  The STX is a shift register, so all the bits need to be aligned
(bit-endianness must match byte-endianness).  Processors typically write
the bits within a byte in the same order that the bytes of a word are
written in.  So if the host CPU is big-endian, then only big-endian
samples will be written to STX properly.

.. _`fsl_ssi_isr`:

fsl_ssi_isr
===========

.. c:function:: irqreturn_t fsl_ssi_isr(int irq, void *dev_id)

    :param int irq:
        *undescribed*

    :param void \*dev_id:
        *undescribed*

.. _`fsl_ssi_rxtx_config`:

fsl_ssi_rxtx_config
===================

.. c:function:: void fsl_ssi_rxtx_config(struct fsl_ssi *ssi, bool enable)

    :param struct fsl_ssi \*ssi:
        *undescribed*

    :param bool enable:
        *undescribed*

.. _`fsl_ssi_fifo_clear`:

fsl_ssi_fifo_clear
==================

.. c:function:: void fsl_ssi_fifo_clear(struct fsl_ssi *ssi, bool is_rx)

    :param struct fsl_ssi \*ssi:
        *undescribed*

    :param bool is_rx:
        *undescribed*

.. _`fsl_ssi_disable_val`:

fsl_ssi_disable_val
===================

.. c:function::  fsl_ssi_disable_val( vals_disable,  vals_stream,  stream_active)

    getting disabled. This keeps the bits enabled that are necessary for the second stream to work if 'stream_active' is true.

    :param  vals_disable:
        *undescribed*

    :param  vals_stream:
        *undescribed*

    :param  stream_active:
        *undescribed*

.. _`fsl_ssi_disable_val.detailed-calculation`:

Detailed calculation
--------------------

These are the values that need to be active after disabling. For non-active
second stream, this is 0:
vals_stream \* !!stream_active

The following computes the overall differences between the setup for the
to-disable stream and the active stream, a simple XOR:
vals_disable ^ (vals_stream \* !!(stream_active))

The full expression adds a mask on all values we care about

.. _`fsl_ssi_config`:

fsl_ssi_config
==============

.. c:function:: void fsl_ssi_config(struct fsl_ssi *ssi, bool enable, struct fsl_ssi_regvals *vals)

    :param struct fsl_ssi \*ssi:
        *undescribed*

    :param bool enable:
        *undescribed*

    :param struct fsl_ssi_regvals \*vals:
        *undescribed*

.. _`fsl_ssi_setup_regvals`:

fsl_ssi_setup_regvals
=====================

.. c:function:: void fsl_ssi_setup_regvals(struct fsl_ssi *ssi)

    :param struct fsl_ssi \*ssi:
        *undescribed*

.. _`fsl_ssi_set_bclk`:

fsl_ssi_set_bclk
================

.. c:function:: int fsl_ssi_set_bclk(struct snd_pcm_substream *substream, struct snd_soc_dai *dai, struct snd_pcm_hw_params *hw_params)

    :param struct snd_pcm_substream \*substream:
        *undescribed*

    :param struct snd_soc_dai \*dai:
        *undescribed*

    :param struct snd_pcm_hw_params \*hw_params:
        *undescribed*

.. _`fsl_ssi_set_bclk.note`:

Note
----

This function can be only called when using SSI as DAI master

.. _`fsl_ssi_set_bclk.freq`:

freq
----

Output BCLK frequency = samplerate \* slots \* slot_width
(In 2-channel I2S Master mode, slot_width is fixed 32)

.. _`fsl_ssi_hw_params`:

fsl_ssi_hw_params
=================

.. c:function:: int fsl_ssi_hw_params(struct snd_pcm_substream *substream, struct snd_pcm_hw_params *hw_params, struct snd_soc_dai *dai)

    :param struct snd_pcm_substream \*substream:
        *undescribed*

    :param struct snd_pcm_hw_params \*hw_params:
        *undescribed*

    :param struct snd_soc_dai \*dai:
        *undescribed*

.. _`fsl_ssi_hw_params.notes`:

Notes
-----

1) SxCCR.WL bits are critical bits that require SSI to be temporarily
disabled on offline_config SoCs. Even for online configurable SoCs
running in synchronous mode (both TX and RX use STCCR), it is not
safe to re-configure them when both two streams start running.
2) SxCCR.PM, SxCCR.DIV2 and SxCCR.PSR bits will be configured in the
\ :c:func:`fsl_ssi_set_bclk`\  if SSI is the DAI clock master.

.. _`fsl_ssi_set_dai_fmt`:

fsl_ssi_set_dai_fmt
===================

.. c:function:: int fsl_ssi_set_dai_fmt(struct snd_soc_dai *dai, unsigned int fmt)

    :param struct snd_soc_dai \*dai:
        *undescribed*

    :param unsigned int fmt:
        *undescribed*

.. _`fsl_ssi_set_dai_tdm_slot`:

fsl_ssi_set_dai_tdm_slot
========================

.. c:function:: int fsl_ssi_set_dai_tdm_slot(struct snd_soc_dai *dai, u32 tx_mask, u32 rx_mask, int slots, int slot_width)

    :param struct snd_soc_dai \*dai:
        *undescribed*

    :param u32 tx_mask:
        *undescribed*

    :param u32 rx_mask:
        *undescribed*

    :param int slots:
        *undescribed*

    :param int slot_width:
        *undescribed*

.. _`fsl_ssi_trigger`:

fsl_ssi_trigger
===============

.. c:function:: int fsl_ssi_trigger(struct snd_pcm_substream *substream, int cmd, struct snd_soc_dai *dai)

    :param struct snd_pcm_substream \*substream:
        *undescribed*

    :param int cmd:
        *undescribed*

    :param struct snd_soc_dai \*dai:
        *undescribed*

.. _`fsl_ssi_trigger.description`:

Description
-----------

The DMA channel is in external master start and pause mode, which
means the SSI completely controls the flow of data.

.. _`make_lowercase`:

make_lowercase
==============

.. c:function:: void make_lowercase(char *s)

    case

    :param char \*s:
        *undescribed*

.. This file was automatic generated / don't edit.

