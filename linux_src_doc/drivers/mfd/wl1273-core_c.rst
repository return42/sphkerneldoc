.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mfd/wl1273-core.c

.. _`wl1273_fm_set_audio`:

wl1273_fm_set_audio
===================

.. c:function:: int wl1273_fm_set_audio(struct wl1273_core *core, unsigned int new_mode)

    Set audio mode.

    :param core:
        A pointer to the device struct.
    :type core: struct wl1273_core \*

    :param new_mode:
        The new audio mode.
    :type new_mode: unsigned int

.. _`wl1273_fm_set_audio.description`:

Description
-----------

Audio modes are WL1273_AUDIO_DIGITAL and WL1273_AUDIO_ANALOG.

.. _`wl1273_fm_set_volume`:

wl1273_fm_set_volume
====================

.. c:function:: int wl1273_fm_set_volume(struct wl1273_core *core, unsigned int volume)

    Set volume.

    :param core:
        A pointer to the device struct.
    :type core: struct wl1273_core \*

    :param volume:
        The new volume value.
    :type volume: unsigned int

.. This file was automatic generated / don't edit.

