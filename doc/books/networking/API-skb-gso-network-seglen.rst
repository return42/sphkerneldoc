
.. _API-skb-gso-network-seglen:

======================
skb_gso_network_seglen
======================

*man skb_gso_network_seglen(9)*

*4.6.0-rc1*

Return length of individual segments of a gso packet


Synopsis
========

.. c:function:: unsigned int skb_gso_network_seglen( const struct sk_buff * skb )

Arguments
=========

``skb``
    GSO skb


Description
===========

skb_gso_network_seglen is used to determine the real size of the individual segments, including Layer3 (IP, IPv6) and L4 headers (TCP/UDP).

The MAC/L2 header is not accounted for.
