
.. _API-intel-audio-codec-disable:

=========================
intel_audio_codec_disable
=========================

*man intel_audio_codec_disable(9)*

*4.6.0-rc1*

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

The disable sequences must be performed before disabling the transcoder or port.
