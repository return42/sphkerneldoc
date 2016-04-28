.. -*- coding: utf-8; mode: rst -*-

.. _API-enum-demod-pad-index:

====================
enum demod_pad_index
====================

*man enum demod_pad_index(9)*

*4.6.0-rc5*

analog TV pad index for MEDIA_ENT_F_ATV_DECODER


Synopsis
========

.. code-block:: c

    enum demod_pad_index {
      DEMOD_PAD_IF_INPUT,
      DEMOD_PAD_VID_OUT,
      DEMOD_PAD_VBI_OUT,
      DEMOD_PAD_AUDIO_OUT,
      DEMOD_NUM_PADS
    };


Constants
=========

DEMOD_PAD_IF_INPUT
    IF input sink pad.

DEMOD_PAD_VID_OUT
    Video output source pad.

DEMOD_PAD_VBI_OUT
    Vertical Blank Interface (VBI) output source pad.

DEMOD_PAD_AUDIO_OUT
    Audio output source pad.

DEMOD_NUM_PADS
    Maximum number of output pads.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
