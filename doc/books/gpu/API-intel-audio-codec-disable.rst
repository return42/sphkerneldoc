.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-audio-codec-disable:

=========================
intel_audio_codec_disable
=========================

*man intel_audio_codec_disable(9)*

*4.6.0-rc5*

Disable the audio codec for HD audio


Synopsis
========

.. c:function:: void intel_audio_codec_disable( struct intel_encoder * intel_encoder )

Arguments
=========

``intel_encoder``
    encoder on which to disable audio


Description
===========

The disable sequences must be performed before disabling the transcoder
or port.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
