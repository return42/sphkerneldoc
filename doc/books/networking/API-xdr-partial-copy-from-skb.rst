
.. _API-xdr-partial-copy-from-skb:

=========================
xdr_partial_copy_from_skb
=========================

*man xdr_partial_copy_from_skb(9)*

*4.6.0-rc1*

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
