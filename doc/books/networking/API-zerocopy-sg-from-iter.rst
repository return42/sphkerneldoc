.. -*- coding: utf-8; mode: rst -*-

.. _API-zerocopy-sg-from-iter:

=====================
zerocopy_sg_from_iter
=====================

*man zerocopy_sg_from_iter(9)*

*4.6.0-rc5*

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

The function will first copy up to headlen, and then pin the userspace
pages and build frags through them.

Returns 0, -EFAULT or -EMSGSIZE.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
