.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/ipv4/ip_sockglue.c

.. _`ipv4_pktinfo_prepare`:

ipv4_pktinfo_prepare
====================

.. c:function:: void ipv4_pktinfo_prepare(const struct sock *sk, struct sk_buff *skb)

    transfer some info from rtable to skb

    :param const struct sock \*sk:
        socket

    :param struct sk_buff \*skb:
        buffer

.. _`ipv4_pktinfo_prepare.description`:

Description
-----------

To support IP_CMSG_PKTINFO option, we store rt_iif and specific
destination in skb->cb[] before dst drop.
This way, receiver doesn't make cache line misses to read rtable.

.. This file was automatic generated / don't edit.

