
.. _API-compare-ether-header:

====================
compare_ether_header
====================

*man compare_ether_header(9)*

*4.6.0-rc1*

Compare two Ethernet headers


Synopsis
========

.. c:function:: unsigned long compare_ether_header( const void * a, const void * b )

Arguments
=========

``a``
    Pointer to Ethernet header

``b``
    Pointer to Ethernet header


Description
===========

Compare two Ethernet headers, returns 0 if equal. This assumes that the network header (i.e., IP header) is 4-byte aligned OR the platform can handle unaligned access. This is the
case for all packets coming into netif_receive_skb or similar entry points.
