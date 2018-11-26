.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hv/channel.c

.. _`vmbus_sendpacket`:

vmbus_sendpacket
================

.. c:function:: int vmbus_sendpacket(struct vmbus_channel *channel, void *buffer, u32 bufferlen, u64 requestid, enum vmbus_packet_type type, u32 flags)

    Send the specified buffer on the given channel

    :param channel:
        Pointer to vmbus_channel structure
    :type channel: struct vmbus_channel \*

    :param buffer:
        Pointer to the buffer you want to send the data from.
    :type buffer: void \*

    :param bufferlen:
        Maximum size of what the buffer holds.
    :type bufferlen: u32

    :param requestid:
        Identifier of the request
    :type requestid: u64

    :param type:
        Type of packet that is being sent e.g. negotiate, time
        packet etc.
    :type type: enum vmbus_packet_type

    :param flags:
        0 or VMBUS_DATA_PACKET_FLAG_COMPLETION_REQUESTED
    :type flags: u32

.. _`vmbus_sendpacket.description`:

Description
-----------

Sends data in \ ``buffer``\  directly to Hyper-V via the vmbus.
This will send the data unparsed to Hyper-V.

Mainly used by Hyper-V drivers.

.. _`__vmbus_recvpacket`:

\__vmbus_recvpacket
===================

.. c:function:: int __vmbus_recvpacket(struct vmbus_channel *channel, void *buffer, u32 bufferlen, u32 *buffer_actual_len, u64 *requestid, bool raw)

    Retrieve the user packet on the specified channel

    :param channel:
        Pointer to vmbus_channel structure
    :type channel: struct vmbus_channel \*

    :param buffer:
        Pointer to the buffer you want to receive the data into.
    :type buffer: void \*

    :param bufferlen:
        Maximum size of what the buffer can hold.
    :type bufferlen: u32

    :param buffer_actual_len:
        The actual size of the data after it was received.
    :type buffer_actual_len: u32 \*

    :param requestid:
        Identifier of the request
    :type requestid: u64 \*

    :param raw:
        true means keep the vmpacket_descriptor header in the received data.
    :type raw: bool

.. _`__vmbus_recvpacket.description`:

Description
-----------

Receives directly from the hyper-v vmbus and puts the data it received
into Buffer. This will receive the data unparsed from hyper-v.

Mainly used by Hyper-V drivers.

.. This file was automatic generated / don't edit.

