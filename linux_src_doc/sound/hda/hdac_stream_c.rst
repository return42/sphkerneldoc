.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/hda/hdac_stream.c

.. _`snd_hdac_stream_init`:

snd_hdac_stream_init
====================

.. c:function:: void snd_hdac_stream_init(struct hdac_bus *bus, struct hdac_stream *azx_dev, int idx, int direction, int tag)

    initialize each stream (aka device)

    :param bus:
        HD-audio core bus
    :type bus: struct hdac_bus \*

    :param azx_dev:
        HD-audio core stream object to initialize
    :type azx_dev: struct hdac_stream \*

    :param idx:
        stream index number
    :type idx: int

    :param direction:
        stream direction (SNDRV_PCM_STREAM_PLAYBACK or SNDRV_PCM_STREAM_CAPTURE)
    :type direction: int

    :param tag:
        the tag id to assign
    :type tag: int

.. _`snd_hdac_stream_init.description`:

Description
-----------

Assign the starting bdl address to each stream (device) and initialize.

.. _`snd_hdac_stream_start`:

snd_hdac_stream_start
=====================

.. c:function:: void snd_hdac_stream_start(struct hdac_stream *azx_dev, bool fresh_start)

    start a stream

    :param azx_dev:
        HD-audio core stream to start
    :type azx_dev: struct hdac_stream \*

    :param fresh_start:
        false = wallclock timestamp relative to period wallclock
    :type fresh_start: bool

.. _`snd_hdac_stream_start.description`:

Description
-----------

Start a stream, set start_wallclk and set the running flag.

.. _`snd_hdac_stream_clear`:

snd_hdac_stream_clear
=====================

.. c:function:: void snd_hdac_stream_clear(struct hdac_stream *azx_dev)

    stop a stream DMA

    :param azx_dev:
        HD-audio core stream to stop
    :type azx_dev: struct hdac_stream \*

.. _`snd_hdac_stream_stop`:

snd_hdac_stream_stop
====================

.. c:function:: void snd_hdac_stream_stop(struct hdac_stream *azx_dev)

    stop a stream

    :param azx_dev:
        HD-audio core stream to stop
    :type azx_dev: struct hdac_stream \*

.. _`snd_hdac_stream_stop.description`:

Description
-----------

Stop a stream DMA and disable stream interrupt

.. _`snd_hdac_stream_reset`:

snd_hdac_stream_reset
=====================

.. c:function:: void snd_hdac_stream_reset(struct hdac_stream *azx_dev)

    reset a stream

    :param azx_dev:
        HD-audio core stream to reset
    :type azx_dev: struct hdac_stream \*

.. _`snd_hdac_stream_setup`:

snd_hdac_stream_setup
=====================

.. c:function:: int snd_hdac_stream_setup(struct hdac_stream *azx_dev)

    set up the SD for streaming

    :param azx_dev:
        HD-audio core stream to set up
    :type azx_dev: struct hdac_stream \*

.. _`snd_hdac_stream_cleanup`:

snd_hdac_stream_cleanup
=======================

.. c:function:: void snd_hdac_stream_cleanup(struct hdac_stream *azx_dev)

    cleanup a stream

    :param azx_dev:
        HD-audio core stream to clean up
    :type azx_dev: struct hdac_stream \*

.. _`snd_hdac_stream_assign`:

snd_hdac_stream_assign
======================

.. c:function:: struct hdac_stream *snd_hdac_stream_assign(struct hdac_bus *bus, struct snd_pcm_substream *substream)

    assign a stream for the PCM

    :param bus:
        HD-audio core bus
    :type bus: struct hdac_bus \*

    :param substream:
        PCM substream to assign
    :type substream: struct snd_pcm_substream \*

.. _`snd_hdac_stream_assign.description`:

Description
-----------

Look for an unused stream for the given PCM substream, assign it
and return the stream object.  If no stream is free, returns NULL.
The function tries to keep using the same stream object when it's used
beforehand.  Also, when bus->reverse_assign flag is set, the last free
or matching entry is returned.  This is needed for some strange codecs.

.. _`snd_hdac_stream_release`:

snd_hdac_stream_release
=======================

.. c:function:: void snd_hdac_stream_release(struct hdac_stream *azx_dev)

    release the assigned stream

    :param azx_dev:
        HD-audio core stream to release
    :type azx_dev: struct hdac_stream \*

.. _`snd_hdac_stream_release.description`:

Description
-----------

Release the stream that has been assigned by \ :c:func:`snd_hdac_stream_assign`\ .

.. _`snd_hdac_get_stream`:

snd_hdac_get_stream
===================

.. c:function:: struct hdac_stream *snd_hdac_get_stream(struct hdac_bus *bus, int dir, int stream_tag)

    return hdac_stream based on stream_tag and direction

    :param bus:
        HD-audio core bus
    :type bus: struct hdac_bus \*

    :param dir:
        direction for the stream to be found
    :type dir: int

    :param stream_tag:
        stream tag for stream to be found
    :type stream_tag: int

.. _`snd_hdac_stream_setup_periods`:

snd_hdac_stream_setup_periods
=============================

.. c:function:: int snd_hdac_stream_setup_periods(struct hdac_stream *azx_dev)

    set up BDL entries

    :param azx_dev:
        HD-audio core stream to set up
    :type azx_dev: struct hdac_stream \*

.. _`snd_hdac_stream_setup_periods.description`:

Description
-----------

Set up the buffer descriptor table of the given stream based on the
period and buffer sizes of the assigned PCM substream.

.. _`snd_hdac_stream_set_params`:

snd_hdac_stream_set_params
==========================

.. c:function:: int snd_hdac_stream_set_params(struct hdac_stream *azx_dev, unsigned int format_val)

    set stream parameters

    :param azx_dev:
        HD-audio core stream for which parameters are to be set
    :type azx_dev: struct hdac_stream \*

    :param format_val:
        format value parameter
    :type format_val: unsigned int

.. _`snd_hdac_stream_set_params.description`:

Description
-----------

Setup the HD-audio core stream parameters from substream of the stream
and passed format value

.. _`snd_hdac_stream_timecounter_init`:

snd_hdac_stream_timecounter_init
================================

.. c:function:: void snd_hdac_stream_timecounter_init(struct hdac_stream *azx_dev, unsigned int streams)

    initialize time counter

    :param azx_dev:
        HD-audio core stream (master stream)
    :type azx_dev: struct hdac_stream \*

    :param streams:
        bit flags of streams to set up
    :type streams: unsigned int

.. _`snd_hdac_stream_timecounter_init.description`:

Description
-----------

Initializes the time counter of streams marked by the bit flags (each
bit corresponds to the stream index).
The trigger timestamp of PCM substream assigned to the given stream is
updated accordingly, too.

.. _`snd_hdac_stream_sync_trigger`:

snd_hdac_stream_sync_trigger
============================

.. c:function:: void snd_hdac_stream_sync_trigger(struct hdac_stream *azx_dev, bool set, unsigned int streams, unsigned int reg)

    turn on/off stream sync register

    :param azx_dev:
        HD-audio core stream (master stream)
    :type azx_dev: struct hdac_stream \*

    :param set:
        *undescribed*
    :type set: bool

    :param streams:
        bit flags of streams to sync
    :type streams: unsigned int

    :param reg:
        *undescribed*
    :type reg: unsigned int

.. _`snd_hdac_stream_sync`:

snd_hdac_stream_sync
====================

.. c:function:: void snd_hdac_stream_sync(struct hdac_stream *azx_dev, bool start, unsigned int streams)

    sync with start/strop trigger operation

    :param azx_dev:
        HD-audio core stream (master stream)
    :type azx_dev: struct hdac_stream \*

    :param start:
        true = start, false = stop
    :type start: bool

    :param streams:
        bit flags of streams to sync
    :type streams: unsigned int

.. _`snd_hdac_stream_sync.description`:

Description
-----------

For \ ``start``\  = true, wait until all FIFOs get ready.
For \ ``start``\  = false, wait until all RUN bits are cleared.

.. _`snd_hdac_dsp_prepare`:

snd_hdac_dsp_prepare
====================

.. c:function:: int snd_hdac_dsp_prepare(struct hdac_stream *azx_dev, unsigned int format, unsigned int byte_size, struct snd_dma_buffer *bufp)

    prepare for DSP loading

    :param azx_dev:
        HD-audio core stream used for DSP loading
    :type azx_dev: struct hdac_stream \*

    :param format:
        HD-audio stream format
    :type format: unsigned int

    :param byte_size:
        data chunk byte size
    :type byte_size: unsigned int

    :param bufp:
        allocated buffer
    :type bufp: struct snd_dma_buffer \*

.. _`snd_hdac_dsp_prepare.description`:

Description
-----------

Allocate the buffer for the given size and set up the given stream for
DSP loading.  Returns the stream tag (>= 0), or a negative error code.

.. _`snd_hdac_dsp_trigger`:

snd_hdac_dsp_trigger
====================

.. c:function:: void snd_hdac_dsp_trigger(struct hdac_stream *azx_dev, bool start)

    start / stop DSP loading

    :param azx_dev:
        HD-audio core stream used for DSP loading
    :type azx_dev: struct hdac_stream \*

    :param start:
        trigger start or stop
    :type start: bool

.. _`snd_hdac_dsp_cleanup`:

snd_hdac_dsp_cleanup
====================

.. c:function:: void snd_hdac_dsp_cleanup(struct hdac_stream *azx_dev, struct snd_dma_buffer *dmab)

    clean up the stream from DSP loading to normal

    :param azx_dev:
        HD-audio core stream used for DSP loading
    :type azx_dev: struct hdac_stream \*

    :param dmab:
        buffer used by DSP loading
    :type dmab: struct snd_dma_buffer \*

.. This file was automatic generated / don't edit.

