
.. _API-skb-put:

=======
skb_put
=======

*man skb_put(9)*

*4.6.0-rc1*

add data to a buffer


Synopsis
========

.. c:function:: unsigned char ⋆ skb_put( struct sk_buff * skb, unsigned int len )

Arguments
=========

``skb``
    buffer to use

``len``
    amount of data to add


Description
===========

This function extends the used data area of the buffer. If this would exceed the total buffer size the kernel will panic. A pointer to the first byte of the extra data is returned.
