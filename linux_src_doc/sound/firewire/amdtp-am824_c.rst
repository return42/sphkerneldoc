.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/firewire/amdtp-am824.c

.. _`amdtp_am824_set_parameters`:

amdtp_am824_set_parameters
==========================

.. c:function:: int amdtp_am824_set_parameters(struct amdtp_stream *s, unsigned int rate, unsigned int pcm_channels, unsigned int midi_ports, bool double_pcm_frames)

    set stream parameters

    :param s:
        the AMDTP stream to configure
    :type s: struct amdtp_stream \*

    :param rate:
        the sample rate
    :type rate: unsigned int

    :param pcm_channels:
        the number of PCM samples in each data block, to be encoded
        as AM824 multi-bit linear audio
    :type pcm_channels: unsigned int

    :param midi_ports:
        the number of MIDI ports (i.e., MPX-MIDI Data Channels)
    :type midi_ports: unsigned int

    :param double_pcm_frames:
        one data block transfers two PCM frames
    :type double_pcm_frames: bool

.. _`amdtp_am824_set_parameters.description`:

Description
-----------

The parameters must be set before the stream is started, and must not be
changed while the stream is running.

.. _`amdtp_am824_set_pcm_position`:

amdtp_am824_set_pcm_position
============================

.. c:function:: void amdtp_am824_set_pcm_position(struct amdtp_stream *s, unsigned int index, unsigned int position)

    set an index of data channel for a channel of PCM frame

    :param s:
        the AMDTP stream
    :type s: struct amdtp_stream \*

    :param index:
        the index of data channel in an data block
    :type index: unsigned int

    :param position:
        the channel of PCM frame
    :type position: unsigned int

.. _`amdtp_am824_set_midi_position`:

amdtp_am824_set_midi_position
=============================

.. c:function:: void amdtp_am824_set_midi_position(struct amdtp_stream *s, unsigned int position)

    set a index of data channel for MIDI conformant data channel

    :param s:
        the AMDTP stream
    :type s: struct amdtp_stream \*

    :param position:
        the index of data channel in an data block
    :type position: unsigned int

.. _`amdtp_am824_add_pcm_hw_constraints`:

amdtp_am824_add_pcm_hw_constraints
==================================

.. c:function:: int amdtp_am824_add_pcm_hw_constraints(struct amdtp_stream *s, struct snd_pcm_runtime *runtime)

    add hw constraints for PCM substream

    :param s:
        the AMDTP stream for AM824 data block, must be initialized.
    :type s: struct amdtp_stream \*

    :param runtime:
        the PCM substream runtime
    :type runtime: struct snd_pcm_runtime \*

.. _`amdtp_am824_midi_trigger`:

amdtp_am824_midi_trigger
========================

.. c:function:: void amdtp_am824_midi_trigger(struct amdtp_stream *s, unsigned int port, struct snd_rawmidi_substream *midi)

    start/stop playback/capture with a MIDI device

    :param s:
        the AMDTP stream
    :type s: struct amdtp_stream \*

    :param port:
        index of MIDI port
    :type port: unsigned int

    :param midi:
        the MIDI device to be started, or \ ``NULL``\  to stop the current device
    :type midi: struct snd_rawmidi_substream \*

.. _`amdtp_am824_midi_trigger.description`:

Description
-----------

Call this function on a running isochronous stream to enable the actual
transmission of MIDI data.  This function should be called from the MIDI
device's .trigger callback.

.. _`amdtp_am824_init`:

amdtp_am824_init
================

.. c:function:: int amdtp_am824_init(struct amdtp_stream *s, struct fw_unit *unit, enum amdtp_stream_direction dir, enum cip_flags flags)

    initialize an AMDTP stream structure to handle AM824 data block

    :param s:
        the AMDTP stream to initialize
    :type s: struct amdtp_stream \*

    :param unit:
        the target of the stream
    :type unit: struct fw_unit \*

    :param dir:
        the direction of stream
    :type dir: enum amdtp_stream_direction

    :param flags:
        the packet transmission method to use
    :type flags: enum cip_flags

.. This file was automatic generated / don't edit.

