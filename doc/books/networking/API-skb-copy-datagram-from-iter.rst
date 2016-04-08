
.. _API-skb-copy-datagram-from-iter:

===========================
skb_copy_datagram_from_iter
===========================

*man skb_copy_datagram_from_iter(9)*

*4.6.0-rc1*

Copy a datagram from an iov_iter.


Synopsis
========

.. c:function:: int skb_copy_datagram_from_iter( struct sk_buff * skb, int offset, struct iov_iter * from, int len )

Arguments
=========

``skb``
    buffer to copy

``offset``
    offset in the buffer to start copying to

``from``
    the copy source

``len``
    amount of data to copy to buffer from iovec


Description
===========

Returns 0 or -EFAULT.
