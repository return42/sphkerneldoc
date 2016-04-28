.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-cow-data:

============
skb_cow_data
============

*man skb_cow_data(9)*

*4.6.0-rc5*

Check that a socket buffer's data buffers are writable


Synopsis
========

.. c:function:: int skb_cow_data( struct sk_buff * skb, int tailbits, struct sk_buff ** trailer )

Arguments
=========

``skb``
    The socket buffer to check.

``tailbits``
    Amount of trailing space to be added

``trailer``
    Returned pointer to the skb where the ``tailbits`` space begins


Description
===========

Make sure that the data buffers attached to a socket buffer are
writable. If they are not, private copies are made of the data buffers
and the socket buffer is set to use these instead.

If ``tailbits`` is given, make sure that there is space to write
``tailbits`` bytes of data beyond current end of socket buffer.
``trailer`` will be set to point to the skb in which this space begins.

The number of scatterlist elements required to completely map the COW'd
and extended socket buffer will be returned.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
