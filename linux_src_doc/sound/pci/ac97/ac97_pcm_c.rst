.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/pci/ac97/ac97_pcm.c

.. _`snd_ac97_set_rate`:

snd_ac97_set_rate
=================

.. c:function:: int snd_ac97_set_rate(struct snd_ac97 *ac97, int reg, unsigned int rate)

    change the rate of the given input/output.

    :param ac97:
        the ac97 instance
    :type ac97: struct snd_ac97 \*

    :param reg:
        the register to change
    :type reg: int

    :param rate:
        the sample rate to set
    :type rate: unsigned int

.. _`snd_ac97_set_rate.description`:

Description
-----------

Changes the rate of the given input/output on the codec.
If the codec doesn't support VAR, the rate must be 48000 (except
for SPDIF).

The valid registers are AC97_PMC_MIC_ADC_RATE,
AC97_PCM_FRONT_DAC_RATE, AC97_PCM_LR_ADC_RATE.
AC97_PCM_SURR_DAC_RATE and AC97_PCM_LFE_DAC_RATE are accepted
if the codec supports them.
AC97_SPDIF is accepted as a pseudo register to modify the SPDIF
status bits.

.. _`snd_ac97_set_rate.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. _`snd_ac97_pcm_assign`:

snd_ac97_pcm_assign
===================

.. c:function:: int snd_ac97_pcm_assign(struct snd_ac97_bus *bus, unsigned short pcms_count, const struct ac97_pcm *pcms)

    assign AC97 slots to given PCM streams

    :param bus:
        the ac97 bus instance
    :type bus: struct snd_ac97_bus \*

    :param pcms_count:
        count of PCMs to be assigned
    :type pcms_count: unsigned short

    :param pcms:
        PCMs to be assigned
    :type pcms: const struct ac97_pcm \*

.. _`snd_ac97_pcm_assign.description`:

Description
-----------

It assigns available AC97 slots for given PCMs. If none or only
some slots are available, pcm->xxx.slots and pcm->xxx.rslots[] members
are reduced and might be zero.

.. _`snd_ac97_pcm_assign.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. _`snd_ac97_pcm_open`:

snd_ac97_pcm_open
=================

.. c:function:: int snd_ac97_pcm_open(struct ac97_pcm *pcm, unsigned int rate, enum ac97_pcm_cfg cfg, unsigned short slots)

    opens the given AC97 pcm

    :param pcm:
        the ac97 pcm instance
    :type pcm: struct ac97_pcm \*

    :param rate:
        rate in Hz, if codec does not support VRA, this value must be 48000Hz
    :type rate: unsigned int

    :param cfg:
        output stream characteristics
    :type cfg: enum ac97_pcm_cfg

    :param slots:
        a subset of allocated slots (snd_ac97_pcm_assign) for this pcm
    :type slots: unsigned short

.. _`snd_ac97_pcm_open.description`:

Description
-----------

It locks the specified slots and sets the given rate to AC97 registers.

.. _`snd_ac97_pcm_open.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. _`snd_ac97_pcm_close`:

snd_ac97_pcm_close
==================

.. c:function:: int snd_ac97_pcm_close(struct ac97_pcm *pcm)

    closes the given AC97 pcm

    :param pcm:
        the ac97 pcm instance
    :type pcm: struct ac97_pcm \*

.. _`snd_ac97_pcm_close.description`:

Description
-----------

It frees the locked AC97 slots.

.. _`snd_ac97_pcm_close.return`:

Return
------

Zero.

.. _`snd_ac97_pcm_double_rate_rules`:

snd_ac97_pcm_double_rate_rules
==============================

.. c:function:: int snd_ac97_pcm_double_rate_rules(struct snd_pcm_runtime *runtime)

    set double rate constraints

    :param runtime:
        the runtime of the ac97 front playback pcm
    :type runtime: struct snd_pcm_runtime \*

.. _`snd_ac97_pcm_double_rate_rules.description`:

Description
-----------

Installs the hardware constraint rules to prevent using double rates and
more than two channels at the same time.

.. _`snd_ac97_pcm_double_rate_rules.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. This file was automatic generated / don't edit.

