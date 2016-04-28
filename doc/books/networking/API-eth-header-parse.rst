.. -*- coding: utf-8; mode: rst -*-

.. _API-eth-header-parse:

================
eth_header_parse
================

*man eth_header_parse(9)*

*4.6.0-rc5*

extract hardware address from packet


Synopsis
========

.. c:function:: int eth_header_parse( const struct sk_buff * skb, unsigned char * haddr )

Arguments
=========

``skb``
    packet to extract header from

``haddr``
    destination buffer


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
