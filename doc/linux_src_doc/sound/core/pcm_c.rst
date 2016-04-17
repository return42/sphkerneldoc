.. -*- coding: utf-8; mode: rst -*-

=====
pcm.c
=====


.. _`snd_pcm_format_name`:

snd_pcm_format_name
===================

.. c:function:: const char *snd_pcm_format_name (snd_pcm_format_t format)

    Return a name string for the given PCM format

    :param snd_pcm_format_t format:
        PCM format



.. _`snd_pcm_new_stream`:

snd_pcm_new_stream
==================

.. c:function:: int snd_pcm_new_stream (struct snd_pcm *pcm, int stream, int substream_count)

    create a new PCM stream

    :param struct snd_pcm \*pcm:
        the pcm instance

    :param int stream:
        the stream direction, SNDRV_PCM_STREAM_XXX

    :param int substream_count:
        the number of substreams



.. _`snd_pcm_new_stream.description`:

Description
-----------

Creates a new stream for the pcm.
The corresponding stream on the pcm must have been empty before
calling this, i.e. zero must be given to the argument of
:c:func:`snd_pcm_new`.



.. _`snd_pcm_new_stream.return`:

Return
------

Zero if successful, or a negative error code on failure.



.. _`snd_pcm_new`:

snd_pcm_new
===========

.. c:function:: int snd_pcm_new (struct snd_card *card, const char *id, int device, int playback_count, int capture_count, struct snd_pcm **rpcm)

    create a new PCM instance

    :param struct snd_card \*card:
        the card instance

    :param const char \*id:
        the id string

    :param int device:
        the device index (zero based)

    :param int playback_count:
        the number of substreams for playback

    :param int capture_count:
        the number of substreams for capture

    :param struct snd_pcm \*\*rpcm:
        the pointer to store the new pcm instance



.. _`snd_pcm_new.description`:

Description
-----------

Creates a new PCM instance.

The pcm operators have to be set afterwards to the new instance
via :c:func:`snd_pcm_set_ops`.



.. _`snd_pcm_new.return`:

Return
------

Zero if successful, or a negative error code on failure.



.. _`snd_pcm_new_internal`:

snd_pcm_new_internal
====================

.. c:function:: int snd_pcm_new_internal (struct snd_card *card, const char *id, int device, int playback_count, int capture_count, struct snd_pcm **rpcm)

    create a new internal PCM instance

    :param struct snd_card \*card:
        the card instance

    :param const char \*id:
        the id string

    :param int device:
        the device index (zero based - shared with normal PCMs)

    :param int playback_count:
        the number of substreams for playback

    :param int capture_count:
        the number of substreams for capture

    :param struct snd_pcm \*\*rpcm:
        the pointer to store the new pcm instance



.. _`snd_pcm_new_internal.description`:

Description
-----------

Creates a new internal PCM instance with no userspace device or procfs
entries. This is used by ASoC Back End PCMs in order to create a PCM that
will only be used internally by kernel drivers. i.e. it cannot be opened
by userspace. It provides existing ASoC components drivers with a substream
and access to any private data.

The pcm operators have to be set afterwards to the new instance
via :c:func:`snd_pcm_set_ops`.



.. _`snd_pcm_new_internal.return`:

Return
------

Zero if successful, or a negative error code on failure.



.. _`snd_pcm_notify`:

snd_pcm_notify
==============

.. c:function:: int snd_pcm_notify (struct snd_pcm_notify *notify, int nfree)

    Add/remove the notify list

    :param struct snd_pcm_notify \*notify:
        PCM notify list

    :param int nfree:
        0 = register, 1 = unregister



.. _`snd_pcm_notify.description`:

Description
-----------

This adds the given notifier to the global list so that the callback is
called for each registered PCM devices.  This exists only for PCM OSS
emulation, so far.

