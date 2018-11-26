.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/fsl/mpc5200_psc_i2s.c

.. _`psc_i2s_rates`:

PSC_I2S_RATES
=============

.. c:function::  PSC_I2S_RATES()

    sample rates supported by the I2S

.. _`psc_i2s_rates.description`:

Description
-----------

This driver currently only supports the PSC running in I2S slave mode,
which means the codec determines the sample rate.  Therefore, we tell
ALSA that we support all rates and let the codec driver decide what rates
are really supported.

.. _`psc_i2s_formats`:

PSC_I2S_FORMATS
===============

.. c:function::  PSC_I2S_FORMATS()

    audio formats supported by the PSC I2S mode

.. _`psc_i2s_set_sysclk`:

psc_i2s_set_sysclk
==================

.. c:function:: int psc_i2s_set_sysclk(struct snd_soc_dai *cpu_dai, int clk_id, unsigned int freq, int dir)

    set the clock frequency and direction

    :param cpu_dai:
        *undescribed*
    :type cpu_dai: struct snd_soc_dai \*

    :param clk_id:
        reserved, should be zero
    :type clk_id: int

    :param freq:
        the frequency of the given clock ID, currently ignored
    :type freq: unsigned int

    :param dir:
        SND_SOC_CLOCK_IN (clock slave) or SND_SOC_CLOCK_OUT (clock master)
    :type dir: int

.. _`psc_i2s_set_sysclk.description`:

Description
-----------

This function is called by the machine driver to tell us what the clock
frequency and direction are.

Currently, we only support operating as a clock slave (SND_SOC_CLOCK_IN),
and we don't care about the frequency.  Return an error if the direction
is not SND_SOC_CLOCK_IN.

.. _`psc_i2s_set_fmt`:

psc_i2s_set_fmt
===============

.. c:function:: int psc_i2s_set_fmt(struct snd_soc_dai *cpu_dai, unsigned int format)

    set the serial format.

    :param cpu_dai:
        *undescribed*
    :type cpu_dai: struct snd_soc_dai \*

    :param format:
        one of SND_SOC_DAIFMT_xxx
    :type format: unsigned int

.. _`psc_i2s_set_fmt.description`:

Description
-----------

This function is called by the machine driver to tell us what serial
format to use.

This driver only supports I2S mode.  Return an error if the format is
not SND_SOC_DAIFMT_I2S.

.. This file was automatic generated / don't edit.

