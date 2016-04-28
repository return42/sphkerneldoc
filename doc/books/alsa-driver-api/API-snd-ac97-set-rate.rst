.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-ac97-set-rate:

=================
snd_ac97_set_rate
=================

*man snd_ac97_set_rate(9)*

*4.6.0-rc5*

change the rate of the given input/output.


Synopsis
========

.. c:function:: int snd_ac97_set_rate( struct snd_ac97 * ac97, int reg, unsigned int rate )

Arguments
=========

``ac97``
    the ac97 instance

``reg``
    the register to change

``rate``
    the sample rate to set


Description
===========

Changes the rate of the given input/output on the codec. If the codec
doesn't support VAR, the rate must be 48000 (except for SPDIF).

The valid registers are AC97_PMC_MIC_ADC_RATE,
AC97_PCM_FRONT_DAC_RATE, AC97_PCM_LR_ADC_RATE.
AC97_PCM_SURR_DAC_RATE and AC97_PCM_LFE_DAC_RATE are accepted if
the codec supports them. AC97_SPDIF is accepted as a pseudo register to
modify the SPDIF status bits.


Return
======

Zero if successful, or a negative error code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
