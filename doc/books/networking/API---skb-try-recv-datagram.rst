.. -*- coding: utf-8; mode: rst -*-

.. _API---skb-try-recv-datagram:

=======================
__skb_try_recv_datagram
=======================

*man __skb_try_recv_datagram(9)*

*4.6.0-rc5*

Receive a datagram skbuff


Synopsis
========

.. c:function:: struct sk_buff * __skb_try_recv_datagram( struct sock * sk, unsigned int flags, int * peeked, int * off, int * err, struct sk_buff ** last )

Arguments
=========

``sk``
    socket

``flags``
    MSG_ flags

``peeked``
    returns non-zero if this packet has been seen before

``off``
    an offset in bytes to peek skb from. Returns an offset within an skb
    where data actually starts

``err``
    error code returned

``last``
    set to last peeked message to inform the wait function what to look
    for when peeking


Description
===========

Get a datagram skbuff, understands the peeking, nonblocking wakeups and
possible races. This replaces identical code in packet, raw and udp, as
well as the IPX AX.25 and Appletalk. It also finally fixes the long
standing peek and read race for datagram sockets. If you alter this
routine remember it must be re-entrant.

This function will lock the socket if a skb is returned, so the caller
needs to unlock the socket in that case (usually by calling
skb_free_datagram). Returns NULL with *err set to -EAGAIN if no data
was available or to some other value if an error was detected.

* It does not lock socket since today. This function is * free of race
conditions. This measure should/can improve * significantly datagram
socket latencies at high loads, * when data copying to user space takes
lots of time. * (BTW I've just killed the last ``cli`` in
IP/IPv6/core/netlink/packet * 8) Great win.) * --ANK (980729)

The order of the tests when we find no data waiting are specified quite
explicitly by POSIX 1003.1g, don't change them without having the
standard around please.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
