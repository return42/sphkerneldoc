.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/qrtr/qrtr.c

.. _`qrtr_hdr_v1`:

struct qrtr_hdr_v1
==================

.. c:type:: struct qrtr_hdr_v1

    (I\|R)PCrouter packet header version 1

.. _`qrtr_hdr_v1.definition`:

Definition
----------

.. code-block:: c

    struct qrtr_hdr_v1 {
        __le32 version;
        __le32 type;
        __le32 src_node_id;
        __le32 src_port_id;
        __le32 confirm_rx;
        __le32 size;
        __le32 dst_node_id;
        __le32 dst_port_id;
    }

.. _`qrtr_hdr_v1.members`:

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

.. _`qrtr_hdr_v2`:

struct qrtr_hdr_v2
==================

.. c:type:: struct qrtr_hdr_v2

    (I\|R)PCrouter packet header later versions

.. _`qrtr_hdr_v2.definition`:

Definition
----------

.. code-block:: c

    struct qrtr_hdr_v2 {
        u8 version;
        u8 type;
        u8 flags;
        u8 optlen;
        __le32 size;
        __le16 src_node_id;
        __le16 src_port_id;
        __le16 dst_node_id;
        __le16 dst_port_id;
    }

.. _`qrtr_hdr_v2.members`:

Members
-------

version
    protocol version

type
    packet type; one of QRTR_TYPE\_\*

flags
    bitmask of QRTR_FLAGS\_\*

optlen
    length of optional header data

size
    length of packet, excluding this header and optlen

src_node_id
    source node

src_port_id
    source port

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

    :param ep:
        endpoint handle
    :type ep: struct qrtr_endpoint \*

    :param data:
        data pointer
    :type data: const void \*

    :param len:
        size of data in bytes
    :type len: size_t

.. _`qrtr_endpoint_post.return`:

Return
------

0 on success; negative error code on failure

.. _`qrtr_alloc_ctrl_packet`:

qrtr_alloc_ctrl_packet
======================

.. c:function:: struct sk_buff *qrtr_alloc_ctrl_packet(struct qrtr_ctrl_pkt **pkt)

    allocate control packet skb

    :param pkt:
        reference to qrtr_ctrl_pkt pointer
    :type pkt: struct qrtr_ctrl_pkt \*\*

.. _`qrtr_alloc_ctrl_packet.description`:

Description
-----------

Returns newly allocated sk_buff, or NULL on failure

This function allocates a sk_buff large enough to carry a qrtr_ctrl_pkt and
on success returns a reference to the control packet in \ ``pkt``\ .

.. _`qrtr_endpoint_register`:

qrtr_endpoint_register
======================

.. c:function:: int qrtr_endpoint_register(struct qrtr_endpoint *ep, unsigned int nid)

    register a new endpoint

    :param ep:
        endpoint to register
    :type ep: struct qrtr_endpoint \*

    :param nid:
        desired node id; may be QRTR_EP_NID_AUTO for auto-assignment
    :type nid: unsigned int

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

    :param ep:
        endpoint to unregister
    :type ep: struct qrtr_endpoint \*

.. This file was automatic generated / don't edit.

