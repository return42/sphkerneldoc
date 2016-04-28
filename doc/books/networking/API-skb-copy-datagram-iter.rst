.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-copy-datagram-iter:

======================
skb_copy_datagram_iter
======================

*man skb_copy_datagram_iter(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
