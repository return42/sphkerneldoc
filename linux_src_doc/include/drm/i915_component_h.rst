.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/i915_component.h

.. _`i915_audio_component`:

struct i915_audio_component
===========================

.. c:type:: struct i915_audio_component

    Used for direct communication between i915 and hda drivers

.. _`i915_audio_component.definition`:

Definition
----------

.. code-block:: c

    struct i915_audio_component {
        struct drm_audio_component base;
        int aud_sample_rate[MAX_PORTS];
    }

.. _`i915_audio_component.members`:

Members
-------

base
    the drm_audio_component base class

aud_sample_rate
    the array of audio sample rate per port

.. This file was automatic generated / don't edit.

