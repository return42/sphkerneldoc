
.. _API-skb-gso-transport-seglen:

========================
skb_gso_transport_seglen
========================

*man skb_gso_transport_seglen(9)*

*4.6.0-rc1*

Return length of individual segments of a gso packet


Synopsis
========

.. c:function:: unsigned int skb_gso_transport_seglen( const struct sk_buff * skb )

Arguments
=========

``skb``
    GSO skb


Description
===========

skb_gso_transport_seglen is used to determine the real size of the individual segments, including Layer4 headers (TCP/UDP).

The MAC/L2 or network (IP, IPv6) headers are not accounted for.
