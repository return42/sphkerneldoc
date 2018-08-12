.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/codecs/sta32x.c

.. _`sta32x_set_dai_sysclk`:

sta32x_set_dai_sysclk
=====================

.. c:function:: int sta32x_set_dai_sysclk(struct snd_soc_dai *codec_dai, int clk_id, unsigned int freq, int dir)

    configure MCLK

    :param struct snd_soc_dai \*codec_dai:
        the codec DAI

    :param int clk_id:
        the clock ID (ignored)

    :param unsigned int freq:
        the MCLK input frequency

    :param int dir:
        the clock direction (ignored)

.. _`sta32x_set_dai_sysclk.description`:

Description
-----------

The value of MCLK is used to determine which sample rates are supported
by the STA32X, based on the mclk_ratios table.

This function must be called by the machine driver's 'startup' function,
otherwise the list of supported sample rates will not be available in
time for ALSA.

For setups with variable MCLKs, pass 0 as 'freq' argument. This will cause
theoretically possible sample rates to be enabled. Call it again with a
proper value set one the external clock is set (most probably you would do
that from a machine's driver 'hw_param' hook.

.. _`sta32x_set_dai_fmt`:

sta32x_set_dai_fmt
==================

.. c:function:: int sta32x_set_dai_fmt(struct snd_soc_dai *codec_dai, unsigned int fmt)

    configure the codec for the selected audio format

    :param struct snd_soc_dai \*codec_dai:
        the codec DAI

    :param unsigned int fmt:
        a SND_SOC_DAIFMT_x value indicating the data format

.. _`sta32x_set_dai_fmt.description`:

Description
-----------

This function takes a bitmask of SND_SOC_DAIFMT_x bits and programs the
codec accordingly.

.. _`sta32x_hw_params`:

sta32x_hw_params
================

.. c:function:: int sta32x_hw_params(struct snd_pcm_substream *substream, struct snd_pcm_hw_params *params, struct snd_soc_dai *dai)

    program the STA32X with the given hardware parameters.

    :param struct snd_pcm_substream \*substream:
        the audio stream

    :param struct snd_pcm_hw_params \*params:
        the hardware parameters to set

    :param struct snd_soc_dai \*dai:
        the SOC DAI (ignored)

.. _`sta32x_hw_params.description`:

Description
-----------

This function programs the hardware with the values provided.
Specifically, the sample rate and the data format.

.. _`sta32x_set_bias_level`:

sta32x_set_bias_level
=====================

.. c:function:: int sta32x_set_bias_level(struct snd_soc_component *component, enum snd_soc_bias_level level)

    DAPM callback

    :param struct snd_soc_component \*component:
        the component device

    :param enum snd_soc_bias_level level:
        DAPM power level

.. _`sta32x_set_bias_level.description`:

Description
-----------

This is called by ALSA to put the component into low power mode
or to wake it up.  If the component is powered off completely
all registers must be restored after power on.

.. This file was automatic generated / don't edit.

