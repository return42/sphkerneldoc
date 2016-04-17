.. -*- coding: utf-8; mode: rst -*-

===========
hdac_i915.c
===========


.. _`snd_hdac_set_codec_wakeup`:

snd_hdac_set_codec_wakeup
=========================

.. c:function:: int snd_hdac_set_codec_wakeup (struct hdac_bus *bus, bool enable)

    Enable / disable HDMI/DP codec wakeup

    :param struct hdac_bus \*bus:
        HDA core bus

    :param bool enable:
        enable or disable the wakeup



.. _`snd_hdac_set_codec_wakeup.description`:

Description
-----------

This function is supposed to be used only by a HD-audio controller
driver that needs the interaction with i915 graphics.

This function should be called during the chip reset, also called at
resume for updating STATESTS register read.

Returns zero for success or a negative error code.



.. _`snd_hdac_display_power`:

snd_hdac_display_power
======================

.. c:function:: int snd_hdac_display_power (struct hdac_bus *bus, bool enable)

    Power up / down the power refcount

    :param struct hdac_bus \*bus:
        HDA core bus

    :param bool enable:
        power up or down



.. _`snd_hdac_display_power.description`:

Description
-----------

This function is supposed to be used only by a HD-audio controller
driver that needs the interaction with i915 graphics.

This function manages a refcount and calls the i915 :c:func:`get_power` and
:c:func:`put_power` ops accordingly, toggling the codec wakeup, too.

Returns zero for success or a negative error code.



.. _`snd_hdac_get_display_clk`:

snd_hdac_get_display_clk
========================

.. c:function:: int snd_hdac_get_display_clk (struct hdac_bus *bus)

    Get CDCLK in kHz

    :param struct hdac_bus \*bus:
        HDA core bus



.. _`snd_hdac_get_display_clk.description`:

Description
-----------

This function is supposed to be used only by a HD-audio controller
driver that needs the interaction with i915 graphics.

This function queries CDCLK value in kHz from the graphics driver and
returns the value.  A negative code is returned in error.



.. _`snd_hdac_sync_audio_rate`:

snd_hdac_sync_audio_rate
========================

.. c:function:: int snd_hdac_sync_audio_rate (struct hdac_bus *bus, hda_nid_t nid, int rate)

    Set N/CTS based on the sample rate

    :param struct hdac_bus \*bus:
        HDA core bus

    :param hda_nid_t nid:
        the pin widget NID

    :param int rate:
        the sample rate to set



.. _`snd_hdac_sync_audio_rate.description`:

Description
-----------

This function is supposed to be used only by a HD-audio controller
driver that needs the interaction with i915 graphics.

This function sets N/CTS value based on the given sample rate.
Returns zero for success, or a negative error code.



.. _`snd_hdac_acomp_get_eld`:

snd_hdac_acomp_get_eld
======================

.. c:function:: int snd_hdac_acomp_get_eld (struct hdac_bus *bus, hda_nid_t nid, bool *audio_enabled, char *buffer, int max_bytes)

    Get the audio state and ELD via component

    :param struct hdac_bus \*bus:
        HDA core bus

    :param hda_nid_t nid:
        the pin widget NID

    :param bool \*audio_enabled:
        the pointer to store the current audio state

    :param char \*buffer:
        the buffer pointer to store ELD bytes

    :param int max_bytes:
        the max bytes to be stored on ``buffer``



.. _`snd_hdac_acomp_get_eld.description`:

Description
-----------

This function is supposed to be used only by a HD-audio controller
driver that needs the interaction with i915 graphics.

This function queries the current state of the audio on the given
digital port and fetches the ELD bytes onto the given buffer.
It returns the number of bytes for the total ELD data, zero for
invalid ELD, or a negative error code.

The return size is the total bytes required for the whole ELD bytes,
thus it may be over ``max_bytes``\ .  If it's over ``max_bytes``\ , it implies
that only a part of ELD bytes have been fetched.



.. _`snd_hdac_i915_register_notifier`:

snd_hdac_i915_register_notifier
===============================

.. c:function:: int snd_hdac_i915_register_notifier (const struct i915_audio_component_audio_ops *aops)

    Register i915 audio component ops

    :param const struct i915_audio_component_audio_ops \*aops:
        i915 audio component ops



.. _`snd_hdac_i915_register_notifier.description`:

Description
-----------

This function is supposed to be used only by a HD-audio controller
driver that needs the interaction with i915 graphics.

This function sets the given ops to be called by the i915 graphics driver.

Returns zero for success or a negative error code.



.. _`snd_hdac_i915_init`:

snd_hdac_i915_init
==================

.. c:function:: int snd_hdac_i915_init (struct hdac_bus *bus)

    Initialize i915 audio component

    :param struct hdac_bus \*bus:
        HDA core bus



.. _`snd_hdac_i915_init.description`:

Description
-----------

This function is supposed to be used only by a HD-audio controller
driver that needs the interaction with i915 graphics.

This function initializes and sets up the audio component to communicate
with i915 graphics driver.

Returns zero for success or a negative error code.



.. _`snd_hdac_i915_exit`:

snd_hdac_i915_exit
==================

.. c:function:: int snd_hdac_i915_exit (struct hdac_bus *bus)

    Finalize i915 audio component

    :param struct hdac_bus \*bus:
        HDA core bus



.. _`snd_hdac_i915_exit.description`:

Description
-----------

This function is supposed to be used only by a HD-audio controller
driver that needs the interaction with i915 graphics.

This function releases the i915 audio component that has been used.

Returns zero for success or a negative error code.

