.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/i915_component.h

.. _`i915_audio_component_ops`:

struct i915_audio_component_ops
===============================

.. c:type:: struct i915_audio_component_ops

    Ops implemented by i915 driver, called by hda driver

.. _`i915_audio_component_ops.definition`:

Definition
----------

.. code-block:: c

    struct i915_audio_component_ops {
        struct module *owner;
        void (* get_power) (struct device *);
        void (* put_power) (struct device *);
        void (* codec_wake_override) (struct device *, bool enable);
        int (* get_cdclk_freq) (struct device *);
        int (* sync_audio_rate) (struct device *, int port, int rate);
        int (* get_eld) (struct device *, int port, bool *enabled,unsigned char *buf, int max_bytes);
    }

.. _`i915_audio_component_ops.members`:

Members
-------

owner
    i915 module

get_power
    get the POWER_DOMAIN_AUDIO power well
    Request the power well to be turned on.

put_power
    put the POWER_DOMAIN_AUDIO power well
    Allow the power well to be turned off.

codec_wake_override
    Enable/disable codec wake signal

get_cdclk_freq
    Get the Core Display Clock in kHz

sync_audio_rate
    set n/cts based on the sample rate
    Called from audio driver. After audio driver sets the
    sample rate, it will call this function to set n/cts

get_eld
    fill the audio state and ELD bytes for the given port
    Called from audio driver to get the HDMI/DP audio state of the given
    digital port, and also fetch ELD bytes to the given pointer.

    It returns the byte size of the original ELD (not the actually
    copied size), zero for an invalid ELD, or a negative error code.

    Note that the returned size may be over \ ``max_bytes``\ .  Then it
    implies that only a part of ELD has been copied to the buffer.

.. _`i915_audio_component_audio_ops`:

struct i915_audio_component_audio_ops
=====================================

.. c:type:: struct i915_audio_component_audio_ops

    Ops implemented by hda driver, called by i915 driver

.. _`i915_audio_component_audio_ops.definition`:

Definition
----------

.. code-block:: c

    struct i915_audio_component_audio_ops {
        void *audio_ptr;
        void (* pin_eld_notify) (void *audio_ptr, int port);
    }

.. _`i915_audio_component_audio_ops.members`:

Members
-------

audio_ptr
    Pointer to be used in call to pin_eld_notify

pin_eld_notify
    Notify the HDA driver that pin sense and/or ELD information has changed
    Called when the i915 driver has set up audio pipeline or has just
    begun to tear it down. This allows the HDA driver to update its
    status accordingly (even when the HDA controller is in power save
    mode).

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
        struct device *dev;
        int aud_sample_rate[MAX_PORTS];
        const struct i915_audio_component_ops *ops;
        const struct i915_audio_component_audio_ops *audio_ops;
    }

.. _`i915_audio_component.members`:

Members
-------

dev
    i915 device, used as parameter for ops

aud_sample_rate
    the array of audio sample rate per port

ops
    Ops implemented by i915 driver, called by hda driver

audio_ops
    Ops implemented by hda driver, called by i915 driver

.. This file was automatic generated / don't edit.

