.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-put-padto:

=============
skb_put_padto
=============

*man skb_put_padto(9)*

*4.6.0-rc5*

increase size and pad an skbuff up to a minimal size


Synopsis
========

.. c:function:: int skb_put_padto( struct sk_buff * skb, unsigned int len )

Arguments
=========

``skb``
    buffer to pad

``len``
    minimal length


Description
===========

Pads up a buffer to ensure the trailing bytes exist and are blanked. If
the buffer already contains sufficient data it is untouched. Otherwise
it is extended. Returns zero on success. The skb is freed on error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
