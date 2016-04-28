.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-i915-audio-component:

===========================
struct i915_audio_component
===========================

*man struct i915_audio_component(9)*

*4.6.0-rc5*

Used for direct communication between i915 and hda drivers


Synopsis
========

.. code-block:: c

    struct i915_audio_component {
      struct device * dev;
      int aud_sample_rate[MAX_PORTS];
      const struct i915_audio_component_ops * ops;
      const struct i915_audio_component_audio_ops * audio_ops;
    };


Members
=======

dev
    i915 device, used as parameter for ops

aud_sample_rate[MAX_PORTS]
    the array of audio sample rate per port

ops
    Ops implemented by i915 driver, called by hda driver

audio_ops
    Ops implemented by hda driver, called by i915 driver


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
