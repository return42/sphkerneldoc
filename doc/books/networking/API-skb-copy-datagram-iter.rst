
.. _API-skb-copy-datagram-iter:

======================
skb_copy_datagram_iter
======================

*man skb_copy_datagram_iter(9)*

*4.6.0-rc1*

Copy a datagram to an iovec iterator.


Synopsis
========

.. c:function:: int skb_copy_datagram_iter( const struct sk_buff * skb, int offset, struct iov_iter * to, int len )

Arguments
=========

``skb``
    buffer to copy

``offset``
    offset in the buffer to start copying from

``to``
    iovec iterator to copy to

``len``
    amount of data to copy from buffer to iovec
