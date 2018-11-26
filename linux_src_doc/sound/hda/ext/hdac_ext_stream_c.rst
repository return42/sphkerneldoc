.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/hda/ext/hdac_ext_stream.c

.. _`snd_hdac_ext_stream_init`:

snd_hdac_ext_stream_init
========================

.. c:function:: void snd_hdac_ext_stream_init(struct hdac_bus *bus, struct hdac_ext_stream *stream, int idx, int direction, int tag)

    initialize each stream (aka device)

    :param bus:
        HD-audio core bus
    :type bus: struct hdac_bus \*

    :param stream:
        HD-audio ext core stream object to initialize
    :type stream: struct hdac_ext_stream \*

    :param idx:
        stream index number
    :type idx: int

    :param direction:
        stream direction (SNDRV_PCM_STREAM_PLAYBACK or SNDRV_PCM_STREAM_CAPTURE)
    :type direction: int

    :param tag:
        the tag id to assign
    :type tag: int

.. _`snd_hdac_ext_stream_init.description`:

Description
-----------

initialize the stream, if ppcap is enabled then init those and then
invoke hdac stream initialization routine

.. _`snd_hdac_ext_stream_init_all`:

snd_hdac_ext_stream_init_all
============================

.. c:function:: int snd_hdac_ext_stream_init_all(struct hdac_bus *bus, int start_idx, int num_stream, int dir)

    create and initialize the stream objects for an extended hda bus

    :param bus:
        HD-audio core bus
    :type bus: struct hdac_bus \*

    :param start_idx:
        start index for streams
    :type start_idx: int

    :param num_stream:
        number of streams to initialize
    :type num_stream: int

    :param dir:
        direction of streams
    :type dir: int

.. _`snd_hdac_stream_free_all`:

snd_hdac_stream_free_all
========================

.. c:function:: void snd_hdac_stream_free_all(struct hdac_bus *bus)

    free hdac extended stream objects

    :param bus:
        HD-audio core bus
    :type bus: struct hdac_bus \*

.. _`snd_hdac_ext_stream_decouple`:

snd_hdac_ext_stream_decouple
============================

.. c:function:: void snd_hdac_ext_stream_decouple(struct hdac_bus *bus, struct hdac_ext_stream *stream, bool decouple)

    decouple the hdac stream

    :param bus:
        HD-audio core bus
    :type bus: struct hdac_bus \*

    :param stream:
        HD-audio ext core stream object to initialize
    :type stream: struct hdac_ext_stream \*

    :param decouple:
        flag to decouple
    :type decouple: bool

.. _`snd_hdac_ext_link_stream_start`:

snd_hdac_ext_link_stream_start
==============================

.. c:function:: void snd_hdac_ext_link_stream_start(struct hdac_ext_stream *stream)

    start a stream

    :param stream:
        HD-audio ext core stream to start
    :type stream: struct hdac_ext_stream \*

.. _`snd_hdac_ext_link_stream_clear`:

snd_hdac_ext_link_stream_clear
==============================

.. c:function:: void snd_hdac_ext_link_stream_clear(struct hdac_ext_stream *stream)

    stop a stream DMA

    :param stream:
        HD-audio ext core stream to stop
    :type stream: struct hdac_ext_stream \*

.. _`snd_hdac_ext_link_stream_reset`:

snd_hdac_ext_link_stream_reset
==============================

.. c:function:: void snd_hdac_ext_link_stream_reset(struct hdac_ext_stream *stream)

    reset a stream

    :param stream:
        HD-audio ext core stream to reset
    :type stream: struct hdac_ext_stream \*

.. _`snd_hdac_ext_link_stream_setup`:

snd_hdac_ext_link_stream_setup
==============================

.. c:function:: int snd_hdac_ext_link_stream_setup(struct hdac_ext_stream *stream, int fmt)

    set up the SD for streaming

    :param stream:
        HD-audio ext core stream to set up
    :type stream: struct hdac_ext_stream \*

    :param fmt:
        stream format
    :type fmt: int

.. _`snd_hdac_ext_link_set_stream_id`:

snd_hdac_ext_link_set_stream_id
===============================

.. c:function:: void snd_hdac_ext_link_set_stream_id(struct hdac_ext_link *link, int stream)

    maps stream id to link output

    :param link:
        HD-audio ext link to set up
    :type link: struct hdac_ext_link \*

    :param stream:
        stream id
    :type stream: int

.. _`snd_hdac_ext_link_clear_stream_id`:

snd_hdac_ext_link_clear_stream_id
=================================

.. c:function:: void snd_hdac_ext_link_clear_stream_id(struct hdac_ext_link *link, int stream)

    maps stream id to link output

    :param link:
        HD-audio ext link to set up
    :type link: struct hdac_ext_link \*

    :param stream:
        stream id
    :type stream: int

.. _`snd_hdac_ext_stream_assign`:

snd_hdac_ext_stream_assign
==========================

.. c:function:: struct hdac_ext_stream *snd_hdac_ext_stream_assign(struct hdac_bus *bus, struct snd_pcm_substream *substream, int type)

    assign a stream for the PCM

    :param bus:
        HD-audio core bus
    :type bus: struct hdac_bus \*

    :param substream:
        PCM substream to assign
    :type substream: struct snd_pcm_substream \*

    :param type:
        type of stream (coupled, host or link stream)
    :type type: int

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

.. c:function:: void snd_hdac_ext_stream_release(struct hdac_ext_stream *stream, int type)

    release the assigned stream

    :param stream:
        HD-audio ext core stream to release
    :type stream: struct hdac_ext_stream \*

    :param type:
        type of stream (coupled, host or link stream)
    :type type: int

.. _`snd_hdac_ext_stream_release.description`:

Description
-----------

Release the stream that has been assigned by \ :c:func:`snd_hdac_ext_stream_assign`\ .

.. _`snd_hdac_ext_stream_spbcap_enable`:

snd_hdac_ext_stream_spbcap_enable
=================================

.. c:function:: void snd_hdac_ext_stream_spbcap_enable(struct hdac_bus *bus, bool enable, int index)

    enable SPIB for a stream

    :param bus:
        HD-audio core bus
    :type bus: struct hdac_bus \*

    :param enable:
        flag to enable/disable SPIB
    :type enable: bool

    :param index:
        stream index for which SPIB need to be enabled
    :type index: int

.. _`snd_hdac_ext_stream_set_spib`:

snd_hdac_ext_stream_set_spib
============================

.. c:function:: int snd_hdac_ext_stream_set_spib(struct hdac_bus *bus, struct hdac_ext_stream *stream, u32 value)

    sets the spib value of a stream

    :param bus:
        HD-audio core bus
    :type bus: struct hdac_bus \*

    :param stream:
        hdac_ext_stream
    :type stream: struct hdac_ext_stream \*

    :param value:
        spib value to set
    :type value: u32

.. _`snd_hdac_ext_stream_get_spbmaxfifo`:

snd_hdac_ext_stream_get_spbmaxfifo
==================================

.. c:function:: int snd_hdac_ext_stream_get_spbmaxfifo(struct hdac_bus *bus, struct hdac_ext_stream *stream)

    gets the spib value of a stream

    :param bus:
        HD-audio core bus
    :type bus: struct hdac_bus \*

    :param stream:
        hdac_ext_stream
    :type stream: struct hdac_ext_stream \*

.. _`snd_hdac_ext_stream_get_spbmaxfifo.description`:

Description
-----------

Return maxfifo for the stream

.. _`snd_hdac_ext_stop_streams`:

snd_hdac_ext_stop_streams
=========================

.. c:function:: void snd_hdac_ext_stop_streams(struct hdac_bus *bus)

    stop all stream if running

    :param bus:
        HD-audio core bus
    :type bus: struct hdac_bus \*

.. _`snd_hdac_ext_stream_drsm_enable`:

snd_hdac_ext_stream_drsm_enable
===============================

.. c:function:: void snd_hdac_ext_stream_drsm_enable(struct hdac_bus *bus, bool enable, int index)

    enable DMA resume for a stream

    :param bus:
        HD-audio core bus
    :type bus: struct hdac_bus \*

    :param enable:
        flag to enable/disable DRSM
    :type enable: bool

    :param index:
        stream index for which DRSM need to be enabled
    :type index: int

.. _`snd_hdac_ext_stream_set_dpibr`:

snd_hdac_ext_stream_set_dpibr
=============================

.. c:function:: int snd_hdac_ext_stream_set_dpibr(struct hdac_bus *bus, struct hdac_ext_stream *stream, u32 value)

    sets the dpibr value of a stream

    :param bus:
        HD-audio core bus
    :type bus: struct hdac_bus \*

    :param stream:
        hdac_ext_stream
    :type stream: struct hdac_ext_stream \*

    :param value:
        dpib value to set
    :type value: u32

.. _`snd_hdac_ext_stream_set_lpib`:

snd_hdac_ext_stream_set_lpib
============================

.. c:function:: int snd_hdac_ext_stream_set_lpib(struct hdac_ext_stream *stream, u32 value)

    sets the lpib value of a stream

    :param stream:
        hdac_ext_stream
    :type stream: struct hdac_ext_stream \*

    :param value:
        lpib value to set
    :type value: u32

.. This file was automatic generated / don't edit.

