.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/firewire/amdtp-stream.h

.. _`cip_flags`:

enum cip_flags
==============

.. c:type:: enum cip_flags

    describes details of the streaming protocol

.. _`cip_flags.definition`:

Definition
----------

.. code-block:: c

    enum cip_flags {
        CIP_NONBLOCKING,
        CIP_BLOCKING,
        CIP_EMPTY_WITH_TAG0,
        CIP_DBC_IS_END_EVENT,
        CIP_WRONG_DBS,
        CIP_SKIP_DBC_ZERO_CHECK,
        CIP_EMPTY_HAS_WRONG_DBC,
        CIP_JUMBO_PAYLOAD,
        CIP_HEADER_WITHOUT_EOH,
        CIP_NO_HEADER
    };

.. _`cip_flags.constants`:

Constants
---------

CIP_NONBLOCKING
    In non-blocking mode, each packet contains
    sample_rate/8000 samples, with rounding up or down to adjust
    for clock skew and left-over fractional samples.  This should
    be used if supported by the device.

CIP_BLOCKING
    In blocking mode, each packet contains either zero or
    SYT_INTERVAL samples, with these two types alternating so that
    the overall sample rate comes out right.

CIP_EMPTY_WITH_TAG0
    Only for in-stream. Empty in-packets have TAG0.

CIP_DBC_IS_END_EVENT
    The value of dbc in an packet corresponds to the end
    of event in the packet. Out of IEC 61883.

CIP_WRONG_DBS
    Only for in-stream. The value of dbs is wrong in in-packets.
    The value of data_block_quadlets is used instead of reported value.

CIP_SKIP_DBC_ZERO_CHECK
    Only for in-stream.  Packets with zero in dbc is
    skipped for detecting discontinuity.

CIP_EMPTY_HAS_WRONG_DBC
    Only for in-stream. The value of dbc in empty
    packet is wrong but the others are correct.

CIP_JUMBO_PAYLOAD
    Only for in-stream. The number of data blocks in an
    packet is larger than IEC 61883-6 defines. Current implementation
    allows 5 times as large as IEC 61883-6 defines.

CIP_HEADER_WITHOUT_EOH
    Only for in-stream. CIP Header doesn't include
    valid EOH.

CIP_NO_HEADER
    *undescribed*

.. _`cip_sfc`:

enum cip_sfc
============

.. c:type:: enum cip_sfc

    supported Sampling Frequency Codes (SFCs)

.. _`cip_sfc.definition`:

Definition
----------

.. code-block:: c

    enum cip_sfc {
        CIP_SFC_32000,
        CIP_SFC_44100,
        CIP_SFC_48000,
        CIP_SFC_88200,
        CIP_SFC_96000,
        CIP_SFC_176400,
        CIP_SFC_192000,
        CIP_SFC_COUNT
    };

.. _`cip_sfc.constants`:

Constants
---------

CIP_SFC_32000
    32,000 data blocks

CIP_SFC_44100
    44,100 data blocks

CIP_SFC_48000
    48,000 data blocks

CIP_SFC_88200
    88,200 data blocks

CIP_SFC_96000
    96,000 data blocks

CIP_SFC_176400
    176,400 data blocks

CIP_SFC_192000
    192,000 data blocks

CIP_SFC_COUNT
    the number of supported SFCs

.. _`cip_sfc.description`:

Description
-----------

These values are used to show nominal Sampling Frequency Code in
Format Dependent Field (FDF) of AMDTP packet header. In IEC 61883-6:2002,
this code means the number of events per second. Actually the code
represents the number of data blocks transferred per second in an AMDTP
stream.

In IEC 61883-6:2005, some extensions were added to support more types of
data such as 'One Bit LInear Audio', therefore the meaning of SFC became
different depending on the types.

Currently our implementation is compatible with IEC 61883-6:2002.

.. _`amdtp_stream_running`:

amdtp_stream_running
====================

.. c:function:: bool amdtp_stream_running(struct amdtp_stream *s)

    check stream is running or not

    :param s:
        the AMDTP stream
    :type s: struct amdtp_stream \*

.. _`amdtp_stream_running.description`:

Description
-----------

If this function returns true, the stream is running.

.. _`amdtp_streaming_error`:

amdtp_streaming_error
=====================

.. c:function:: bool amdtp_streaming_error(struct amdtp_stream *s)

    check for streaming error

    :param s:
        the AMDTP stream
    :type s: struct amdtp_stream \*

.. _`amdtp_streaming_error.description`:

Description
-----------

If this function returns true, the stream's packet queue has stopped due to
an asynchronous error.

.. _`amdtp_stream_pcm_running`:

amdtp_stream_pcm_running
========================

.. c:function:: bool amdtp_stream_pcm_running(struct amdtp_stream *s)

    check PCM substream is running or not

    :param s:
        the AMDTP stream
    :type s: struct amdtp_stream \*

.. _`amdtp_stream_pcm_running.description`:

Description
-----------

If this function returns true, PCM substream in the AMDTP stream is running.

.. _`amdtp_stream_pcm_trigger`:

amdtp_stream_pcm_trigger
========================

.. c:function:: void amdtp_stream_pcm_trigger(struct amdtp_stream *s, struct snd_pcm_substream *pcm)

    start/stop playback from a PCM device

    :param s:
        the AMDTP stream
    :type s: struct amdtp_stream \*

    :param pcm:
        the PCM device to be started, or \ ``NULL``\  to stop the current device
    :type pcm: struct snd_pcm_substream \*

.. _`amdtp_stream_pcm_trigger.description`:

Description
-----------

Call this function on a running isochronous stream to enable the actual
transmission of PCM data.  This function should be called from the PCM
device's .trigger callback.

.. _`amdtp_stream_wait_callback`:

amdtp_stream_wait_callback
==========================

.. c:function:: bool amdtp_stream_wait_callback(struct amdtp_stream *s, unsigned int timeout)

    sleep till callbacked or timeout

    :param s:
        the AMDTP stream
    :type s: struct amdtp_stream \*

    :param timeout:
        msec till timeout
    :type timeout: unsigned int

.. _`amdtp_stream_wait_callback.description`:

Description
-----------

If this function return false, the AMDTP stream should be stopped.

.. This file was automatic generated / don't edit.

