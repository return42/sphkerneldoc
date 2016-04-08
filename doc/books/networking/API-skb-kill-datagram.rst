
.. _API-skb-kill-datagram:

=================
skb_kill_datagram
=================

*man skb_kill_datagram(9)*

*4.6.0-rc1*

Free a datagram skbuff forcibly


Synopsis
========

.. c:function:: int skb_kill_datagram( struct sock * sk, struct sk_buff * skb, unsigned int flags )

Arguments
=========

``sk``
    socket

``skb``
    datagram skbuff

``flags``
    MSG_ flags


Description
===========

This function frees a datagram skbuff that was received by skb_recv_datagram. The flags argument must match the one used for skb_recv_datagram.

If the MSG_PEEK flag is set, and the packet is still on the receive queue of the socket, it will be taken off the queue before it is freed.

This function currently only disables BH when acquiring the sk_receive_queue lock. Therefore it must not be used in a context where that lock is acquired in an IRQ context.

It returns 0 if the packet was removed by us.
