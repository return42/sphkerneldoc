.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/qrtr/qrtr.c

.. _`qrtr_hdr`:

struct qrtr_hdr
===============

.. c:type:: struct qrtr_hdr

    (I\|R)PCrouter packet header

.. _`qrtr_hdr.definition`:

Definition
----------

.. code-block:: c

    struct qrtr_hdr {
        __le32 version;
        __le32 type;
        __le32 src_node_id;
        __le32 src_port_id;
        __le32 confirm_rx;
        __le32 size;
        __le32 dst_node_id;
        __le32 dst_port_id;
    }

.. _`qrtr_hdr.members`:

Members
-------

version
    protocol version

type
    packet type; one of QRTR_TYPE\_\*

src_node_id
    source node

src_port_id
    source port

confirm_rx
    boolean; whether a resume-tx packet should be send in reply

size
    length of packet, excluding this header

dst_node_id
    destination node

dst_port_id
    destination port

.. _`qrtr_node`:

struct qrtr_node
================

.. c:type:: struct qrtr_node

    endpoint node

.. _`qrtr_node.definition`:

Definition
----------

.. code-block:: c

    struct qrtr_node {
        struct mutex ep_lock;
        struct qrtr_endpoint *ep;
        struct kref ref;
        unsigned int nid;
        struct sk_buff_head rx_queue;
        struct work_struct work;
        struct list_head item;
    }

.. _`qrtr_node.members`:

Members
-------

ep_lock
    lock for endpoint management and callbacks

ep
    endpoint

ref
    reference count for node

nid
    node id

rx_queue
    receive queue

work
    scheduled work struct for recv work

item
    list item for broadcast list

.. _`qrtr_endpoint_post`:

qrtr_endpoint_post
==================

.. c:function:: int qrtr_endpoint_post(struct qrtr_endpoint *ep, const void *data, size_t len)

    post incoming data

    :param struct qrtr_endpoint \*ep:
        endpoint handle

    :param const void \*data:
        data pointer

    :param size_t len:
        size of data in bytes

.. _`qrtr_endpoint_post.return`:

Return
------

0 on success; negative error code on failure

.. _`qrtr_endpoint_register`:

qrtr_endpoint_register
======================

.. c:function:: int qrtr_endpoint_register(struct qrtr_endpoint *ep, unsigned int nid)

    register a new endpoint

    :param struct qrtr_endpoint \*ep:
        endpoint to register

    :param unsigned int nid:
        desired node id; may be QRTR_EP_NID_AUTO for auto-assignment

.. _`qrtr_endpoint_register.return`:

Return
------

0 on success; negative error code on failure

The specified endpoint must have the xmit function pointer set on call.

.. _`qrtr_endpoint_unregister`:

qrtr_endpoint_unregister
========================

.. c:function:: void qrtr_endpoint_unregister(struct qrtr_endpoint *ep)

    unregister endpoint

    :param struct qrtr_endpoint \*ep:
        endpoint to unregister

.. This file was automatic generated / don't edit.

