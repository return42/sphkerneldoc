.. -*- coding: utf-8; mode: rst -*-

.. _API-i915-audio-component-cleanup:

============================
i915_audio_component_cleanup
============================

*man i915_audio_component_cleanup(9)*

*4.6.0-rc5*

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

Deregisters the audio component, breaking any existing binding to the
corresponding snd_hda_intel driver's master component.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
