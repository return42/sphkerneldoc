.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mailbox/mailbox.c

.. _`mbox_chan_received_data`:

mbox_chan_received_data
=======================

.. c:function:: void mbox_chan_received_data(struct mbox_chan *chan, void *mssg)

    A way for controller driver to push data received from remote to the upper layer.

    :param chan:
        Pointer to the mailbox channel on which RX happened.
    :type chan: struct mbox_chan \*

    :param mssg:
        Client specific message typecasted as void \*
    :type mssg: void \*

.. _`mbox_chan_received_data.description`:

Description
-----------

After startup and before shutdown any data received on the chan
is passed on to the API via atomic \ :c:func:`mbox_chan_received_data`\ .
The controller should ACK the RX only after this call returns.

.. _`mbox_chan_txdone`:

mbox_chan_txdone
================

.. c:function:: void mbox_chan_txdone(struct mbox_chan *chan, int r)

    A way for controller driver to notify the framework that the last TX has completed.

    :param chan:
        Pointer to the mailbox chan on which TX happened.
    :type chan: struct mbox_chan \*

    :param r:
        Status of last TX - OK or ERROR
    :type r: int

.. _`mbox_chan_txdone.description`:

Description
-----------

The controller that has IRQ for TX ACK calls this atomic API
to tick the TX state machine. It works only if txdone_irq
is set by the controller.

.. _`mbox_client_txdone`:

mbox_client_txdone
==================

.. c:function:: void mbox_client_txdone(struct mbox_chan *chan, int r)

    The way for a client to run the TX state machine.

    :param chan:
        Mailbox channel assigned to this client.
    :type chan: struct mbox_chan \*

    :param r:
        Success status of last transmission.
    :type r: int

.. _`mbox_client_txdone.description`:

Description
-----------

The client/protocol had received some 'ACK' packet and it notifies
the API that the last packet was sent successfully. This only works
if the controller can't sense TX-Done.

.. _`mbox_client_peek_data`:

mbox_client_peek_data
=====================

.. c:function:: bool mbox_client_peek_data(struct mbox_chan *chan)

    A way for client driver to pull data received from remote by the controller.

    :param chan:
        Mailbox channel assigned to this client.
    :type chan: struct mbox_chan \*

.. _`mbox_client_peek_data.description`:

Description
-----------

A poke to controller driver for any received data.
The data is actually passed onto client via the
\ :c:func:`mbox_chan_received_data`\ 
The call can be made from atomic context, so the controller's
implementation of \ :c:func:`peek_data`\  must not sleep.

.. _`mbox_client_peek_data.return`:

Return
------

True, if controller has, and is going to push after this,
some data.
False, if controller doesn't have any data to be read.

.. _`mbox_send_message`:

mbox_send_message
=================

.. c:function:: int mbox_send_message(struct mbox_chan *chan, void *mssg)

    For client to submit a message to be sent to the remote.

    :param chan:
        Mailbox channel assigned to this client.
    :type chan: struct mbox_chan \*

    :param mssg:
        Client specific message typecasted.
    :type mssg: void \*

.. _`mbox_send_message.description`:

Description
-----------

For client to submit data to the controller destined for a remote
processor. If the client had set 'tx_block', the call will return
either when the remote receives the data or when 'tx_tout' millisecs
run out.
In non-blocking mode, the requests are buffered by the API and a
non-negative token is returned for each queued request. If the request
is not queued, a negative token is returned. Upon failure or successful
TX, the API calls 'tx_done' from atomic context, from which the client
could submit yet another request.
The pointer to message should be preserved until it is sent
over the chan, i.e, \ :c:func:`tx_done`\  is made.
This function could be called from atomic context as it simply
queues the data and returns a token against the request.

.. _`mbox_send_message.return`:

Return
------

Non-negative integer for successful submission (non-blocking mode)
or transmission over chan (blocking mode).
Negative value denotes failure.

.. _`mbox_request_channel`:

mbox_request_channel
====================

.. c:function:: struct mbox_chan *mbox_request_channel(struct mbox_client *cl, int index)

    Request a mailbox channel.

    :param cl:
        Identity of the client requesting the channel.
    :type cl: struct mbox_client \*

    :param index:
        Index of mailbox specifier in 'mboxes' property.
    :type index: int

.. _`mbox_request_channel.description`:

Description
-----------

The Client specifies its requirements and capabilities while asking for
a mailbox channel. It can't be called from atomic context.
The channel is exclusively allocated and can't be used by another
client before the owner calls mbox_free_channel.
After assignment, any packet received on this channel will be
handed over to the client via the 'rx_callback'.
The framework holds reference to the client, so the mbox_client
structure shouldn't be modified until the mbox_free_channel returns.

.. _`mbox_request_channel.return`:

Return
------

Pointer to the channel assigned to the client if successful.
ERR_PTR for request failure.

.. _`mbox_free_channel`:

mbox_free_channel
=================

.. c:function:: void mbox_free_channel(struct mbox_chan *chan)

    The client relinquishes control of a mailbox channel by this call.

    :param chan:
        The mailbox channel to be freed.
    :type chan: struct mbox_chan \*

.. _`mbox_controller_register`:

mbox_controller_register
========================

.. c:function:: int mbox_controller_register(struct mbox_controller *mbox)

    Register the mailbox controller

    :param mbox:
        Pointer to the mailbox controller.
    :type mbox: struct mbox_controller \*

.. _`mbox_controller_register.description`:

Description
-----------

The controller driver registers its communication channels

.. _`mbox_controller_unregister`:

mbox_controller_unregister
==========================

.. c:function:: void mbox_controller_unregister(struct mbox_controller *mbox)

    Unregister the mailbox controller

    :param mbox:
        Pointer to the mailbox controller.
    :type mbox: struct mbox_controller \*

.. This file was automatic generated / don't edit.

