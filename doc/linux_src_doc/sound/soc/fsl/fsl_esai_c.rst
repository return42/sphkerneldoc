.. -*- coding: utf-8; mode: rst -*-

==========
fsl_esai.c
==========


.. _`fsl_esai_divisor_cal`:

fsl_esai_divisor_cal
====================

.. c:function:: int fsl_esai_divisor_cal (struct snd_soc_dai *dai, bool tx, u32 ratio, bool usefp, u32 fp)

    :param struct snd_soc_dai \*dai:

        *undescribed*

    :param bool tx:
        current setting is for playback or capture

    :param u32 ratio:
        desired overall ratio for the paticipating dividers

    :param bool usefp:
        for HCK setting, there is no need to set fp divider

    :param u32 fp:
        bypass other dividers by setting fp directly if fp != 0



.. _`fsl_esai_divisor_cal.description`:

Description
-----------

supposed to be called in :c:func:`set_dai_sysclk` and :c:func:`set_bclk`.



.. _`fsl_esai_set_dai_sysclk`:

fsl_esai_set_dai_sysclk
=======================

.. c:function:: int fsl_esai_set_dai_sysclk (struct snd_soc_dai *dai, int clk_id, unsigned int freq, int dir)

    :param struct snd_soc_dai \*dai:

        *undescribed*

    :param int clk_id:

        *undescribed*

    :param unsigned int freq:

        *undescribed*

    :param int dir:

        *undescribed*



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

.. c:function:: int fsl_esai_set_bclk (struct snd_soc_dai *dai, bool tx, u32 freq)

    :param struct snd_soc_dai \*dai:

        *undescribed*

    :param bool tx:

        *undescribed*

    :param u32 freq:

        *undescribed*

