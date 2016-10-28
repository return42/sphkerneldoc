.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/llc/llc_input.c

.. _`llc_pdu_type`:

llc_pdu_type
============

.. c:function:: int llc_pdu_type(struct sk_buff *skb)

    returns which LLC component must handle for PDU

    :param struct sk_buff \*skb:
        input skb

.. _`llc_pdu_type.description`:

Description
-----------

This function returns which LLC component must handle this PDU.

.. _`llc_fixup_skb`:

llc_fixup_skb
=============

.. c:function:: int llc_fixup_skb(struct sk_buff *skb)

    initializes skb pointers

    :param struct sk_buff \*skb:
        This argument points to incoming skb

.. _`llc_fixup_skb.description`:

Description
-----------

Initializes internal skb pointer to start of network layer by deriving
length of LLC header; finds length of LLC control field in LLC header
by looking at the two lowest-order bits of the first control field
byte; field is either 3 or 4 bytes long.

.. _`llc_rcv`:

llc_rcv
=======

.. c:function:: int llc_rcv(struct sk_buff *skb, struct net_device *dev, struct packet_type *pt, struct net_device *orig_dev)

    802.2 entry point from net lower layers

    :param struct sk_buff \*skb:
        received pdu

    :param struct net_device \*dev:
        device that receive pdu

    :param struct packet_type \*pt:
        packet type

    :param struct net_device \*orig_dev:
        *undescribed*

.. _`llc_rcv.description`:

Description
-----------

When the system receives a 802.2 frame this function is called. It
checks SAP and connection of received pdu and passes frame to
llc_{station,sap,conn}_rcv for sending to proper state machine. If
the frame is related to a busy connection (a connection is sending
data now), it queues this frame in the connection's backlog.

.. This file was automatic generated / don't edit.

