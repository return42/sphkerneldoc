.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/fsl/fsl_esai.c

.. _`fsl_esai_divisor_cal`:

fsl_esai_divisor_cal
====================

.. c:function:: int fsl_esai_divisor_cal(struct snd_soc_dai *dai, bool tx, u32 ratio, bool usefp, u32 fp)

    supposed to be called in \ :c:func:`set_dai_sysclk`\  and \ :c:func:`set_bclk`\ .

    :param dai:
        *undescribed*
    :type dai: struct snd_soc_dai \*

    :param tx:
        current setting is for playback or capture
    :type tx: bool

    :param ratio:
        desired overall ratio for the paticipating dividers
    :type ratio: u32

    :param usefp:
        for HCK setting, there is no need to set fp divider
    :type usefp: bool

    :param fp:
        bypass other dividers by setting fp directly if fp != 0
    :type fp: u32

.. _`fsl_esai_set_dai_sysclk`:

fsl_esai_set_dai_sysclk
=======================

.. c:function:: int fsl_esai_set_dai_sysclk(struct snd_soc_dai *dai, int clk_id, unsigned int freq, int dir)

    :param dai:
        *undescribed*
    :type dai: struct snd_soc_dai \*

    :param clk_id:
        *undescribed*
    :type clk_id: int

    :param freq:
        *undescribed*
    :type freq: unsigned int

    :param dir:
        *undescribed*
    :type dir: int

.. _`fsl_esai_set_dai_sysclk.clk_id`:

clk_id
------

The clock source of HCKT/HCKR
(Input from outside; output from inside, FSYS or EXTAL)

.. _`fsl_esai_set_dai_sysclk.freq`:

freq
----

The required clock rate of HCKT/HCKR

.. _`fsl_esai_set_dai_sysclk.dir`:

dir
---

The clock direction of HCKT/HCKR

.. _`fsl_esai_set_dai_sysclk.note`:

Note
----

If the direction is input, we do not care about clk_id.

.. _`fsl_esai_set_bclk`:

fsl_esai_set_bclk
=================

.. c:function:: int fsl_esai_set_bclk(struct snd_soc_dai *dai, bool tx, u32 freq)

    :param dai:
        *undescribed*
    :type dai: struct snd_soc_dai \*

    :param tx:
        *undescribed*
    :type tx: bool

    :param freq:
        *undescribed*
    :type freq: u32

.. This file was automatic generated / don't edit.

