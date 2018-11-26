.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/core/pcm.c

.. _`snd_pcm_format_name`:

snd_pcm_format_name
===================

.. c:function:: const char *snd_pcm_format_name(snd_pcm_format_t format)

    Return a name string for the given PCM format

    :param format:
        PCM format
    :type format: snd_pcm_format_t

.. _`snd_pcm_new_stream`:

snd_pcm_new_stream
==================

.. c:function:: int snd_pcm_new_stream(struct snd_pcm *pcm, int stream, int substream_count)

    create a new PCM stream

    :param pcm:
        the pcm instance
    :type pcm: struct snd_pcm \*

    :param stream:
        the stream direction, SNDRV_PCM_STREAM_XXX
    :type stream: int

    :param substream_count:
        the number of substreams
    :type substream_count: int

.. _`snd_pcm_new_stream.description`:

Description
-----------

Creates a new stream for the pcm.
The corresponding stream on the pcm must have been empty before
calling this, i.e. zero must be given to the argument of
\ :c:func:`snd_pcm_new`\ .

.. _`snd_pcm_new_stream.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. _`snd_pcm_new`:

snd_pcm_new
===========

.. c:function:: int snd_pcm_new(struct snd_card *card, const char *id, int device, int playback_count, int capture_count, struct snd_pcm **rpcm)

    create a new PCM instance

    :param card:
        the card instance
    :type card: struct snd_card \*

    :param id:
        the id string
    :type id: const char \*

    :param device:
        the device index (zero based)
    :type device: int

    :param playback_count:
        the number of substreams for playback
    :type playback_count: int

    :param capture_count:
        the number of substreams for capture
    :type capture_count: int

    :param rpcm:
        the pointer to store the new pcm instance
    :type rpcm: struct snd_pcm \*\*

.. _`snd_pcm_new.description`:

Description
-----------

Creates a new PCM instance.

The pcm operators have to be set afterwards to the new instance
via \ :c:func:`snd_pcm_set_ops`\ .

.. _`snd_pcm_new.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. _`snd_pcm_new_internal`:

snd_pcm_new_internal
====================

.. c:function:: int snd_pcm_new_internal(struct snd_card *card, const char *id, int device, int playback_count, int capture_count, struct snd_pcm **rpcm)

    create a new internal PCM instance

    :param card:
        the card instance
    :type card: struct snd_card \*

    :param id:
        the id string
    :type id: const char \*

    :param device:
        the device index (zero based - shared with normal PCMs)
    :type device: int

    :param playback_count:
        the number of substreams for playback
    :type playback_count: int

    :param capture_count:
        the number of substreams for capture
    :type capture_count: int

    :param rpcm:
        the pointer to store the new pcm instance
    :type rpcm: struct snd_pcm \*\*

.. _`snd_pcm_new_internal.description`:

Description
-----------

Creates a new internal PCM instance with no userspace device or procfs
entries. This is used by ASoC Back End PCMs in order to create a PCM that
will only be used internally by kernel drivers. i.e. it cannot be opened
by userspace. It provides existing ASoC components drivers with a substream
and access to any private data.

The pcm operators have to be set afterwards to the new instance
via \ :c:func:`snd_pcm_set_ops`\ .

.. _`snd_pcm_new_internal.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. _`snd_pcm_notify`:

snd_pcm_notify
==============

.. c:function:: int snd_pcm_notify(struct snd_pcm_notify *notify, int nfree)

    Add/remove the notify list

    :param notify:
        PCM notify list
    :type notify: struct snd_pcm_notify \*

    :param nfree:
        0 = register, 1 = unregister
    :type nfree: int

.. _`snd_pcm_notify.description`:

Description
-----------

This adds the given notifier to the global list so that the callback is
called for each registered PCM devices.  This exists only for PCM OSS
emulation, so far.

.. This file was automatic generated / don't edit.

