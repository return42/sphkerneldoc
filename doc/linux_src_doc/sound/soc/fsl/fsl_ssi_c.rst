.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/fsl/fsl_ssi.c

.. _`fslssi_i2s_rates`:

FSLSSI_I2S_RATES
================

.. c:function::  FSLSSI_I2S_RATES()

    sample rates supported by the I2S

.. _`fslssi_i2s_rates.description`:

Description
-----------

This driver currently only supports the SSI running in I2S slave mode,
which means the codec determines the sample rate.  Therefore, we tell
ALSA that we support all rates and let the codec driver decide what rates
are really supported.

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

    SSI interrupt handler

    :param int irq:
        IRQ of the SSI device

    :param void \*dev_id:
        pointer to the ssi_private structure for this SSI device

.. _`fsl_ssi_isr.description`:

Description
-----------

Although it's possible to use the interrupt handler to send and receive
data to/from the SSI, we use the DMA instead.  Programming is more
complicated, but the performance is much better.

This interrupt handler is used only to gather statistics.

.. _`fsl_ssi_startup`:

fsl_ssi_startup
===============

.. c:function:: int fsl_ssi_startup(struct snd_pcm_substream *substream, struct snd_soc_dai *dai)

    create a new substream

    :param struct snd_pcm_substream \*substream:
        *undescribed*

    :param struct snd_soc_dai \*dai:
        *undescribed*

.. _`fsl_ssi_startup.description`:

Description
-----------

This is the first function called when a stream is opened.

If this is the first stream open, then grab the IRQ and program most of
the SSI registers.

.. _`fsl_ssi_shutdown`:

fsl_ssi_shutdown
================

.. c:function:: void fsl_ssi_shutdown(struct snd_pcm_substream *substream, struct snd_soc_dai *dai)

    shutdown the SSI

    :param struct snd_pcm_substream \*substream:
        *undescribed*

    :param struct snd_soc_dai \*dai:
        *undescribed*

.. _`fsl_ssi_set_bclk`:

fsl_ssi_set_bclk
================

.. c:function:: int fsl_ssi_set_bclk(struct snd_pcm_substream *substream, struct snd_soc_dai *cpu_dai, struct snd_pcm_hw_params *hw_params)

    configure Digital Audio Interface bit clock

    :param struct snd_pcm_substream \*substream:
        *undescribed*

    :param struct snd_soc_dai \*cpu_dai:
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

Output BCLK frequency = samplerate \* 32 (fixed) \* channels

.. _`fsl_ssi_set_bclk.dir`:

dir
---

SND_SOC_CLOCK_OUT -> TxBCLK, SND_SOC_CLOCK_IN -> RxBCLK.

.. _`fsl_ssi_hw_params`:

fsl_ssi_hw_params
=================

.. c:function:: int fsl_ssi_hw_params(struct snd_pcm_substream *substream, struct snd_pcm_hw_params *hw_params, struct snd_soc_dai *cpu_dai)

    program the sample size

    :param struct snd_pcm_substream \*substream:
        *undescribed*

    :param struct snd_pcm_hw_params \*hw_params:
        *undescribed*

    :param struct snd_soc_dai \*cpu_dai:
        *undescribed*

.. _`fsl_ssi_hw_params.description`:

Description
-----------

Most of the SSI registers have been programmed in the startup function,
but the word length must be programmed here.  Unfortunately, programming
the SxCCR.WL bits requires the SSI to be temporarily disabled.  This can
cause a problem with supporting simultaneous playback and capture.  If
the SSI is already playing a stream, then that stream may be temporarily
stopped when you start capture.

.. _`fsl_ssi_hw_params.note`:

Note
----

The SxCCR.DC and SxCCR.PM bits are only used if the SSI is the
clock master.

.. _`fsl_ssi_set_dai_fmt`:

fsl_ssi_set_dai_fmt
===================

.. c:function:: int fsl_ssi_set_dai_fmt(struct snd_soc_dai *cpu_dai, unsigned int fmt)

    configure Digital Audio Interface Format.

    :param struct snd_soc_dai \*cpu_dai:
        *undescribed*

    :param unsigned int fmt:
        *undescribed*

.. _`fsl_ssi_set_dai_tdm_slot`:

fsl_ssi_set_dai_tdm_slot
========================

.. c:function:: int fsl_ssi_set_dai_tdm_slot(struct snd_soc_dai *cpu_dai, u32 tx_mask, u32 rx_mask, int slots, int slot_width)

    set TDM slot number

    :param struct snd_soc_dai \*cpu_dai:
        *undescribed*

    :param u32 tx_mask:
        *undescribed*

    :param u32 rx_mask:
        *undescribed*

    :param int slots:
        *undescribed*

    :param int slot_width:
        *undescribed*

.. _`fsl_ssi_set_dai_tdm_slot.note`:

Note
----

This function can be only called when using SSI as DAI master

.. _`fsl_ssi_trigger`:

fsl_ssi_trigger
===============

.. c:function:: int fsl_ssi_trigger(struct snd_pcm_substream *substream, int cmd, struct snd_soc_dai *dai)

    start and stop the DMA transfer.

    :param struct snd_pcm_substream \*substream:
        *undescribed*

    :param int cmd:
        *undescribed*

    :param struct snd_soc_dai \*dai:
        *undescribed*

.. _`fsl_ssi_trigger.description`:

Description
-----------

This function is called by ALSA to start, stop, pause, and resume the DMA
transfer of data.

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

