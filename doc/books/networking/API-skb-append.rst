.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-append:

==========
skb_append
==========

*man skb_append(9)*

*4.6.0-rc5*

append a buffer


Synopsis
========

.. c:function:: void skb_append( struct sk_buff * old, struct sk_buff * newsk, struct sk_buff_head * list )

Arguments
=========

``old``
    buffer to insert after

``newsk``
    buffer to insert

``list``
    list to use


Description
===========

Place a packet after a given packet in a list. The list locks are taken
and this function is atomic with respect to other list locked calls. A
buffer cannot be placed on two lists at the same time.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
