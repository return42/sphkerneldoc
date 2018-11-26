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

    :param irq:
        *undescribed*
    :type irq: int

    :param dev_id:
        *undescribed*
    :type dev_id: void \*

.. _`fsl_ssi_config_enable`:

fsl_ssi_config_enable
=====================

.. c:function:: void fsl_ssi_config_enable(struct fsl_ssi *ssi, bool tx)

    :param ssi:
        *undescribed*
    :type ssi: struct fsl_ssi \*

    :param tx:
        *undescribed*
    :type tx: bool

.. _`fsl_ssi_config_enable.notes`:

Notes
-----

1) For offline_config SoCs, enable all necessary bits of both streams
when 1st stream starts, even if the opposite stream will not start
2) It also clears FIFO before setting regvals; SOR is safe to set online

.. _`_ssi_xor_shared_bits`:

\_ssi_xor_shared_bits
=====================

.. c:function::  _ssi_xor_shared_bits( vals,  avals,  aactive)

    :param vals:
        regvals of the current stream
    :type vals: 

    :param avals:
        regvals of the opposite stream
    :type avals: 

    :param aactive:
        active state of the opposite stream
    :type aactive: 

.. _`_ssi_xor_shared_bits.description`:

Description
-----------

When both streams are active, disabling some bits for the current stream
might break the other stream if these bits are used by it.

1) XOR vals and avals to get the differences if the other stream is active;
Otherwise, return current vals if the other stream is not active
2) AND the result of 1) with the current vals

.. _`fsl_ssi_config_disable`:

fsl_ssi_config_disable
======================

.. c:function:: void fsl_ssi_config_disable(struct fsl_ssi *ssi, bool tx)

    :param ssi:
        *undescribed*
    :type ssi: struct fsl_ssi \*

    :param tx:
        *undescribed*
    :type tx: bool

.. _`fsl_ssi_config_disable.notes`:

Notes
-----

1) For offline_config SoCs, to avoid online reconfigurations, disable all
bits of both streams at once when the last stream is abort to end
2) It also clears FIFO after unsetting regvals; SOR is safe to set online

.. _`fsl_ssi_setup_regvals`:

fsl_ssi_setup_regvals
=====================

.. c:function:: void fsl_ssi_setup_regvals(struct fsl_ssi *ssi)

    :param ssi:
        *undescribed*
    :type ssi: struct fsl_ssi \*

.. _`fsl_ssi_set_bclk`:

fsl_ssi_set_bclk
================

.. c:function:: int fsl_ssi_set_bclk(struct snd_pcm_substream *substream, struct snd_soc_dai *dai, struct snd_pcm_hw_params *hw_params)

    :param substream:
        *undescribed*
    :type substream: struct snd_pcm_substream \*

    :param dai:
        *undescribed*
    :type dai: struct snd_soc_dai \*

    :param hw_params:
        *undescribed*
    :type hw_params: struct snd_pcm_hw_params \*

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

    :param substream:
        *undescribed*
    :type substream: struct snd_pcm_substream \*

    :param hw_params:
        *undescribed*
    :type hw_params: struct snd_pcm_hw_params \*

    :param dai:
        *undescribed*
    :type dai: struct snd_soc_dai \*

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

    :param dai:
        *undescribed*
    :type dai: struct snd_soc_dai \*

    :param fmt:
        *undescribed*
    :type fmt: unsigned int

.. _`fsl_ssi_set_dai_tdm_slot`:

fsl_ssi_set_dai_tdm_slot
========================

.. c:function:: int fsl_ssi_set_dai_tdm_slot(struct snd_soc_dai *dai, u32 tx_mask, u32 rx_mask, int slots, int slot_width)

    :param dai:
        *undescribed*
    :type dai: struct snd_soc_dai \*

    :param tx_mask:
        *undescribed*
    :type tx_mask: u32

    :param rx_mask:
        *undescribed*
    :type rx_mask: u32

    :param slots:
        *undescribed*
    :type slots: int

    :param slot_width:
        *undescribed*
    :type slot_width: int

.. _`fsl_ssi_trigger`:

fsl_ssi_trigger
===============

.. c:function:: int fsl_ssi_trigger(struct snd_pcm_substream *substream, int cmd, struct snd_soc_dai *dai)

    :param substream:
        *undescribed*
    :type substream: struct snd_pcm_substream \*

    :param cmd:
        *undescribed*
    :type cmd: int

    :param dai:
        *undescribed*
    :type dai: struct snd_soc_dai \*

.. _`fsl_ssi_trigger.description`:

Description
-----------

The DMA channel is in external master start and pause mode, which
means the SSI completely controls the flow of data.

.. _`fsl_ssi_hw_init`:

fsl_ssi_hw_init
===============

.. c:function:: int fsl_ssi_hw_init(struct fsl_ssi *ssi)

    :param ssi:
        *undescribed*
    :type ssi: struct fsl_ssi \*

.. _`fsl_ssi_hw_clean`:

fsl_ssi_hw_clean
================

.. c:function:: void fsl_ssi_hw_clean(struct fsl_ssi *ssi)

    :param ssi:
        *undescribed*
    :type ssi: struct fsl_ssi \*

.. _`make_lowercase`:

make_lowercase
==============

.. c:function:: void make_lowercase(char *s)

    case

    :param s:
        *undescribed*
    :type s: char \*

.. This file was automatic generated / don't edit.

