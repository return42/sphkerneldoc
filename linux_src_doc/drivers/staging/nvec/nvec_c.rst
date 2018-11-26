.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/nvec/nvec.c

.. _`nvec_msg_category`:

enum nvec_msg_category
======================

.. c:type:: enum nvec_msg_category

    Message categories for \ :c:func:`nvec_msg_alloc`\ 

.. _`nvec_msg_category.definition`:

Definition
----------

.. code-block:: c

    enum nvec_msg_category {
        NVEC_MSG_RX,
        NVEC_MSG_TX
    };

.. _`nvec_msg_category.constants`:

Constants
---------

NVEC_MSG_RX
    The message is an incoming message (from EC)

NVEC_MSG_TX
    The message is an outgoing message (to EC)

.. _`nvec_register_notifier`:

nvec_register_notifier
======================

.. c:function:: int nvec_register_notifier(struct nvec_chip *nvec, struct notifier_block *nb, unsigned int events)

    Register a notifier with nvec

    :param nvec:
        A \ :c:type:`struct nvec_chip <nvec_chip>`\ 
    :type nvec: struct nvec_chip \*

    :param nb:
        The notifier block to register
    :type nb: struct notifier_block \*

    :param events:
        *undescribed*
    :type events: unsigned int

.. _`nvec_register_notifier.description`:

Description
-----------

Registers a notifier with \ ``nvec``\ . The notifier will be added to an atomic
notifier chain that is called for all received messages except those that
correspond to a request initiated by \ :c:func:`nvec_write_sync`\ .

.. _`nvec_unregister_notifier`:

nvec_unregister_notifier
========================

.. c:function:: int nvec_unregister_notifier(struct nvec_chip *nvec, struct notifier_block *nb)

    Unregister a notifier with nvec

    :param nvec:
        A \ :c:type:`struct nvec_chip <nvec_chip>`\ 
    :type nvec: struct nvec_chip \*

    :param nb:
        The notifier block to unregister
    :type nb: struct notifier_block \*

.. _`nvec_unregister_notifier.description`:

Description
-----------

Unregisters a notifier with \ ``nvec``\ . The notifier will be removed from the
atomic notifier chain.

.. _`nvec_status_notifier`:

nvec_status_notifier
====================

.. c:function:: int nvec_status_notifier(struct notifier_block *nb, unsigned long event_type, void *data)

    The final notifier

    :param nb:
        *undescribed*
    :type nb: struct notifier_block \*

    :param event_type:
        *undescribed*
    :type event_type: unsigned long

    :param data:
        *undescribed*
    :type data: void \*

.. _`nvec_status_notifier.description`:

Description
-----------

Prints a message about control events not handled in the notifier
chain.

.. _`nvec_msg_alloc`:

nvec_msg_alloc
==============

.. c:function:: struct nvec_msg *nvec_msg_alloc(struct nvec_chip *nvec, enum nvec_msg_category category)

    :param nvec:
        A \ :c:type:`struct nvec_chip <nvec_chip>`\ 
    :type nvec: struct nvec_chip \*

    :param category:
        Pool category, see \ :c:type:`enum nvec_msg_category <nvec_msg_category>`\ 
    :type category: enum nvec_msg_category

.. _`nvec_msg_alloc.description`:

Description
-----------

Allocate a single \ :c:type:`struct nvec_msg <nvec_msg>`\  object from the message pool of
\ ``nvec``\ . The result shall be passed to \ :c:func:`nvec_msg_free`\  if no longer
used.

Outgoing messages are placed in the upper 75% of the pool, keeping the
lower 25% available for RX buffers only. The reason is to prevent a
situation where all buffers are full and a message is thus endlessly
retried because the response could never be processed.

.. _`nvec_msg_free`:

nvec_msg_free
=============

.. c:function:: void nvec_msg_free(struct nvec_chip *nvec, struct nvec_msg *msg)

    :param nvec:
        A \ :c:type:`struct nvec_chip <nvec_chip>`\ 
    :type nvec: struct nvec_chip \*

    :param msg:
        A message (must be allocated by \ :c:func:`nvec_msg_alloc`\  and belong to \ ``nvec``\ )
    :type msg: struct nvec_msg \*

.. _`nvec_msg_free.description`:

Description
-----------

Free the given message

.. _`nvec_msg_is_event`:

nvec_msg_is_event
=================

.. c:function:: bool nvec_msg_is_event(struct nvec_msg *msg)

    Return \ ``true``\  if \ ``msg``\  is an event

    :param msg:
        A message
    :type msg: struct nvec_msg \*

.. _`nvec_msg_size`:

nvec_msg_size
=============

.. c:function:: size_t nvec_msg_size(struct nvec_msg *msg)

    Get the size of a message

    :param msg:
        The message to get the size for
    :type msg: struct nvec_msg \*

.. _`nvec_msg_size.description`:

Description
-----------

This only works for received messages, not for outgoing messages.

.. _`nvec_gpio_set_value`:

nvec_gpio_set_value
===================

.. c:function:: void nvec_gpio_set_value(struct nvec_chip *nvec, int value)

    Set the GPIO value

    :param nvec:
        A \ :c:type:`struct nvec_chip <nvec_chip>`\ 
    :type nvec: struct nvec_chip \*

    :param value:
        The value to write (0 or 1)
    :type value: int

.. _`nvec_gpio_set_value.description`:

Description
-----------

Like \ :c:func:`gpio_set_value`\ , but generating debugging information

.. _`nvec_write_async`:

nvec_write_async
================

.. c:function:: int nvec_write_async(struct nvec_chip *nvec, const unsigned char *data, short size)

    Asynchronously write a message to NVEC

    :param nvec:
        An nvec_chip instance
    :type nvec: struct nvec_chip \*

    :param data:
        The message data, starting with the request type
    :type data: const unsigned char \*

    :param size:
        The size of \ ``data``\ 
    :type size: short

.. _`nvec_write_async.description`:

Description
-----------

Queue a single message to be transferred to the embedded controller
and return immediately.

.. _`nvec_write_async.return`:

Return
------

0 on success, a negative error code on failure. If a failure
occurred, the nvec driver may print an error.

.. _`nvec_write_sync`:

nvec_write_sync
===============

.. c:function:: int nvec_write_sync(struct nvec_chip *nvec, const unsigned char *data, short size, struct nvec_msg **msg)

    Write a message to nvec and read the response

    :param nvec:
        An \ :c:type:`struct nvec_chip <nvec_chip>`\ 
    :type nvec: struct nvec_chip \*

    :param data:
        The data to write
    :type data: const unsigned char \*

    :param size:
        The size of \ ``data``\ 
    :type size: short

    :param msg:
        The response message received
    :type msg: struct nvec_msg \*\*

.. _`nvec_write_sync.description`:

Description
-----------

This is similar to \ :c:func:`nvec_write_async`\ , but waits for the
request to be answered before returning. This function
uses a mutex and can thus not be called from e.g.
interrupt handlers.

.. _`nvec_write_sync.return`:

Return
------

0 on success, a negative error code on failure.
The response message is returned in \ ``msg``\ . Shall be freed with
with \ :c:func:`nvec_msg_free`\  once no longer used.

.. _`nvec_toggle_global_events`:

nvec_toggle_global_events
=========================

.. c:function:: void nvec_toggle_global_events(struct nvec_chip *nvec, bool state)

    enables or disables global event reporting

    :param nvec:
        nvec handle
    :type nvec: struct nvec_chip \*

    :param state:
        true for enable, false for disable
    :type state: bool

.. _`nvec_toggle_global_events.description`:

Description
-----------

This switches on/off global event reports by the embedded controller.

.. _`nvec_event_mask`:

nvec_event_mask
===============

.. c:function:: void nvec_event_mask(char *ev, u32 mask)

    fill the command string with event bitfield ev: points to event command string

    :param ev:
        *undescribed*
    :type ev: char \*

    :param mask:
        *undescribed*
    :type mask: u32

.. _`nvec_event_mask.mask`:

mask
----

bit to insert into the event mask

Configure event command expects a 32 bit bitfield which describes
which events to enable. The bitfield has the following structure
(from highest byte to lowest):
system state bits 7-0
system state bits 15-8
oem system state bits 7-0
oem system state bits 15-8

.. _`nvec_request_master`:

nvec_request_master
===================

.. c:function:: void nvec_request_master(struct work_struct *work)

    Process outgoing messages

    :param work:
        A \ :c:type:`struct work_struct <work_struct>`\  (the tx_worker member of \ :c:type:`struct nvec_chip <nvec_chip>`\ )
    :type work: struct work_struct \*

.. _`nvec_request_master.description`:

Description
-----------

Processes all outgoing requests by sending the request and awaiting the
response, then continuing with the next request. Once a request has a
matching response, it will be freed and removed from the list.

.. _`parse_msg`:

parse_msg
=========

.. c:function:: int parse_msg(struct nvec_chip *nvec, struct nvec_msg *msg)

    Print some information and call the notifiers on an RX message

    :param nvec:
        A \ :c:type:`struct nvec_chip <nvec_chip>`\ 
    :type nvec: struct nvec_chip \*

    :param msg:
        A message received by \ ``nvec``\ 
    :type msg: struct nvec_msg \*

.. _`parse_msg.description`:

Description
-----------

Paarse some pieces of the message and then call the chain of notifiers
registered via nvec_register_notifier.

.. _`nvec_dispatch`:

nvec_dispatch
=============

.. c:function:: void nvec_dispatch(struct work_struct *work)

    Process messages received from the EC

    :param work:
        A \ :c:type:`struct work_struct <work_struct>`\  (the tx_worker member of \ :c:type:`struct nvec_chip <nvec_chip>`\ )
    :type work: struct work_struct \*

.. _`nvec_dispatch.description`:

Description
-----------

Process messages previously received from the EC and put into the RX
queue of the \ :c:type:`struct nvec_chip <nvec_chip>`\  instance associated with \ ``work``\ .

.. _`nvec_tx_completed`:

nvec_tx_completed
=================

.. c:function:: void nvec_tx_completed(struct nvec_chip *nvec)

    Complete the current transfer

    :param nvec:
        A \ :c:type:`struct nvec_chip <nvec_chip>`\ 
    :type nvec: struct nvec_chip \*

.. _`nvec_tx_completed.description`:

Description
-----------

This is called when we have received an END_TRANS on a TX transfer.

.. _`nvec_rx_completed`:

nvec_rx_completed
=================

.. c:function:: void nvec_rx_completed(struct nvec_chip *nvec)

    Complete the current transfer

    :param nvec:
        A \ :c:type:`struct nvec_chip <nvec_chip>`\ 
    :type nvec: struct nvec_chip \*

.. _`nvec_rx_completed.description`:

Description
-----------

This is called when we have received an END_TRANS on a RX transfer.

.. _`nvec_invalid_flags`:

nvec_invalid_flags
==================

.. c:function:: void nvec_invalid_flags(struct nvec_chip *nvec, unsigned int status, bool reset)

    Send an error message about invalid flags and jump

    :param nvec:
        The nvec device
    :type nvec: struct nvec_chip \*

    :param status:
        The status flags
    :type status: unsigned int

    :param reset:
        Whether we shall jump to state 0.
    :type reset: bool

.. _`nvec_tx_set`:

nvec_tx_set
===========

.. c:function:: void nvec_tx_set(struct nvec_chip *nvec)

    Set the message to transfer (nvec->tx)

    :param nvec:
        A \ :c:type:`struct nvec_chip <nvec_chip>`\ 
    :type nvec: struct nvec_chip \*

.. _`nvec_tx_set.description`:

Description
-----------

Gets the first entry from the tx_data list of \ ``nvec``\  and sets the
tx member to it. If the tx_data list is empty, this uses the
tx_scratch message to send a no operation message.

.. _`nvec_interrupt`:

nvec_interrupt
==============

.. c:function:: irqreturn_t nvec_interrupt(int irq, void *dev)

    Interrupt handler

    :param irq:
        The IRQ
    :type irq: int

    :param dev:
        The nvec device
    :type dev: void \*

.. _`nvec_interrupt.description`:

Description
-----------

Interrupt handler that fills our RX buffers and empties our TX
buffers. This uses a finite state machine with ridiculous amounts
of error checking, in order to be fairly reliable.

.. This file was automatic generated / don't edit.

