
.. _API-skb-shared:

==========
skb_shared
==========

*man skb_shared(9)*

*4.6.0-rc1*

is the buffer shared


Synopsis
========

.. c:function:: int skb_shared( const struct sk_buff * skb )

Arguments
=========

``skb``
    buffer to check


Description
===========

Returns true if more than one person has a reference to this buffer.
