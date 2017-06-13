.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_audio.c

.. _`intel_audio_codec_enable`:

intel_audio_codec_enable
========================

.. c:function:: void intel_audio_codec_enable(struct intel_encoder *intel_encoder, const struct intel_crtc_state *crtc_state, const struct drm_connector_state *conn_state)

    Enable the audio codec for HD audio

    :param struct intel_encoder \*intel_encoder:
        encoder on which to enable audio

    :param const struct intel_crtc_state \*crtc_state:
        pointer to the current crtc state.

    :param const struct drm_connector_state \*conn_state:
        pointer to the current connector state.

.. _`intel_audio_codec_enable.description`:

Description
-----------

The enable sequences may only be performed after enabling the transcoder and
port, and after completed link training.

.. _`intel_audio_codec_disable`:

intel_audio_codec_disable
=========================

.. c:function:: void intel_audio_codec_disable(struct intel_encoder *intel_encoder)

    Disable the audio codec for HD audio

    :param struct intel_encoder \*intel_encoder:
        encoder on which to disable audio

.. _`intel_audio_codec_disable.description`:

Description
-----------

The disable sequences must be performed before disabling the transcoder or
port.

.. _`intel_init_audio_hooks`:

intel_init_audio_hooks
======================

.. c:function:: void intel_init_audio_hooks(struct drm_i915_private *dev_priv)

    Set up chip specific audio hooks

    :param struct drm_i915_private \*dev_priv:
        device private

.. _`i915_audio_component_init`:

i915_audio_component_init
=========================

.. c:function:: void i915_audio_component_init(struct drm_i915_private *dev_priv)

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

.. c:function:: void i915_audio_component_cleanup(struct drm_i915_private *dev_priv)

    deregister the audio component

    :param struct drm_i915_private \*dev_priv:
        i915 device instance

.. _`i915_audio_component_cleanup.description`:

Description
-----------

Deregisters the audio component, breaking any existing binding to the
corresponding snd_hda_intel driver's master component.

.. _`intel_audio_init`:

intel_audio_init
================

.. c:function:: void intel_audio_init(struct drm_i915_private *dev_priv)

    Initialize the audio driver either using component framework or using lpe audio bridge

    :param struct drm_i915_private \*dev_priv:
        the i915 drm device private data

.. _`intel_audio_deinit`:

intel_audio_deinit
==================

.. c:function:: void intel_audio_deinit(struct drm_i915_private *dev_priv)

    deinitialize the audio driver

    :param struct drm_i915_private \*dev_priv:
        the i915 drm device private data

.. This file was automatic generated / don't edit.

