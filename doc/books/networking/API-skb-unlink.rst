.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-unlink:

==========
skb_unlink
==========

*man skb_unlink(9)*

*4.6.0-rc5*

remove a buffer from a list


Synopsis
========

.. c:function:: void skb_unlink( struct sk_buff * skb, struct sk_buff_head * list )

Arguments
=========

``skb``
    buffer to remove

``list``
    list to use


Description
===========

Remove a packet from a list. The list locks are taken and this function
is atomic with respect to other list locked calls

You must know what list the SKB is on.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
