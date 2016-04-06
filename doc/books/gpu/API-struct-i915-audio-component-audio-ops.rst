
.. _API-struct-i915-audio-component-audio-ops:

=====================================
struct i915_audio_component_audio_ops
=====================================

*man struct i915_audio_component_audio_ops(9)*

*4.6.0-rc1*

Ops implemented by hda driver, called by i915 driver


Synopsis
========

.. code-block:: c

    struct i915_audio_component_audio_ops {
      void * audio_ptr;
      void (* pin_eld_notify) (void *audio_ptr, int port);
    };


Members
=======

audio_ptr
    Pointer to be used in call to pin_eld_notify

pin_eld_notify
    Notify the HDA driver that pin sense and/or ELD information has changed

    Called when the i915 driver has set up audio pipeline or has just begun to tear it down. This allows the HDA driver to update its status accordingly (even when the HDA
    controller is in power save mode).
