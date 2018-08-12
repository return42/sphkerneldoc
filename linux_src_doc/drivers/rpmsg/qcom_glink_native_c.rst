.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/rpmsg/qcom_glink_native.c

.. _`glink_defer_cmd`:

struct glink_defer_cmd
======================

.. c:type:: struct glink_defer_cmd

    deferred incoming control message

.. _`glink_defer_cmd.definition`:

Definition
----------

.. code-block:: c

    struct glink_defer_cmd {
        struct list_head node;
        struct glink_msg msg;
        u8 data[];
    }

.. _`glink_defer_cmd.members`:

Members
-------

node
    list node

msg
    message header

data
    *undescribed*

.. _`glink_defer_cmd.data`:

data
----

payload of the message

Copy of a received control message, to be added to \ ``rx_queue``\  and processed
by \ ``rx_work``\  of \ ``qcom_glink``\ .

.. _`glink_core_rx_intent`:

struct glink_core_rx_intent
===========================

.. c:type:: struct glink_core_rx_intent

    RX intent RX intent

.. _`glink_core_rx_intent.definition`:

Definition
----------

.. code-block:: c

    struct glink_core_rx_intent {
        void *data;
        u32 id;
        size_t size;
        bool reuse;
        bool in_use;
        u32 offset;
        struct list_head node;
    }

.. _`glink_core_rx_intent.members`:

Members
-------

data
    *undescribed*

id
    *undescribed*

size
    *undescribed*

reuse
    *undescribed*

in_use
    *undescribed*

offset
    *undescribed*

node
    *undescribed*

.. _`glink_core_rx_intent.data`:

data
----

pointer to the data (may be NULL for zero-copy)
id: remote or local intent ID

.. _`glink_core_rx_intent.size`:

size
----

size of the original intent (do not modify)

.. _`glink_core_rx_intent.reuse`:

reuse
-----

To mark if the intent can be reused after first use

.. _`glink_core_rx_intent.in_use`:

in_use
------

To mark if intent is already in use for the channel

.. _`glink_core_rx_intent.offset`:

offset
------

next write offset (initially 0)

.. _`qcom_glink`:

struct qcom_glink
=================

.. c:type:: struct qcom_glink

    driver context, relates to one remote subsystem

.. _`qcom_glink.definition`:

Definition
----------

.. code-block:: c

    struct qcom_glink {
        struct device *dev;
        struct mbox_client mbox_client;
        struct mbox_chan *mbox_chan;
        struct qcom_glink_pipe *rx_pipe;
        struct qcom_glink_pipe *tx_pipe;
        int irq;
        struct work_struct rx_work;
        spinlock_t rx_lock;
        struct list_head rx_queue;
        spinlock_t tx_lock;
        spinlock_t idr_lock;
        struct idr lcids;
        struct idr rcids;
        unsigned long features;
        bool intentless;
    }

.. _`qcom_glink.members`:

Members
-------

dev
    reference to the associated struct device

mbox_client
    mailbox client

mbox_chan
    mailbox channel

rx_pipe
    pipe object for receive FIFO

tx_pipe
    pipe object for transmit FIFO

irq
    IRQ for signaling incoming events

rx_work
    worker for handling received control messages

rx_lock
    protects the \ ``rx_queue``\ 

rx_queue
    queue of received control messages to be processed in \ ``rx_work``\ 

tx_lock
    synchronizes operations on the tx fifo

idr_lock
    synchronizes \ ``lcids``\  and \ ``rcids``\  modifications

lcids
    idr of all channels with a known local channel id

rcids
    idr of all channels with a known remote channel id

features
    *undescribed*

intentless
    *undescribed*

.. _`glink_channel`:

struct glink_channel
====================

.. c:type:: struct glink_channel

    internal representation of a channel

.. _`glink_channel.definition`:

Definition
----------

.. code-block:: c

    struct glink_channel {
        struct rpmsg_endpoint ept;
        struct rpmsg_device *rpdev;
        struct qcom_glink *glink;
        struct kref refcount;
        spinlock_t recv_lock;
        char *name;
        unsigned int lcid;
        unsigned int rcid;
        spinlock_t intent_lock;
        struct idr liids;
        struct idr riids;
        struct work_struct intent_work;
        struct list_head done_intents;
        struct glink_core_rx_intent *buf;
        int buf_offset;
        int buf_size;
        struct completion open_ack;
        struct completion open_req;
        struct mutex intent_req_lock;
        bool intent_req_result;
        struct completion intent_req_comp;
    }

.. _`glink_channel.members`:

Members
-------

ept
    rpmsg endpoint this channel is associated with

rpdev
    rpdev reference, only used for primary endpoints

glink
    qcom_glink context handle

refcount
    refcount for the channel object

recv_lock
    guard for \ ``ept.cb``\ 

name
    unique channel name/identifier

lcid
    channel id, in local space

rcid
    channel id, in remote space

intent_lock
    lock for protection of \ ``liids``\ , \ ``riids``\ 

liids
    idr of all local intents

riids
    idr of all remote intents

intent_work
    worker responsible for transmitting rx_done packets

done_intents
    list of intents that needs to be announced rx_done

buf
    receive buffer, for gathering fragments

buf_offset
    write offset in \ ``buf``\ 

buf_size
    size of current \ ``buf``\ 

open_ack
    completed once remote has acked the open-request

open_req
    completed once open-request has been received

intent_req_lock
    Synchronises multiple intent requests

intent_req_result
    Result of intent request

intent_req_comp
    Completion for intent_req signalling

.. _`qcom_glink_send_open_req`:

qcom_glink_send_open_req
========================

.. c:function:: int qcom_glink_send_open_req(struct qcom_glink *glink, struct glink_channel *channel)

    send a RPM_CMD_OPEN request to the remote

    :param struct qcom_glink \*glink:
        Ptr to the glink edge

    :param struct glink_channel \*channel:
        Ptr to the channel that the open req is sent

.. _`qcom_glink_send_open_req.description`:

Description
-----------

Allocates a local channel id and sends a RPM_CMD_OPEN message to the remote.
Will return with refcount held, regardless of outcome.

Returns 0 on success, negative errno otherwise.

.. _`qcom_glink_receive_version`:

qcom_glink_receive_version
==========================

.. c:function:: void qcom_glink_receive_version(struct qcom_glink *glink, u32 version, u32 features)

    receive version/features from remote system

    :param struct qcom_glink \*glink:
        pointer to transport interface

    :param u32 version:
        *undescribed*

    :param u32 features:
        *undescribed*

.. _`qcom_glink_receive_version.description`:

Description
-----------

This function is called in response to a remote-initiated version/feature
negotiation sequence.

.. _`qcom_glink_receive_version_ack`:

qcom_glink_receive_version_ack
==============================

.. c:function:: void qcom_glink_receive_version_ack(struct qcom_glink *glink, u32 version, u32 features)

    receive negotiation ack from remote system

    :param struct qcom_glink \*glink:
        pointer to transport interface

    :param u32 version:
        *undescribed*

    :param u32 features:
        *undescribed*

.. _`qcom_glink_receive_version_ack.description`:

Description
-----------

This function is called in response to a local-initiated version/feature
negotiation sequence and is the counter-offer from the remote side based
upon the initial version and feature set requested.

.. _`qcom_glink_send_intent_req_ack`:

qcom_glink_send_intent_req_ack
==============================

.. c:function:: int qcom_glink_send_intent_req_ack(struct qcom_glink *glink, struct glink_channel *channel, bool granted)

    convert an rx intent request ack cmd to

    :param struct qcom_glink \*glink:
        The transport to transmit on.

    :param struct glink_channel \*channel:
        The glink channel

    :param bool granted:
        The request response to encode.

.. _`qcom_glink_send_intent_req_ack.return`:

Return
------

0 on success or standard Linux error code.

.. _`qcom_glink_advertise_intent`:

qcom_glink_advertise_intent
===========================

.. c:function:: int qcom_glink_advertise_intent(struct qcom_glink *glink, struct glink_channel *channel, struct glink_core_rx_intent *intent)

    convert an rx intent cmd to wire format and transmit

    :param struct qcom_glink \*glink:
        The transport to transmit on.

    :param struct glink_channel \*channel:
        The local channel

    :param struct glink_core_rx_intent \*intent:
        *undescribed*

.. _`qcom_glink_advertise_intent.return`:

Return
------

0 on success or standard Linux error code.

.. _`qcom_glink_handle_intent_req`:

qcom_glink_handle_intent_req
============================

.. c:function:: void qcom_glink_handle_intent_req(struct qcom_glink *glink, u32 cid, size_t size)

    Receive a request for rx_intent from remote side

    :param struct qcom_glink \*glink:
        *undescribed*

    :param u32 cid:
        *undescribed*

    :param size_t size:
        *undescribed*

.. _`qcom_glink_handle_intent_req.if_ptr`:

if_ptr
------

Pointer to the transport interface

.. _`qcom_glink_handle_intent_req.rcid`:

rcid
----

Remote channel ID

.. _`qcom_glink_handle_intent_req.size`:

size
----

size of the intent

The function searches for the local channel to which the request for
rx_intent has arrived and allocates and notifies the remote back

.. This file was automatic generated / don't edit.

