.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/firewire/amdtp-am824.c

.. _`amdtp_am824_set_parameters`:

amdtp_am824_set_parameters
==========================

.. c:function:: int amdtp_am824_set_parameters(struct amdtp_stream *s, unsigned int rate, unsigned int pcm_channels, unsigned int midi_ports, bool double_pcm_frames)

    set stream parameters

    :param struct amdtp_stream \*s:
        the AMDTP stream to configure

    :param unsigned int rate:
        the sample rate

    :param unsigned int pcm_channels:
        the number of PCM samples in each data block, to be encoded
        as AM824 multi-bit linear audio

    :param unsigned int midi_ports:
        the number of MIDI ports (i.e., MPX-MIDI Data Channels)

    :param bool double_pcm_frames:
        one data block transfers two PCM frames

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

    :param struct amdtp_stream \*s:
        the AMDTP stream

    :param unsigned int index:
        the index of data channel in an data block

    :param unsigned int position:
        the channel of PCM frame

.. _`amdtp_am824_set_midi_position`:

amdtp_am824_set_midi_position
=============================

.. c:function:: void amdtp_am824_set_midi_position(struct amdtp_stream *s, unsigned int position)

    set a index of data channel for MIDI conformant data channel

    :param struct amdtp_stream \*s:
        the AMDTP stream

    :param unsigned int position:
        the index of data channel in an data block

.. _`amdtp_am824_set_pcm_format`:

amdtp_am824_set_pcm_format
==========================

.. c:function:: void amdtp_am824_set_pcm_format(struct amdtp_stream *s, snd_pcm_format_t format)

    set the PCM format

    :param struct amdtp_stream \*s:
        the AMDTP stream to configure

    :param snd_pcm_format_t format:
        the format of the ALSA PCM device

.. _`amdtp_am824_set_pcm_format.description`:

Description
-----------

The sample format must be set after the other parameters (rate/PCM channels/
MIDI) and before the stream is started, and must not be changed while the
stream is running.

.. _`amdtp_am824_add_pcm_hw_constraints`:

amdtp_am824_add_pcm_hw_constraints
==================================

.. c:function:: int amdtp_am824_add_pcm_hw_constraints(struct amdtp_stream *s, struct snd_pcm_runtime *runtime)

    add hw constraints for PCM substream

    :param struct amdtp_stream \*s:
        the AMDTP stream for AM824 data block, must be initialized.

    :param struct snd_pcm_runtime \*runtime:
        the PCM substream runtime

.. _`amdtp_am824_midi_trigger`:

amdtp_am824_midi_trigger
========================

.. c:function:: void amdtp_am824_midi_trigger(struct amdtp_stream *s, unsigned int port, struct snd_rawmidi_substream *midi)

    start/stop playback/capture with a MIDI device

    :param struct amdtp_stream \*s:
        the AMDTP stream

    :param unsigned int port:
        index of MIDI port

    :param struct snd_rawmidi_substream \*midi:
        the MIDI device to be started, or \ ``NULL``\  to stop the current device

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

    :param struct amdtp_stream \*s:
        the AMDTP stream to initialize

    :param struct fw_unit \*unit:
        the target of the stream

    :param enum amdtp_stream_direction dir:
        the direction of stream

    :param enum cip_flags flags:
        the packet transmission method to use

.. This file was automatic generated / don't edit.

