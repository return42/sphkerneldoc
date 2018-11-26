.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/decnet/dn_route.c

.. _`dn_return_short`:

dn_return_short
===============

.. c:function:: int dn_return_short(struct sk_buff *skb)

    Return a short packet to its sender

    :param skb:
        The packet to return
    :type skb: struct sk_buff \*

.. _`dn_return_long`:

dn_return_long
==============

.. c:function:: int dn_return_long(struct sk_buff *skb)

    Return a long packet to its sender

    :param skb:
        The long format packet to return
    :type skb: struct sk_buff \*

.. _`dn_route_rx_packet`:

dn_route_rx_packet
==================

.. c:function:: int dn_route_rx_packet(struct net *net, struct sock *sk, struct sk_buff *skb)

    Try and find a route for an incoming packet

    :param net:
        *undescribed*
    :type net: struct net \*

    :param sk:
        *undescribed*
    :type sk: struct sock \*

    :param skb:
        The packet to find a route for
    :type skb: struct sk_buff \*

.. _`dn_route_rx_packet.return`:

Return
------

result of input function if route is found, error code otherwise

.. This file was automatic generated / don't edit.

