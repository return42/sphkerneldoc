.. -*- coding: utf-8; mode: rst -*-

.. _API-enum-if-vid-dec-pad-index:

=========================
enum if_vid_dec_pad_index
=========================

*man enum if_vid_dec_pad_index(9)*

*4.6.0-rc5*

video IF-PLL pad index for MEDIA_ENT_F_IF_VID_DECODER


Synopsis
========

.. code-block:: c

    enum if_vid_dec_pad_index {
      IF_VID_DEC_PAD_IF_INPUT,
      IF_VID_DEC_PAD_OUT,
      IF_VID_DEC_PAD_NUM_PADS
    };


Constants
=========

IF_VID_DEC_PAD_IF_INPUT
    video Intermediate Frequency (IF) sink pad

IF_VID_DEC_PAD_OUT
    IF-PLL video output source pad. Contains the video chrominance and
    luminance IF signals.

IF_VID_DEC_PAD_NUM_PADS
    Number of pads of the video IF-PLL.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
