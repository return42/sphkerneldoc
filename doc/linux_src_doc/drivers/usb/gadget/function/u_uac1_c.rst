.. -*- coding: utf-8; mode: rst -*-

========
u_uac1.c
========


.. _`snd_interval_refine_set`:

snd_interval_refine_set
=======================

.. c:function:: int snd_interval_refine_set (struct snd_interval *i, unsigned int val)

    :param struct snd_interval \*i:

        *undescribed*

    :param unsigned int val:

        *undescribed*



.. _`playback_default_hw_params`:

playback_default_hw_params
==========================

.. c:function:: int playback_default_hw_params (struct gaudio_snd_dev *snd)

    :param struct gaudio_snd_dev \*snd:

        *undescribed*



.. _`u_audio_playback`:

u_audio_playback
================

.. c:function:: size_t u_audio_playback (struct gaudio *card, void *buf, size_t count)

    :param struct gaudio \*card:

        *undescribed*

    :param void \*buf:

        *undescribed*

    :param size_t count:

        *undescribed*



.. _`gaudio_open_snd_dev`:

gaudio_open_snd_dev
===================

.. c:function:: int gaudio_open_snd_dev (struct gaudio *card)

    :param struct gaudio \*card:

        *undescribed*



.. _`gaudio_open_snd_dev.description`:

Description
-----------

Initial the PCM or control device



.. _`gaudio_close_snd_dev`:

gaudio_close_snd_dev
====================

.. c:function:: int gaudio_close_snd_dev (struct gaudio *gau)

    :param struct gaudio \*gau:

        *undescribed*



.. _`gaudio_setup`:

gaudio_setup
============

.. c:function:: int gaudio_setup (struct gaudio *card)

    setup ALSA interface and preparing for USB transfer

    :param struct gaudio \*card:

        *undescribed*



.. _`gaudio_setup.description`:

Description
-----------


This sets up PCM, mixer or MIDI ALSA devices fore USB gadget using.

Returns negative errno, or zero on success



.. _`gaudio_cleanup`:

gaudio_cleanup
==============

.. c:function:: void gaudio_cleanup (struct gaudio *the_card)

    remove ALSA device interface

    :param struct gaudio \*the_card:

        *undescribed*



.. _`gaudio_cleanup.description`:

Description
-----------


This is called to free all resources allocated by @:c:func:`gaudio_setup`.

