
.. _API-i915-audio-component-init:

=========================
i915_audio_component_init
=========================

*man i915_audio_component_init(9)*

*4.6.0-rc1*

initialize and register the audio component


Synopsis
========

.. c:function:: void i915_audio_component_init( struct drm_i915_private * dev_priv )

Arguments
=========

``dev_priv``
    i915 device instance


Description
===========

This will register with the component framework a child component which will bind dynamically to the snd_hda_intel driver's corresponding master component when the latter is
registered. During binding the child initializes an instance of struct i915_audio_component which it receives from the master. The master can then start to use the interface
defined by this struct. Each side can break the binding at any point by deregistering its own component after which each side's component unbind callback is called.

We ignore any error during registration and continue with reduced functionality (i.e. without HDMI audio).
