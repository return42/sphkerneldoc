.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-audio-codec-enable:

========================
intel_audio_codec_enable
========================

*man intel_audio_codec_enable(9)*

*4.6.0-rc5*

Enable the audio codec for HD audio


Synopsis
========

.. c:function:: void intel_audio_codec_enable( struct intel_encoder * intel_encoder )

Arguments
=========

``intel_encoder``
    encoder on which to enable audio


Description
===========

The enable sequences may only be performed after enabling the transcoder
and port, and after completed link training.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
