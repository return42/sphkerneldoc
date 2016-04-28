.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-pad:

=======
skb_pad
=======

*man skb_pad(9)*

*4.6.0-rc5*

zero pad the tail of an skb


Synopsis
========

.. c:function:: int skb_pad( struct sk_buff * skb, int pad )

Arguments
=========

``skb``
    buffer to pad

``pad``
    space to pad


Description
===========

Ensure that a buffer is followed by a padding area that is zero filled.
Used by network drivers which may DMA or transfer data beyond the buffer
end onto the wire.

May return error in out of memory cases. The skb is freed on error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
