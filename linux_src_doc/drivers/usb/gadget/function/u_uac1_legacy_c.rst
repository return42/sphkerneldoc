.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/usb/gadget/function/u_uac1_legacy.c

.. _`snd_interval_refine_set`:

snd_interval_refine_set
=======================

.. c:function:: int snd_interval_refine_set(struct snd_interval *i, unsigned int val)

    :param i:
        *undescribed*
    :type i: struct snd_interval \*

    :param val:
        *undescribed*
    :type val: unsigned int

.. _`playback_default_hw_params`:

playback_default_hw_params
==========================

.. c:function:: int playback_default_hw_params(struct gaudio_snd_dev *snd)

    :param snd:
        *undescribed*
    :type snd: struct gaudio_snd_dev \*

.. _`u_audio_playback`:

u_audio_playback
================

.. c:function:: size_t u_audio_playback(struct gaudio *card, void *buf, size_t count)

    :param card:
        *undescribed*
    :type card: struct gaudio \*

    :param buf:
        *undescribed*
    :type buf: void \*

    :param count:
        *undescribed*
    :type count: size_t

.. _`gaudio_open_snd_dev`:

gaudio_open_snd_dev
===================

.. c:function:: int gaudio_open_snd_dev(struct gaudio *card)

    Initial the PCM or control device

    :param card:
        *undescribed*
    :type card: struct gaudio \*

.. _`gaudio_close_snd_dev`:

gaudio_close_snd_dev
====================

.. c:function:: int gaudio_close_snd_dev(struct gaudio *gau)

    :param gau:
        *undescribed*
    :type gau: struct gaudio \*

.. _`gaudio_setup`:

gaudio_setup
============

.. c:function:: int gaudio_setup(struct gaudio *card)

    setup ALSA interface and preparing for USB transfer

    :param card:
        *undescribed*
    :type card: struct gaudio \*

.. _`gaudio_setup.description`:

Description
-----------

This sets up PCM, mixer or MIDI ALSA devices fore USB gadget using.

Returns negative errno, or zero on success

.. _`gaudio_cleanup`:

gaudio_cleanup
==============

.. c:function:: void gaudio_cleanup(struct gaudio *the_card)

    remove ALSA device interface

    :param the_card:
        *undescribed*
    :type the_card: struct gaudio \*

.. _`gaudio_cleanup.description`:

Description
-----------

This is called to free all resources allocated by \ ``gaudio_setup``\ ().

.. This file was automatic generated / don't edit.

