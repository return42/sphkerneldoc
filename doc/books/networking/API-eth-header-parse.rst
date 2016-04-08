
.. _API-eth-header-parse:

================
eth_header_parse
================

*man eth_header_parse(9)*

*4.6.0-rc1*

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
