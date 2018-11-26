.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/hda/hdac_i915.c

.. _`snd_hdac_i915_set_bclk`:

snd_hdac_i915_set_bclk
======================

.. c:function:: void snd_hdac_i915_set_bclk(struct hdac_bus *bus)

    Reprogram BCLK for HSW/BDW

    :param bus:
        HDA core bus
    :type bus: struct hdac_bus \*

.. _`snd_hdac_i915_set_bclk.description`:

Description
-----------

Intel HSW/BDW display HDA controller is in GPU. Both its power and link BCLK
depends on GPU. Two Extended Mode registers EM4 (M value) and EM5 (N Value)
are used to convert CDClk (Core Display Clock) to 24MHz BCLK:
BCLK = CDCLK \* M / N
The values will be lost when the display power well is disabled and need to
be restored to avoid abnormal playback speed.

Call this function at initializing and changing power well, as well as
at ELD notifier for the hotplug.

.. _`snd_hdac_i915_init`:

snd_hdac_i915_init
==================

.. c:function:: int snd_hdac_i915_init(struct hdac_bus *bus)

    Initialize i915 audio component

    :param bus:
        HDA core bus
    :type bus: struct hdac_bus \*

.. _`snd_hdac_i915_init.description`:

Description
-----------

This function is supposed to be used only by a HD-audio controller
driver that needs the interaction with i915 graphics.

This function initializes and sets up the audio component to communicate
with i915 graphics driver.

Returns zero for success or a negative error code.

.. This file was automatic generated / don't edit.

