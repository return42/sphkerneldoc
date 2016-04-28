.. -*- coding: utf-8; mode: rst -*-

.. _API-compare-ether-header:

====================
compare_ether_header
====================

*man compare_ether_header(9)*

*4.6.0-rc5*

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

Compare two Ethernet headers, returns 0 if equal. This assumes that the
network header (i.e., IP header) is 4-byte aligned OR the platform can
handle unaligned access. This is the case for all packets coming into
netif_receive_skb or similar entry points.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
