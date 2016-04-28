.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-reserve:

===========
skb_reserve
===========

*man skb_reserve(9)*

*4.6.0-rc5*

adjust headroom


Synopsis
========

.. c:function:: void skb_reserve( struct sk_buff * skb, int len )

Arguments
=========

``skb``
    buffer to alter

``len``
    bytes to move


Description
===========

Increase the headroom of an empty ``sk_buff`` by reducing the tail room.
This is only allowed for an empty buffer.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
