.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/rpmsg/qcom_glink_rpm.c

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
        u8 data;
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
by \ ``rx_work``\  of \ ``glink_rpm``\ .

.. _`glink_rpm`:

struct glink_rpm
================

.. c:type:: struct glink_rpm

    driver context, relates to one remote subsystem

.. _`glink_rpm.definition`:

Definition
----------

.. code-block:: c

    struct glink_rpm {
        struct device *dev;
        struct mbox_client mbox_client;
        struct mbox_chan *mbox_chan;
        struct glink_rpm_pipe rx_pipe;
        struct glink_rpm_pipe tx_pipe;
        int irq;
        struct work_struct rx_work;
        spinlock_t rx_lock;
        struct list_head rx_queue;
        struct mutex tx_lock;
        struct mutex idr_lock;
        struct idr lcids;
        struct idr rcids;
    }

.. _`glink_rpm.members`:

Members
-------

dev
    reference to the associated struct device

mbox_client
    *undescribed*

mbox_chan
    *undescribed*

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
        struct glink_rpm *glink;
        struct kref refcount;
        spinlock_t recv_lock;
        char *name;
        unsigned int lcid;
        unsigned int rcid;
        void *buf;
        int buf_offset;
        int buf_size;
        struct completion open_ack;
        struct completion open_req;
    }

.. _`glink_channel.members`:

Members
-------

ept
    rpmsg endpoint this channel is associated with

rpdev
    rpdev reference, only used for primary endpoints

glink
    glink_rpm context handle

refcount
    refcount for the channel object

recv_lock
    guard for \ ``ept``\ .cb

name
    unique channel name/identifier

lcid
    channel id, in local space

rcid
    channel id, in remote space

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

.. _`glink_rpm_send_open_req`:

glink_rpm_send_open_req
=======================

.. c:function:: int glink_rpm_send_open_req(struct glink_rpm *glink, struct glink_channel *channel)

    send a RPM_CMD_OPEN request to the remote

    :param struct glink_rpm \*glink:
        *undescribed*

    :param struct glink_channel \*channel:
        *undescribed*

.. _`glink_rpm_send_open_req.description`:

Description
-----------

Allocates a local channel id and sends a RPM_CMD_OPEN message to the remote.
Will return with refcount held, regardless of outcome.

Returns 0 on success, negative errno otherwise.

.. This file was automatic generated / don't edit.

