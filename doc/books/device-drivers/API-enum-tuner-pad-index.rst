.. -*- coding: utf-8; mode: rst -*-

.. _API-enum-tuner-pad-index:

====================
enum tuner_pad_index
====================

*man enum tuner_pad_index(9)*

*4.6.0-rc5*

tuner pad index for MEDIA_ENT_F_TUNER


Synopsis
========

.. code-block:: c

    enum tuner_pad_index {
      TUNER_PAD_RF_INPUT,
      TUNER_PAD_OUTPUT,
      TUNER_PAD_AUD_OUT,
      TUNER_NUM_PADS
    };


Constants
=========

TUNER_PAD_RF_INPUT
    Radiofrequency (RF) sink pad, usually linked to a RF connector
    entity.

TUNER_PAD_OUTPUT
    Tuner video output source pad. Contains the video chrominance and
    luminance or the hole bandwidth of the signal converted to an
    Intermediate Frequency (IF) or to baseband (on zero-IF tuners).

TUNER_PAD_AUD_OUT
    Tuner audio output source pad. Tuners used to decode analog TV
    signals have an extra pad for audio output. Old tuners use an analog
    stage with a saw filter for the audio IF frequency. The output of
    the pad is, in this case, the audio IF, with should be decoded
    either by the bridge chipset (that's the case of cx2388x chipsets)
    or may require an external IF sound processor, like msp34xx. On
    modern silicon tuners, the audio IF decoder is usually incorporated
    at the tuner. On such case, the output of this pad is an audio
    sampled data.

TUNER_NUM_PADS
    Number of pads of the tuner.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
