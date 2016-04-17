.. -*- coding: utf-8; mode: rst -*-

==============
amdtp-stream.c
==============


.. _`amdtp_stream_init`:

amdtp_stream_init
=================

.. c:function:: int amdtp_stream_init (struct amdtp_stream *s, struct fw_unit *unit, enum amdtp_stream_direction dir, enum cip_flags flags, unsigned int fmt, amdtp_stream_process_data_blocks_t process_data_blocks, unsigned int protocol_size)

    initialize an AMDTP stream structure

    :param struct amdtp_stream \*s:
        the AMDTP stream to initialize

    :param struct fw_unit \*unit:
        the target of the stream

    :param enum amdtp_stream_direction dir:
        the direction of stream

    :param enum cip_flags flags:
        the packet transmission method to use

    :param unsigned int fmt:
        the value of fmt field in CIP header

    :param amdtp_stream_process_data_blocks_t process_data_blocks:
        callback handler to process data blocks

    :param unsigned int protocol_size:
        the size to allocate newly for protocol



.. _`amdtp_stream_destroy`:

amdtp_stream_destroy
====================

.. c:function:: void amdtp_stream_destroy (struct amdtp_stream *s)

    free stream resources

    :param struct amdtp_stream \*s:
        the AMDTP stream to destroy



.. _`amdtp_stream_add_pcm_hw_constraints`:

amdtp_stream_add_pcm_hw_constraints
===================================

.. c:function:: int amdtp_stream_add_pcm_hw_constraints (struct amdtp_stream *s, struct snd_pcm_runtime *runtime)

    add hw constraints for PCM substream

    :param struct amdtp_stream \*s:
        the AMDTP stream, which must be initialized.

    :param struct snd_pcm_runtime \*runtime:
        the PCM substream runtime



.. _`amdtp_stream_set_parameters`:

amdtp_stream_set_parameters
===========================

.. c:function:: int amdtp_stream_set_parameters (struct amdtp_stream *s, unsigned int rate, unsigned int data_block_quadlets)

    set stream parameters

    :param struct amdtp_stream \*s:
        the AMDTP stream to configure

    :param unsigned int rate:
        the sample rate

    :param unsigned int data_block_quadlets:
        the size of a data block in quadlet unit



.. _`amdtp_stream_set_parameters.description`:

Description
-----------

The parameters must be set before the stream is started, and must not be
changed while the stream is running.



.. _`amdtp_stream_get_max_payload`:

amdtp_stream_get_max_payload
============================

.. c:function:: unsigned int amdtp_stream_get_max_payload (struct amdtp_stream *s)

    get the stream's packet size

    :param struct amdtp_stream \*s:
        the AMDTP stream



.. _`amdtp_stream_get_max_payload.description`:

Description
-----------

This function must not be called before the stream has been configured
with :c:func:`amdtp_stream_set_parameters`.



.. _`amdtp_stream_pcm_prepare`:

amdtp_stream_pcm_prepare
========================

.. c:function:: void amdtp_stream_pcm_prepare (struct amdtp_stream *s)

    prepare PCM device for running

    :param struct amdtp_stream \*s:
        the AMDTP stream



.. _`amdtp_stream_pcm_prepare.description`:

Description
-----------

This function should be called from the PCM device's .prepare callback.



.. _`amdtp_stream_start`:

amdtp_stream_start
==================

.. c:function:: int amdtp_stream_start (struct amdtp_stream *s, int channel, int speed)

    start transferring packets

    :param struct amdtp_stream \*s:
        the AMDTP stream to start

    :param int channel:
        the isochronous channel on the bus

    :param int speed:
        firewire speed code



.. _`amdtp_stream_start.description`:

Description
-----------

The stream cannot be started until it has been configured with
:c:func:`amdtp_stream_set_parameters` and it must be started before any PCM or MIDI
device can be started.



.. _`amdtp_stream_pcm_pointer`:

amdtp_stream_pcm_pointer
========================

.. c:function:: unsigned long amdtp_stream_pcm_pointer (struct amdtp_stream *s)

    get the PCM buffer position

    :param struct amdtp_stream \*s:
        the AMDTP stream that transports the PCM data



.. _`amdtp_stream_pcm_pointer.description`:

Description
-----------

Returns the current buffer position, in frames.



.. _`amdtp_stream_update`:

amdtp_stream_update
===================

.. c:function:: void amdtp_stream_update (struct amdtp_stream *s)

    update the stream after a bus reset

    :param struct amdtp_stream \*s:
        the AMDTP stream



.. _`amdtp_stream_stop`:

amdtp_stream_stop
=================

.. c:function:: void amdtp_stream_stop (struct amdtp_stream *s)

    stop sending packets

    :param struct amdtp_stream \*s:
        the AMDTP stream to stop



.. _`amdtp_stream_stop.description`:

Description
-----------

All PCM and MIDI devices of the stream must be stopped before the stream
itself can be stopped.



.. _`amdtp_stream_pcm_abort`:

amdtp_stream_pcm_abort
======================

.. c:function:: void amdtp_stream_pcm_abort (struct amdtp_stream *s)

    abort the running PCM device

    :param struct amdtp_stream \*s:
        the AMDTP stream about to be stopped



.. _`amdtp_stream_pcm_abort.description`:

Description
-----------

If the isochronous stream needs to be stopped asynchronously, call this
function first to stop the PCM device.

