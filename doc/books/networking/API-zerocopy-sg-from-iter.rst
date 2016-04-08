
.. _API-zerocopy-sg-from-iter:

=====================
zerocopy_sg_from_iter
=====================

*man zerocopy_sg_from_iter(9)*

*4.6.0-rc1*

Build a zerocopy datagram from an iov_iter


Synopsis
========

.. c:function:: int zerocopy_sg_from_iter( struct sk_buff * skb, struct iov_iter * from )

Arguments
=========

``skb``
    buffer to copy

``from``
    the source to copy from


Description
===========

The function will first copy up to headlen, and then pin the userspace pages and build frags through them.

Returns 0, -EFAULT or -EMSGSIZE.
