
.. _API-i915-audio-component-cleanup:

============================
i915_audio_component_cleanup
============================

*man i915_audio_component_cleanup(9)*

*4.6.0-rc1*

deregister the audio component


Synopsis
========

.. c:function:: void i915_audio_component_cleanup( struct drm_i915_private * dev_priv )

Arguments
=========

``dev_priv``
    i915 device instance


Description
===========

Deregisters the audio component, breaking any existing binding to the corresponding snd_hda_intel driver's master component.
