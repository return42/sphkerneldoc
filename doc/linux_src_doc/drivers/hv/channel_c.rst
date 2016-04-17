.. -*- coding: utf-8; mode: rst -*-

=========
channel.c
=========


.. _`vmbus_sendpacket`:

vmbus_sendpacket
================

.. c:function:: int vmbus_sendpacket (struct vmbus_channel *channel, void *buffer, u32 bufferlen, u64 requestid, enum vmbus_packet_type type, u32 flags)

    Send the specified buffer on the given channel

    :param struct vmbus_channel \*channel:
        Pointer to vmbus_channel structure.

    :param void \*buffer:
        Pointer to the buffer you want to receive the data into.

    :param u32 bufferlen:
        Maximum size of what the the buffer will hold

    :param u64 requestid:
        Identifier of the request

    :param enum vmbus_packet_type type:
        Type of packet that is being send e.g. negotiate, time
        packet etc.

    :param u32 flags:

        *undescribed*



.. _`vmbus_sendpacket.description`:

Description
-----------

Sends data in ``buffer`` directly to hyper-v via the vmbus
This will send the data unparsed to hyper-v.

Mainly used by Hyper-V drivers.



.. _`__vmbus_recvpacket`:

__vmbus_recvpacket
==================

.. c:function:: int __vmbus_recvpacket (struct vmbus_channel *channel, void *buffer, u32 bufferlen, u32 *buffer_actual_len, u64 *requestid, bool raw)

    Retrieve the user packet on the specified channel

    :param struct vmbus_channel \*channel:
        Pointer to vmbus_channel structure.

    :param void \*buffer:
        Pointer to the buffer you want to receive the data into.

    :param u32 bufferlen:
        Maximum size of what the the buffer will hold

    :param u32 \*buffer_actual_len:
        The actual size of the data after it was received

    :param u64 \*requestid:
        Identifier of the request

    :param bool raw:

        *undescribed*



.. _`__vmbus_recvpacket.description`:

Description
-----------

Receives directly from the hyper-v vmbus and puts the data it received
into Buffer. This will receive the data unparsed from hyper-v.

Mainly used by Hyper-V drivers.

