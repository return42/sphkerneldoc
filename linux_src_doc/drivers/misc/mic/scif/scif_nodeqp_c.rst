.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mic/scif/scif_nodeqp.c

.. _`scif_node_connect`:

scif_node_connect
=================

.. c:function:: void scif_node_connect(struct scif_dev *scifdev, int dst)

    Respond to SCIF_NODE_CONNECT interrupt message

    :param scifdev:
        *undescribed*
    :type scifdev: struct scif_dev \*

    :param dst:
        Destination node
    :type dst: int

.. _`scif_node_connect.description`:

Description
-----------

Connect the src and dst node by setting up the p2p connection
between them. Management node here acts like a proxy.

.. _`scif_nodeqp_send`:

scif_nodeqp_send
================

.. c:function:: int scif_nodeqp_send(struct scif_dev *scifdev, struct scifmsg *msg)

    Send a message on the node queue pair

    :param scifdev:
        Scif Device.
    :type scifdev: struct scif_dev \*

    :param msg:
        The message to be sent.
    :type msg: struct scifmsg \*

.. _`scif_init`:

scif_init
=========

.. c:function:: void scif_init(struct scif_dev *scifdev, struct scifmsg *msg)

    Respond to SCIF_INIT interrupt message

    :param scifdev:
        Remote SCIF device node
    :type scifdev: struct scif_dev \*

    :param msg:
        Interrupt message
    :type msg: struct scifmsg \*

.. _`scif_exit`:

scif_exit
=========

.. c:function:: void scif_exit(struct scif_dev *scifdev, struct scifmsg *unused)

    Respond to SCIF_EXIT interrupt message

    :param scifdev:
        Remote SCIF device node
    :type scifdev: struct scif_dev \*

    :param unused:
        *undescribed*
    :type unused: struct scifmsg \*

.. _`scif_exit.description`:

Description
-----------

This function stops the SCIF interface for the node which sent
the SCIF_EXIT message and starts waiting for that node to
resetup the queue pair again.

.. _`scif_exit_ack`:

scif_exit_ack
=============

.. c:function:: void scif_exit_ack(struct scif_dev *scifdev, struct scifmsg *unused)

    Respond to SCIF_EXIT_ACK interrupt message

    :param scifdev:
        Remote SCIF device node
    :type scifdev: struct scif_dev \*

    :param unused:
        *undescribed*
    :type unused: struct scifmsg \*

.. _`scif_node_add`:

scif_node_add
=============

.. c:function:: void scif_node_add(struct scif_dev *scifdev, struct scifmsg *msg)

    Respond to SCIF_NODE_ADD interrupt message

    :param scifdev:
        Remote SCIF device node
    :type scifdev: struct scif_dev \*

    :param msg:
        Interrupt message
    :type msg: struct scifmsg \*

.. _`scif_node_add.description`:

Description
-----------

When the mgmt node driver has finished initializing a MIC node queue pair it
marks the node as online. It then looks for all currently online MIC cards
and send a SCIF_NODE_ADD message to identify the ID of the new card for
peer to peer initialization

The local node allocates its incoming queue and sends its address in the
SCIF_NODE_ADD_ACK message back to the mgmt node, the mgmt node "reflects"
this message to the new node

.. _`scif_node_add_ack`:

scif_node_add_ack
=================

.. c:function:: void scif_node_add_ack(struct scif_dev *scifdev, struct scifmsg *msg)

    Respond to SCIF_NODE_ADD_ACK interrupt message

    :param scifdev:
        Remote SCIF device node
    :type scifdev: struct scif_dev \*

    :param msg:
        Interrupt message
    :type msg: struct scifmsg \*

.. _`scif_node_add_ack.description`:

Description
-----------

After a MIC node receives the SCIF_NODE_ADD_ACK message it send this
message to the mgmt node to confirm the sequence is finished.

.. _`scif_node_add_nack`:

scif_node_add_nack
==================

.. c:function:: void scif_node_add_nack(struct scif_dev *scifdev, struct scifmsg *msg)

    Respond to SCIF_NODE_ADD_NACK interrupt message

    :param scifdev:
        *undescribed*
    :type scifdev: struct scif_dev \*

    :param msg:
        Interrupt message
    :type msg: struct scifmsg \*

.. _`scif_node_add_nack.description`:

Description
-----------

SCIF_NODE_ADD failed, so inform the waiting wq.

.. _`scif_get_node_info_resp`:

scif_get_node_info_resp
=======================

.. c:function:: void scif_get_node_info_resp(struct scif_dev *scifdev, struct scifmsg *msg)

    Respond to SCIF_GET_NODE_INFO interrupt message

    :param scifdev:
        *undescribed*
    :type scifdev: struct scif_dev \*

    :param msg:
        Interrupt message
    :type msg: struct scifmsg \*

.. _`scif_get_node_info_resp.description`:

Description
-----------

Retrieve node info i.e maxid and total from the mgmt node.

.. _`scif_nodeqp_intrhandler`:

scif_nodeqp_intrhandler
=======================

.. c:function:: void scif_nodeqp_intrhandler(struct scif_dev *scifdev, struct scif_qp *qp)

    Interrupt handler for node messages

    :param scifdev:
        Remote device to respond to
    :type scifdev: struct scif_dev \*

    :param qp:
        Remote memory pointer
    :type qp: struct scif_qp \*

.. _`scif_nodeqp_intrhandler.description`:

Description
-----------

This routine is triggered by the interrupt mechanism.  It reads
messages from the node queue RB and calls the Node QP Message handling
routine.

.. _`scif_loopb_wq_handler`:

scif_loopb_wq_handler
=====================

.. c:function:: void scif_loopb_wq_handler(struct work_struct *unused)

    Loopback Workqueue Handler.

    :param unused:
        *undescribed*
    :type unused: struct work_struct \*

.. _`scif_loopb_wq_handler.description`:

Description
-----------

This work queue routine is invoked by the loopback work queue handler.
It grabs the recv lock, dequeues any available messages from the head
of the loopback message list, calls the node QP message handler,
waits for it to return, then frees up this message and dequeues more
elements of the list if available.

.. _`scif_loopb_msg_handler`:

scif_loopb_msg_handler
======================

.. c:function:: int scif_loopb_msg_handler(struct scif_dev *scifdev, struct scif_qp *qp)

    Workqueue handler for loopback messages.

    :param scifdev:
        SCIF device
    :type scifdev: struct scif_dev \*

    :param qp:
        Queue pair.
    :type qp: struct scif_qp \*

.. _`scif_loopb_msg_handler.description`:

Description
-----------

This work queue routine is triggered when a loopback message is received.

We need special handling for receiving Node Qp messages on a loopback SCIF
device via two workqueues for receiving messages.

The reason we need the extra workqueue which is not required with \*normal\*
non-loopback SCIF devices is the potential classic deadlock described below:

Thread A tries to send a message on a loopback SCIF device and blocks since
there is no space in the RB while it has the send_lock held or another
lock called lock X for example.

.. _`scif_loopb_msg_handler.thread-b`:

Thread B
--------

The Loopback Node QP message receive workqueue receives the message
and tries to send a message (eg an ACK) to the loopback SCIF device. It tries
to grab the send lock again or lock X and deadlocks with Thread A. The RB
cannot be drained any further due to this classic deadlock.

In order to avoid deadlocks as mentioned above we have an extra level of
indirection achieved by having two workqueues.
1) The first workqueue whose handler is scif_loopb_msg_handler reads
messages from the Node QP RB, adds them to a list and queues work for the
second workqueue.

2) The second workqueue whose handler is scif_loopb_wq_handler dequeues
messages from the list, handles them, frees up the memory and dequeues
more elements from the list if possible.

.. _`scif_setup_loopback_qp`:

scif_setup_loopback_qp
======================

.. c:function:: int scif_setup_loopback_qp(struct scif_dev *scifdev)

    One time setup work for Loopback Node Qp.

    :param scifdev:
        SCIF device
    :type scifdev: struct scif_dev \*

.. _`scif_setup_loopback_qp.description`:

Description
-----------

Sets up the required loopback workqueues, queue pairs and ring buffers

.. _`scif_destroy_loopback_qp`:

scif_destroy_loopback_qp
========================

.. c:function:: int scif_destroy_loopback_qp(struct scif_dev *scifdev)

    One time uninit work for Loopback Node Qp

    :param scifdev:
        SCIF device
    :type scifdev: struct scif_dev \*

.. _`scif_destroy_loopback_qp.description`:

Description
-----------

Destroys the workqueues and frees up the Ring Buffer and Queue Pair memory.

.. This file was automatic generated / don't edit.

