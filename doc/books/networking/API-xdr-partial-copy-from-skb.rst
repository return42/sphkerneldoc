.. -*- coding: utf-8; mode: rst -*-

.. _API-xdr-partial-copy-from-skb:

=========================
xdr_partial_copy_from_skb
=========================

*man xdr_partial_copy_from_skb(9)*

*4.6.0-rc5*

copy data out of an skb


Synopsis
========

.. c:function:: ssize_t xdr_partial_copy_from_skb( struct xdr_buf * xdr, unsigned int base, struct xdr_skb_reader * desc, xdr_skb_read_actor copy_actor )

Arguments
=========

``xdr``
    target XDR buffer

``base``
    starting offset

``desc``
    sk_buff copy helper

``copy_actor``
    virtual method for copying data


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
