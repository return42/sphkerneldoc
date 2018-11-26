.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/codecs/sta350.c

.. _`sta350_set_dai_sysclk`:

sta350_set_dai_sysclk
=====================

.. c:function:: int sta350_set_dai_sysclk(struct snd_soc_dai *codec_dai, int clk_id, unsigned int freq, int dir)

    configure MCLK

    :param codec_dai:
        the codec DAI
    :type codec_dai: struct snd_soc_dai \*

    :param clk_id:
        the clock ID (ignored)
    :type clk_id: int

    :param freq:
        the MCLK input frequency
    :type freq: unsigned int

    :param dir:
        the clock direction (ignored)
    :type dir: int

.. _`sta350_set_dai_sysclk.description`:

Description
-----------

The value of MCLK is used to determine which sample rates are supported
by the STA350, based on the mcs_ratio_table.

This function must be called by the machine driver's 'startup' function,
otherwise the list of supported sample rates will not be available in
time for ALSA.

.. _`sta350_set_dai_fmt`:

sta350_set_dai_fmt
==================

.. c:function:: int sta350_set_dai_fmt(struct snd_soc_dai *codec_dai, unsigned int fmt)

    configure the codec for the selected audio format

    :param codec_dai:
        the codec DAI
    :type codec_dai: struct snd_soc_dai \*

    :param fmt:
        a SND_SOC_DAIFMT_x value indicating the data format
    :type fmt: unsigned int

.. _`sta350_set_dai_fmt.description`:

Description
-----------

This function takes a bitmask of SND_SOC_DAIFMT_x bits and programs the
codec accordingly.

.. _`sta350_hw_params`:

sta350_hw_params
================

.. c:function:: int sta350_hw_params(struct snd_pcm_substream *substream, struct snd_pcm_hw_params *params, struct snd_soc_dai *dai)

    program the STA350 with the given hardware parameters.

    :param substream:
        the audio stream
    :type substream: struct snd_pcm_substream \*

    :param params:
        the hardware parameters to set
    :type params: struct snd_pcm_hw_params \*

    :param dai:
        the SOC DAI (ignored)
    :type dai: struct snd_soc_dai \*

.. _`sta350_hw_params.description`:

Description
-----------

This function programs the hardware with the values provided.
Specifically, the sample rate and the data format.

.. _`sta350_set_bias_level`:

sta350_set_bias_level
=====================

.. c:function:: int sta350_set_bias_level(struct snd_soc_component *component, enum snd_soc_bias_level level)

    DAPM callback

    :param component:
        the component device
    :type component: struct snd_soc_component \*

    :param level:
        DAPM power level
    :type level: enum snd_soc_bias_level

.. _`sta350_set_bias_level.description`:

Description
-----------

This is called by ALSA to put the component into low power mode
or to wake it up.  If the component is powered off completely
all registers must be restored after power on.

.. This file was automatic generated / don't edit.

