
.. _API-skb-put-padto:

=============
skb_put_padto
=============

*man skb_put_padto(9)*

*4.6.0-rc1*

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

Pads up a buffer to ensure the trailing bytes exist and are blanked. If the buffer already contains sufficient data it is untouched. Otherwise it is extended. Returns zero on
success. The skb is freed on error.
