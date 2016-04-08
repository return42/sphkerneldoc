
.. _API-skb-header-cloned:

=================
skb_header_cloned
=================

*man skb_header_cloned(9)*

*4.6.0-rc1*

is the header a clone


Synopsis
========

.. c:function:: int skb_header_cloned( const struct sk_buff * skb )

Arguments
=========

``skb``
    buffer to check


Description
===========

Returns true if modifying the header part of the buffer requires the data to be copied.
