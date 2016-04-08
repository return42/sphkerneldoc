
.. _API-xdr-skb-read-bits:

=================
xdr_skb_read_bits
=================

*man xdr_skb_read_bits(9)*

*4.6.0-rc1*

copy some data bits from skb to internal buffer


Synopsis
========

.. c:function:: size_t xdr_skb_read_bits( struct xdr_skb_reader * desc, void * to, size_t len )

Arguments
=========

``desc``
    sk_buff copy helper

``to``
    copy destination

``len``
    number of bytes to copy


Description
===========

Possibly called several times to iterate over an sk_buff and copy data out of it.
