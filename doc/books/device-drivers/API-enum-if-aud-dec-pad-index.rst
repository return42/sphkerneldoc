.. -*- coding: utf-8; mode: rst -*-

.. _API-enum-if-aud-dec-pad-index:

=========================
enum if_aud_dec_pad_index
=========================

*man enum if_aud_dec_pad_index(9)*

*4.6.0-rc5*

audio/sound IF-PLL pad index for MEDIA_ENT_F_IF_AUD_DECODER


Synopsis
========

.. code-block:: c

    enum if_aud_dec_pad_index {
      IF_AUD_DEC_PAD_IF_INPUT,
      IF_AUD_DEC_PAD_OUT,
      IF_AUD_DEC_PAD_NUM_PADS
    };


Constants
=========

IF_AUD_DEC_PAD_IF_INPUT
    audio Intermediate Frequency (IF) sink pad

IF_AUD_DEC_PAD_OUT
    IF-PLL audio output source pad. Contains the audio sampled stream
    data, usually connected to the bridge bus via an Inter-IC Sound
    (I2S) bus.

IF_AUD_DEC_PAD_NUM_PADS
    Number of pads of the audio IF-PLL.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
