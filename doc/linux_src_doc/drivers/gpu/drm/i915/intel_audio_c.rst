.. -*- coding: utf-8; mode: rst -*-

=============
intel_audio.c
=============


.. _`high-definition-audio-over-hdmi-and-display-port`:

High Definition Audio over HDMI and Display Port
================================================

The graphics and audio drivers together support High Definition Audio over
HDMI and Display Port. The audio programming sequences are divided into audio
codec and controller enable and disable sequences. The graphics driver
handles the audio codec sequences, while the audio driver handles the audio
controller sequences.

The disable sequences must be performed before disabling the transcoder or
port. The enable sequences may only be performed after enabling the
transcoder and port, and after completed link training. Therefore the audio
enable/disable sequences are part of the modeset sequence.

The codec and controller sequences could be done either parallel or serial,
but generally the ELDV/PD change in the codec sequence indicates to the audio
driver that the controller sequence should start. Indeed, most of the
co-operation between the graphics and audio drivers is handled via audio
related registers. (The notable exception is the power management, not
covered here.)

The struct i915_audio_component is used to interact between the graphics
and audio drivers. The struct i915_audio_component_ops \*ops in it is
defined in graphics driver and called in audio driver. The
struct i915_audio_component_audio_ops \*audio_ops is called from i915 driver.



.. _`intel_audio_codec_enable`:

intel_audio_codec_enable
========================

.. c:function:: void intel_audio_codec_enable (struct intel_encoder *intel_encoder)

    Enable the audio codec for HD audio

    :param struct intel_encoder \*intel_encoder:
        encoder on which to enable audio



.. _`intel_audio_codec_enable.description`:

Description
-----------

The enable sequences may only be performed after enabling the transcoder and
port, and after completed link training.



.. _`intel_audio_codec_disable`:

intel_audio_codec_disable
=========================

.. c:function:: void intel_audio_codec_disable (struct intel_encoder *intel_encoder)

    Disable the audio codec for HD audio

    :param struct intel_encoder \*intel_encoder:
        encoder on which to disable audio



.. _`intel_audio_codec_disable.description`:

Description
-----------

The disable sequences must be performed before disabling the transcoder or
port.



.. _`intel_init_audio`:

intel_init_audio
================

.. c:function:: void intel_init_audio (struct drm_device *dev)

    Set up chip specific audio functions

    :param struct drm_device \*dev:
        drm device



.. _`i915_audio_component_init`:

i915_audio_component_init
=========================

.. c:function:: void i915_audio_component_init (struct drm_i915_private *dev_priv)

    initialize and register the audio component

    :param struct drm_i915_private \*dev_priv:
        i915 device instance



.. _`i915_audio_component_init.description`:

Description
-----------

This will register with the component framework a child component which
will bind dynamically to the snd_hda_intel driver's corresponding master
component when the latter is registered. During binding the child
initializes an instance of struct i915_audio_component which it receives
from the master. The master can then start to use the interface defined by
this struct. Each side can break the binding at any point by deregistering
its own component after which each side's component unbind callback is
called.

We ignore any error during registration and continue with reduced
functionality (i.e. without HDMI audio).



.. _`i915_audio_component_cleanup`:

i915_audio_component_cleanup
============================

.. c:function:: void i915_audio_component_cleanup (struct drm_i915_private *dev_priv)

    deregister the audio component

    :param struct drm_i915_private \*dev_priv:
        i915 device instance



.. _`i915_audio_component_cleanup.description`:

Description
-----------

Deregisters the audio component, breaking any existing binding to the
corresponding snd_hda_intel driver's master component.

