
.. _API-csum-partial-copy-to-xdr:

========================
csum_partial_copy_to_xdr
========================

*man csum_partial_copy_to_xdr(9)*

*4.6.0-rc1*

checksum and copy data


Synopsis
========

.. c:function:: int csum_partial_copy_to_xdr( struct xdr_buf * xdr, struct sk_buff * skb )

Arguments
=========

``xdr``
    target XDR buffer

``skb``
    source skb


Description
===========

We have set things up such that we perform the checksum of the UDP packet in parallel with the copies into the RPC client iovec. -DaveM
