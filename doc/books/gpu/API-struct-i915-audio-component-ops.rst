
.. _API-struct-i915-audio-component-ops:

===============================
struct i915_audio_component_ops
===============================

*man struct i915_audio_component_ops(9)*

*4.6.0-rc1*

Ops implemented by i915 driver, called by hda driver


Synopsis
========

.. code-block:: c

    struct i915_audio_component_ops {
      struct module * owner;
      void (* get_power) (struct device *);
      void (* put_power) (struct device *);
      void (* codec_wake_override) (struct device *, bool enable);
      int (* get_cdclk_freq) (struct device *);
      int (* sync_audio_rate) (struct device *, int port, int rate);
      int (* get_eld) (struct device *, int port, bool *enabled,unsigned char *buf, int max_bytes);
    };


Members
=======

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

    Called from audio driver. After audio driver sets the sample rate, it will call this function to set n/cts

get_eld
    fill the audio state and ELD bytes for the given port

    Called from audio driver to get the HDMI/DP audio state of the given digital port, and also fetch ELD bytes to the given pointer.

    It returns the byte size of the original ELD (not the actually copied size), zero for an invalid ELD, or a negative error code.

    Note that the returned size may be over ``max_bytes``. Then it implies that only a part of ELD has been copied to the buffer.
