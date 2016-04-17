.. -*- coding: utf-8; mode: rst -*-

=================
hdac_ext_stream.c
=================


.. _`snd_hdac_ext_stream_init`:

snd_hdac_ext_stream_init
========================

.. c:function:: void snd_hdac_ext_stream_init (struct hdac_ext_bus *ebus, struct hdac_ext_stream *stream, int idx, int direction, int tag)

    initialize each stream (aka device)

    :param struct hdac_ext_bus \*ebus:
        HD-audio ext core bus

    :param struct hdac_ext_stream \*stream:
        HD-audio ext core stream object to initialize

    :param int idx:
        stream index number

    :param int direction:
        stream direction (SNDRV_PCM_STREAM_PLAYBACK or SNDRV_PCM_STREAM_CAPTURE)

    :param int tag:
        the tag id to assign



.. _`snd_hdac_ext_stream_init.description`:

Description
-----------

initialize the stream, if ppcap is enabled then init those and then
invoke hdac stream initialization routine



.. _`snd_hdac_ext_stream_init_all`:

snd_hdac_ext_stream_init_all
============================

.. c:function:: int snd_hdac_ext_stream_init_all (struct hdac_ext_bus *ebus, int start_idx, int num_stream, int dir)

    create and initialize the stream objects for an extended hda bus

    :param struct hdac_ext_bus \*ebus:
        HD-audio ext core bus

    :param int start_idx:
        start index for streams

    :param int num_stream:
        number of streams to initialize

    :param int dir:
        direction of streams



.. _`snd_hdac_stream_free_all`:

snd_hdac_stream_free_all
========================

.. c:function:: void snd_hdac_stream_free_all (struct hdac_ext_bus *ebus)

    free hdac extended stream objects

    :param struct hdac_ext_bus \*ebus:
        HD-audio ext core bus



.. _`snd_hdac_ext_stream_decouple`:

snd_hdac_ext_stream_decouple
============================

.. c:function:: void snd_hdac_ext_stream_decouple (struct hdac_ext_bus *ebus, struct hdac_ext_stream *stream, bool decouple)

    decouple the hdac stream

    :param struct hdac_ext_bus \*ebus:
        HD-audio ext core bus

    :param struct hdac_ext_stream \*stream:
        HD-audio ext core stream object to initialize

    :param bool decouple:
        flag to decouple



.. _`snd_hdac_ext_link_stream_start`:

snd_hdac_ext_link_stream_start
==============================

.. c:function:: void snd_hdac_ext_link_stream_start (struct hdac_ext_stream *stream)

    start a stream

    :param struct hdac_ext_stream \*stream:
        HD-audio ext core stream to start



.. _`snd_hdac_ext_link_stream_clear`:

snd_hdac_ext_link_stream_clear
==============================

.. c:function:: void snd_hdac_ext_link_stream_clear (struct hdac_ext_stream *stream)

    stop a stream DMA

    :param struct hdac_ext_stream \*stream:
        HD-audio ext core stream to stop



.. _`snd_hdac_ext_link_stream_reset`:

snd_hdac_ext_link_stream_reset
==============================

.. c:function:: void snd_hdac_ext_link_stream_reset (struct hdac_ext_stream *stream)

    reset a stream

    :param struct hdac_ext_stream \*stream:
        HD-audio ext core stream to reset



.. _`snd_hdac_ext_link_stream_setup`:

snd_hdac_ext_link_stream_setup
==============================

.. c:function:: int snd_hdac_ext_link_stream_setup (struct hdac_ext_stream *stream, int fmt)

    set up the SD for streaming

    :param struct hdac_ext_stream \*stream:
        HD-audio ext core stream to set up

    :param int fmt:
        stream format



.. _`snd_hdac_ext_link_set_stream_id`:

snd_hdac_ext_link_set_stream_id
===============================

.. c:function:: void snd_hdac_ext_link_set_stream_id (struct hdac_ext_link *link, int stream)

    maps stream id to link output

    :param struct hdac_ext_link \*link:
        HD-audio ext link to set up

    :param int stream:
        stream id



.. _`snd_hdac_ext_link_clear_stream_id`:

snd_hdac_ext_link_clear_stream_id
=================================

.. c:function:: void snd_hdac_ext_link_clear_stream_id (struct hdac_ext_link *link, int stream)

    maps stream id to link output

    :param struct hdac_ext_link \*link:
        HD-audio ext link to set up

    :param int stream:
        stream id



.. _`snd_hdac_ext_stream_assign`:

snd_hdac_ext_stream_assign
==========================

.. c:function:: struct hdac_ext_stream *snd_hdac_ext_stream_assign (struct hdac_ext_bus *ebus, struct snd_pcm_substream *substream, int type)

    assign a stream for the PCM

    :param struct hdac_ext_bus \*ebus:
        HD-audio ext core bus

    :param struct snd_pcm_substream \*substream:
        PCM substream to assign

    :param int type:
        type of stream (coupled, host or link stream)



.. _`snd_hdac_ext_stream_assign.description`:

Description
-----------

This assigns the stream based on the type (coupled/host/link), for the
given PCM substream, assigns it and returns the stream object



.. _`snd_hdac_ext_stream_assign.coupled`:

coupled
-------

Looks for an unused stream



.. _`snd_hdac_ext_stream_assign.host`:

host
----

Looks for an unused decoupled host stream



.. _`snd_hdac_ext_stream_assign.link`:

link
----

Looks for an unused decoupled link stream

If no stream is free, returns NULL. The function tries to keep using
the same stream object when it's used beforehand.  when a stream is
decoupled, it becomes a host stream and link stream.



.. _`snd_hdac_ext_stream_release`:

snd_hdac_ext_stream_release
===========================

.. c:function:: void snd_hdac_ext_stream_release (struct hdac_ext_stream *stream, int type)

    release the assigned stream

    :param struct hdac_ext_stream \*stream:
        HD-audio ext core stream to release

    :param int type:
        type of stream (coupled, host or link stream)



.. _`snd_hdac_ext_stream_release.description`:

Description
-----------

Release the stream that has been assigned by :c:func:`snd_hdac_ext_stream_assign`.



.. _`snd_hdac_ext_stream_spbcap_enable`:

snd_hdac_ext_stream_spbcap_enable
=================================

.. c:function:: void snd_hdac_ext_stream_spbcap_enable (struct hdac_ext_bus *ebus, bool enable, int index)

    enable SPIB for a stream

    :param struct hdac_ext_bus \*ebus:
        HD-audio ext core bus

    :param bool enable:
        flag to enable/disable SPIB

    :param int index:
        stream index for which SPIB need to be enabled



.. _`snd_hdac_ext_stream_set_spib`:

snd_hdac_ext_stream_set_spib
============================

.. c:function:: int snd_hdac_ext_stream_set_spib (struct hdac_ext_bus *ebus, struct hdac_ext_stream *stream, u32 value)

    sets the spib value of a stream

    :param struct hdac_ext_bus \*ebus:
        HD-audio ext core bus

    :param struct hdac_ext_stream \*stream:
        hdac_ext_stream

    :param u32 value:
        spib value to set



.. _`snd_hdac_ext_stream_get_spbmaxfifo`:

snd_hdac_ext_stream_get_spbmaxfifo
==================================

.. c:function:: int snd_hdac_ext_stream_get_spbmaxfifo (struct hdac_ext_bus *ebus, struct hdac_ext_stream *stream)

    gets the spib value of a stream

    :param struct hdac_ext_bus \*ebus:
        HD-audio ext core bus

    :param struct hdac_ext_stream \*stream:
        hdac_ext_stream



.. _`snd_hdac_ext_stream_get_spbmaxfifo.description`:

Description
-----------

Return maxfifo for the stream



.. _`snd_hdac_ext_stop_streams`:

snd_hdac_ext_stop_streams
=========================

.. c:function:: void snd_hdac_ext_stop_streams (struct hdac_ext_bus *ebus)

    stop all stream if running

    :param struct hdac_ext_bus \*ebus:
        HD-audio ext core bus



.. _`snd_hdac_ext_stream_drsm_enable`:

snd_hdac_ext_stream_drsm_enable
===============================

.. c:function:: void snd_hdac_ext_stream_drsm_enable (struct hdac_ext_bus *ebus, bool enable, int index)

    enable DMA resume for a stream

    :param struct hdac_ext_bus \*ebus:
        HD-audio ext core bus

    :param bool enable:
        flag to enable/disable DRSM

    :param int index:
        stream index for which DRSM need to be enabled



.. _`snd_hdac_ext_stream_set_dpibr`:

snd_hdac_ext_stream_set_dpibr
=============================

.. c:function:: int snd_hdac_ext_stream_set_dpibr (struct hdac_ext_bus *ebus, struct hdac_ext_stream *stream, u32 value)

    sets the dpibr value of a stream

    :param struct hdac_ext_bus \*ebus:
        HD-audio ext core bus

    :param struct hdac_ext_stream \*stream:
        hdac_ext_stream

    :param u32 value:
        dpib value to set



.. _`snd_hdac_ext_stream_set_lpib`:

snd_hdac_ext_stream_set_lpib
============================

.. c:function:: int snd_hdac_ext_stream_set_lpib (struct hdac_ext_stream *stream, u32 value)

    sets the lpib value of a stream

    :param struct hdac_ext_stream \*stream:
        hdac_ext_stream

    :param u32 value:
        lpib value to set

