.. -*- coding: utf-8; mode: rst -*-

========
output.c
========


.. _`dccp_determine_ccmps`:

dccp_determine_ccmps
====================

.. c:function:: u32 dccp_determine_ccmps (const struct dccp_sock *dp)

    Find out about CCID-specific packet-size limits We only consider the HC-sender CCID for setting the CCMPS (RFC 4340, 14.), since the RX CCID is restricted to feedback packets (Acks), which are small in comparison with the data traffic. A value of 0 means "no current CCMPS".

    :param const struct dccp_sock \*dp:

        *undescribed*



.. _`dccp_wait_for_ccid`:

dccp_wait_for_ccid
==================

.. c:function:: int dccp_wait_for_ccid (struct sock *sk, unsigned long delay)

    Await CCID send permission

    :param struct sock \*sk:
        socket to wait for

    :param unsigned long delay:
        timeout in jiffies



.. _`dccp_wait_for_ccid.description`:

Description
-----------

This is used by CCIDs which need to delay the send time in process context.



.. _`dccp_xmit_packet`:

dccp_xmit_packet
================

.. c:function:: void dccp_xmit_packet (struct sock *sk)

    Send data packet under control of CCID Transmits next-queued payload and informs CCID to account for the packet.

    :param struct sock \*sk:

        *undescribed*



.. _`dccp_flush_write_queue`:

dccp_flush_write_queue
======================

.. c:function:: void dccp_flush_write_queue (struct sock *sk, long *time_budget)

    Drain queue at end of connection Since dccp_sendmsg queues packets without waiting for them to be sent, it may happen that the TX queue is not empty at the end of a connection. We give the HC-sender CCID a grace period of up to @time_budget jiffies. If this function returns with a non-empty write queue, it will be purged later.

    :param struct sock \*sk:

        *undescribed*

    :param long \*time_budget:

        *undescribed*



.. _`dccp_retransmit_skb`:

dccp_retransmit_skb
===================

.. c:function:: int dccp_retransmit_skb (struct sock *sk)

    Retransmit Request, Close, or CloseReq packets

    :param struct sock \*sk:

        *undescribed*



.. _`dccp_retransmit_skb.there-are-only-four-retransmittable-packet-types-in-dccp`:

There are only four retransmittable packet types in DCCP
--------------------------------------------------------

- Request  in client-REQUEST  state (sec. 8.1.1),
- CloseReq in server-CLOSEREQ state (sec. 8.3),
- Close    in   node-CLOSING  state (sec. 8.3),
- Acks in client-PARTOPEN state (sec. 8.1.5, handled by :c:func:`dccp_delack_timer`).
This function expects sk->sk_send_head to contain the original skb.

