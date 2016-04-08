
.. _API-sk-filter:

=========
sk_filter
=========

*man sk_filter(9)*

*4.6.0-rc1*

run a packet through a socket filter


Synopsis
========

.. c:function:: int sk_filter( struct sock * sk, struct sk_buff * skb )

Arguments
=========

``sk``
    sock associated with ``sk_buff``

``skb``
    buffer to filter


Description
===========

Run the eBPF program and then cut skb->data to correct size returned by the program. If pkt_len is 0 we toss packet. If skb->len is smaller than pkt_len we keep whole skb->data.
This is the socket level wrapper to BPF_PROG_RUN. It returns 0 if the packet should be accepted or -EPERM if the packet should be tossed.
