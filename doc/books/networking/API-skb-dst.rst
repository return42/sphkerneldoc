.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-dst:

=======
skb_dst
=======

*man skb_dst(9)*

*4.6.0-rc5*

returns skb dst_entry


Synopsis
========

.. c:function:: struct dst_entry * skb_dst( const struct sk_buff * skb )

Arguments
=========

``skb``
    buffer


Description
===========

Returns skb dst_entry, regardless of reference taken or not.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
