
.. _API-skb-availroom:

=============
skb_availroom
=============

*man skb_availroom(9)*

*4.6.0-rc1*

bytes at buffer end


Synopsis
========

.. c:function:: int skb_availroom( const struct sk_buff * skb )

Arguments
=========

``skb``
    buffer to check


Description
===========

Return the number of bytes of free space at the tail of an sk_buff allocated by ``sk_stream_alloc``
