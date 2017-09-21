.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hid/intel-ish-hid/ishtp/client.c

.. _`ishtp_read_list_flush`:

ishtp_read_list_flush
=====================

.. c:function:: void ishtp_read_list_flush(struct ishtp_cl *cl)

    Flush read queue

    :param struct ishtp_cl \*cl:
        ishtp client instance

.. _`ishtp_read_list_flush.description`:

Description
-----------

Used to remove all entries from read queue for a client

.. _`ishtp_cl_flush_queues`:

ishtp_cl_flush_queues
=====================

.. c:function:: int ishtp_cl_flush_queues(struct ishtp_cl *cl)

    Flush all queues for a client

    :param struct ishtp_cl \*cl:
        ishtp client instance

.. _`ishtp_cl_flush_queues.description`:

Description
-----------

Used to remove all queues for a client. This is called when a client device
needs reset due to error, S3 resume or during module removal

.. _`ishtp_cl_flush_queues.return`:

Return
------

0 on success else -EINVAL if device is NULL

.. _`ishtp_cl_init`:

ishtp_cl_init
=============

.. c:function:: void ishtp_cl_init(struct ishtp_cl *cl, struct ishtp_device *dev)

    Initialize all fields of a client device

    :param struct ishtp_cl \*cl:
        ishtp client instance

    :param struct ishtp_device \*dev:
        ishtp device

.. _`ishtp_cl_init.initializes-a-client-device-fields`:

Initializes a client device fields
----------------------------------

Init spinlocks, init queues etc.
This function is called during new client creation

.. _`ishtp_cl_allocate`:

ishtp_cl_allocate
=================

.. c:function:: struct ishtp_cl *ishtp_cl_allocate(struct ishtp_device *dev)

    allocates client structure and sets it up.

    :param struct ishtp_device \*dev:
        ishtp device

.. _`ishtp_cl_allocate.description`:

Description
-----------

Allocate memory for new client device and call to initialize each field.

.. _`ishtp_cl_allocate.return`:

Return
------

The allocated client instance or NULL on failure

.. _`ishtp_cl_free`:

ishtp_cl_free
=============

.. c:function:: void ishtp_cl_free(struct ishtp_cl *cl)

    Frees a client device

    :param struct ishtp_cl \*cl:
        client device instance

.. _`ishtp_cl_free.description`:

Description
-----------

Frees a client device

.. _`ishtp_cl_link`:

ishtp_cl_link
=============

.. c:function:: int ishtp_cl_link(struct ishtp_cl *cl, int id)

    Reserve a host id and link the client instance

    :param struct ishtp_cl \*cl:
        client device instance

    :param int id:
        host client id to use. It can be ISHTP_HOST_CLIENT_ID_ANY if any
        id from the available can be used

.. _`ishtp_cl_link.description`:

Description
-----------


This allocates a single bit in the hostmap. This function will make sure
that not many client sessions are opened at the same time. Once allocated
the client device instance is added to the ishtp device in the current
client list

.. _`ishtp_cl_link.return`:

Return
------

0 or error code on failure

.. _`ishtp_cl_unlink`:

ishtp_cl_unlink
===============

.. c:function:: void ishtp_cl_unlink(struct ishtp_cl *cl)

    remove fw_cl from the client device list

    :param struct ishtp_cl \*cl:
        client device instance

.. _`ishtp_cl_unlink.description`:

Description
-----------

Remove a previously linked device to a ishtp device

.. _`ishtp_cl_disconnect`:

ishtp_cl_disconnect
===================

.. c:function:: int ishtp_cl_disconnect(struct ishtp_cl *cl)

    Send disconnect request to firmware

    :param struct ishtp_cl \*cl:
        client device instance

.. _`ishtp_cl_disconnect.description`:

Description
-----------

Send a disconnect request for a client to firmware.

.. _`ishtp_cl_disconnect.return`:

Return
------

0 if successful disconnect response from the firmware or error
code on failure

.. _`ishtp_cl_is_other_connecting`:

ishtp_cl_is_other_connecting
============================

.. c:function:: bool ishtp_cl_is_other_connecting(struct ishtp_cl *cl)

    Check other client is connecting

    :param struct ishtp_cl \*cl:
        client device instance

.. _`ishtp_cl_is_other_connecting.description`:

Description
-----------

Checks if other client with the same fw client id is connecting

.. _`ishtp_cl_is_other_connecting.return`:

Return
------

true if other client is connected else false

.. _`ishtp_cl_connect`:

ishtp_cl_connect
================

.. c:function:: int ishtp_cl_connect(struct ishtp_cl *cl)

    Send connect request to firmware

    :param struct ishtp_cl \*cl:
        client device instance

.. _`ishtp_cl_connect.description`:

Description
-----------

Send a connect request for a client to firmware. If successful it will
RX and TX ring buffers

.. _`ishtp_cl_connect.return`:

Return
------

0 if successful connect response from the firmware and able
to bind and allocate ring buffers or error code on failure

.. _`ishtp_cl_read_start`:

ishtp_cl_read_start
===================

.. c:function:: int ishtp_cl_read_start(struct ishtp_cl *cl)

    Prepare to read client message

    :param struct ishtp_cl \*cl:
        client device instance

.. _`ishtp_cl_read_start.description`:

Description
-----------

Get a free buffer from pool of free read buffers and add to read buffer
pool to add contents. Send a flow control request to firmware to be able
send next message.

.. _`ishtp_cl_read_start.return`:

Return
------

0 if successful or error code on failure

.. _`ishtp_cl_send`:

ishtp_cl_send
=============

.. c:function:: int ishtp_cl_send(struct ishtp_cl *cl, uint8_t *buf, size_t length)

    Send a message to firmware

    :param struct ishtp_cl \*cl:
        client device instance

    :param uint8_t \*buf:
        message buffer

    :param size_t length:
        length of message

.. _`ishtp_cl_send.description`:

Description
-----------

If the client is correct state to send message, this function gets a buffer
from tx ring buffers, copy the message data and call to send the message
using \ :c:func:`ishtp_cl_send_msg`\ 

.. _`ishtp_cl_send.return`:

Return
------

0 if successful or error code on failure

.. _`ishtp_cl_read_complete`:

ishtp_cl_read_complete
======================

.. c:function:: void ishtp_cl_read_complete(struct ishtp_cl_rb *rb)

    read complete

    :param struct ishtp_cl_rb \*rb:
        Pointer to client request block

.. _`ishtp_cl_read_complete.description`:

Description
-----------

If the message is completely received call \ :c:func:`ishtp_cl_bus_rx_event`\ 
to process message

.. _`ipc_tx_callback`:

ipc_tx_callback
===============

.. c:function:: void ipc_tx_callback(void *prm)

    IPC tx callback function

    :param void \*prm:
        Pointer to client device instance

.. _`ipc_tx_callback.description`:

Description
-----------

Send message over IPC either first time or on callback on previous message
completion

.. _`ishtp_cl_send_msg_ipc`:

ishtp_cl_send_msg_ipc
=====================

.. c:function:: void ishtp_cl_send_msg_ipc(struct ishtp_device *dev, struct ishtp_cl *cl)

    Send message using IPC

    :param struct ishtp_device \*dev:
        ISHTP device instance

    :param struct ishtp_cl \*cl:
        Pointer to client device instance

.. _`ishtp_cl_send_msg_ipc.description`:

Description
-----------

Send message over IPC not using DMA

.. _`ishtp_cl_send_msg_dma`:

ishtp_cl_send_msg_dma
=====================

.. c:function:: void ishtp_cl_send_msg_dma(struct ishtp_device *dev, struct ishtp_cl *cl)

    Send message using DMA

    :param struct ishtp_device \*dev:
        ISHTP device instance

    :param struct ishtp_cl \*cl:
        Pointer to client device instance

.. _`ishtp_cl_send_msg_dma.description`:

Description
-----------

Send message using DMA

.. _`ishtp_cl_send_msg`:

ishtp_cl_send_msg
=================

.. c:function:: void ishtp_cl_send_msg(struct ishtp_device *dev, struct ishtp_cl *cl)

    Send message using DMA or IPC

    :param struct ishtp_device \*dev:
        ISHTP device instance

    :param struct ishtp_cl \*cl:
        Pointer to client device instance

.. _`ishtp_cl_send_msg.description`:

Description
-----------

Send message using DMA or IPC based on transfer_path

.. _`recv_ishtp_cl_msg`:

recv_ishtp_cl_msg
=================

.. c:function:: void recv_ishtp_cl_msg(struct ishtp_device *dev, struct ishtp_msg_hdr *ishtp_hdr)

    Receive client message

    :param struct ishtp_device \*dev:
        ISHTP device instance

    :param struct ishtp_msg_hdr \*ishtp_hdr:
        Pointer to message header

.. _`recv_ishtp_cl_msg.description`:

Description
-----------

Receive and dispatch ISHTP client messages. This function executes in ISR
or work queue context

.. _`recv_ishtp_cl_msg_dma`:

recv_ishtp_cl_msg_dma
=====================

.. c:function:: void recv_ishtp_cl_msg_dma(struct ishtp_device *dev, void *msg, struct dma_xfer_hbm *hbm)

    Receive client message

    :param struct ishtp_device \*dev:
        ISHTP device instance

    :param void \*msg:
        message pointer

    :param struct dma_xfer_hbm \*hbm:
        hbm buffer

.. _`recv_ishtp_cl_msg_dma.description`:

Description
-----------

Receive and dispatch ISHTP client messages using DMA. This function executes
in ISR or work queue context

.. This file was automatic generated / don't edit.

