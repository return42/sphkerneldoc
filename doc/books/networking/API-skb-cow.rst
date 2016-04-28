.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-cow:

=======
skb_cow
=======

*man skb_cow(9)*

*4.6.0-rc5*

copy header of skb when it is required


Synopsis
========

.. c:function:: int skb_cow( struct sk_buff * skb, unsigned int headroom )

Arguments
=========

``skb``
    buffer to cow

``headroom``
    needed headroom


Description
===========

If the skb passed lacks sufficient headroom or its data part is shared,
data is reallocated. If reallocation fails, an error is returned and
original skb is not changed.

The result is skb with writable area skb->head...skb->tail and at least
``headroom`` of space at head.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
