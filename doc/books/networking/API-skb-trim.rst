
.. _API-skb-trim:

========
skb_trim
========

*man skb_trim(9)*

*4.6.0-rc1*

remove end from a buffer


Synopsis
========

.. c:function:: void skb_trim( struct sk_buff * skb, unsigned int len )

Arguments
=========

``skb``
    buffer to alter

``len``
    new length


Description
===========

Cut the length of a buffer down by removing data from the tail. If the buffer is already under the length specified it is not modified. The skb must be linear.
