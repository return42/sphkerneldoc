.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/hda/hdac_component.c

.. _`snd_hdac_set_codec_wakeup`:

snd_hdac_set_codec_wakeup
=========================

.. c:function:: int snd_hdac_set_codec_wakeup(struct hdac_bus *bus, bool enable)

    Enable / disable HDMI/DP codec wakeup

    :param bus:
        HDA core bus
    :type bus: struct hdac_bus \*

    :param enable:
        enable or disable the wakeup
    :type enable: bool

.. _`snd_hdac_set_codec_wakeup.description`:

Description
-----------

This function is supposed to be used only by a HD-audio controller
driver that needs the interaction with graphics driver.

This function should be called during the chip reset, also called at
resume for updating STATESTS register read.

Returns zero for success or a negative error code.

.. _`snd_hdac_display_power`:

snd_hdac_display_power
======================

.. c:function:: int snd_hdac_display_power(struct hdac_bus *bus, bool enable)

    Power up / down the power refcount

    :param bus:
        HDA core bus
    :type bus: struct hdac_bus \*

    :param enable:
        power up or down
    :type enable: bool

.. _`snd_hdac_display_power.description`:

Description
-----------

This function is supposed to be used only by a HD-audio controller
driver that needs the interaction with graphics driver.

This function manages a refcount and calls the \ :c:func:`get_power`\  and
\ :c:func:`put_power`\  ops accordingly, toggling the codec wakeup, too.

Returns zero for success or a negative error code.

.. _`snd_hdac_sync_audio_rate`:

snd_hdac_sync_audio_rate
========================

.. c:function:: int snd_hdac_sync_audio_rate(struct hdac_device *codec, hda_nid_t nid, int dev_id, int rate)

    Set N/CTS based on the sample rate

    :param codec:
        HDA codec
    :type codec: struct hdac_device \*

    :param nid:
        the pin widget NID
    :type nid: hda_nid_t

    :param dev_id:
        device identifier
    :type dev_id: int

    :param rate:
        the sample rate to set
    :type rate: int

.. _`snd_hdac_sync_audio_rate.description`:

Description
-----------

This function is supposed to be used only by a HD-audio controller
driver that needs the interaction with graphics driver.

This function sets N/CTS value based on the given sample rate.
Returns zero for success, or a negative error code.

.. _`snd_hdac_acomp_get_eld`:

snd_hdac_acomp_get_eld
======================

.. c:function:: int snd_hdac_acomp_get_eld(struct hdac_device *codec, hda_nid_t nid, int dev_id, bool *audio_enabled, char *buffer, int max_bytes)

    Get the audio state and ELD via component

    :param codec:
        HDA codec
    :type codec: struct hdac_device \*

    :param nid:
        the pin widget NID
    :type nid: hda_nid_t

    :param dev_id:
        device identifier
    :type dev_id: int

    :param audio_enabled:
        the pointer to store the current audio state
    :type audio_enabled: bool \*

    :param buffer:
        the buffer pointer to store ELD bytes
    :type buffer: char \*

    :param max_bytes:
        the max bytes to be stored on \ ``buffer``\ 
    :type max_bytes: int

.. _`snd_hdac_acomp_get_eld.description`:

Description
-----------

This function is supposed to be used only by a HD-audio controller
driver that needs the interaction with graphics driver.

This function queries the current state of the audio on the given
digital port and fetches the ELD bytes onto the given buffer.
It returns the number of bytes for the total ELD data, zero for
invalid ELD, or a negative error code.

The return size is the total bytes required for the whole ELD bytes,
thus it may be over \ ``max_bytes``\ .  If it's over \ ``max_bytes``\ , it implies
that only a part of ELD bytes have been fetched.

.. _`snd_hdac_acomp_register_notifier`:

snd_hdac_acomp_register_notifier
================================

.. c:function:: int snd_hdac_acomp_register_notifier(struct hdac_bus *bus, const struct drm_audio_component_audio_ops *aops)

    Register audio component ops

    :param bus:
        HDA core bus
    :type bus: struct hdac_bus \*

    :param aops:
        audio component ops
    :type aops: const struct drm_audio_component_audio_ops \*

.. _`snd_hdac_acomp_register_notifier.description`:

Description
-----------

This function is supposed to be used only by a HD-audio controller
driver that needs the interaction with graphics driver.

This function sets the given ops to be called by the graphics driver.

Returns zero for success or a negative error code.

.. _`snd_hdac_acomp_init`:

snd_hdac_acomp_init
===================

.. c:function:: int snd_hdac_acomp_init(struct hdac_bus *bus, const struct drm_audio_component_audio_ops *aops, int (*match_master)(struct device *, void *), size_t extra_size)

    Initialize audio component

    :param bus:
        HDA core bus
    :type bus: struct hdac_bus \*

    :param aops:
        *undescribed*
    :type aops: const struct drm_audio_component_audio_ops \*

    :param int (\*match_master)(struct device \*, void \*):
        match function for finding components

    :param extra_size:
        Extra bytes to allocate
    :type extra_size: size_t

.. _`snd_hdac_acomp_init.description`:

Description
-----------

This function is supposed to be used only by a HD-audio controller
driver that needs the interaction with graphics driver.

This function initializes and sets up the audio component to communicate
with graphics driver.

Unlike \ :c:func:`snd_hdac_i915_init`\ , this function doesn't synchronize with the
binding with the DRM component.  Each caller needs to sync via master_bind
audio_ops.

Returns zero for success or a negative error code.

.. _`snd_hdac_acomp_exit`:

snd_hdac_acomp_exit
===================

.. c:function:: int snd_hdac_acomp_exit(struct hdac_bus *bus)

    Finalize audio component

    :param bus:
        HDA core bus
    :type bus: struct hdac_bus \*

.. _`snd_hdac_acomp_exit.description`:

Description
-----------

This function is supposed to be used only by a HD-audio controller
driver that needs the interaction with graphics driver.

This function releases the audio component that has been used.

Returns zero for success or a negative error code.

.. This file was automatic generated / don't edit.

