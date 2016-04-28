.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-scrub-packet:

================
skb_scrub_packet
================

*man skb_scrub_packet(9)*

*4.6.0-rc5*

scrub an skb


Synopsis
========

.. c:function:: void skb_scrub_packet( struct sk_buff * skb, bool xnet )

Arguments
=========

``skb``
    buffer to clean

``xnet``
    packet is crossing netns


Description
===========

skb_scrub_packet can be used after encapsulating or decapsulting a
packet into/from a tunnel. Some information have to be cleared during
these operations. skb_scrub_packet can also be used to clean a skb
before injecting it in another namespace (``xnet`` == true). We have to
clear all information in the skb that could impact namespace isolation.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
