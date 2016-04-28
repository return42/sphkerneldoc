.. -*- coding: utf-8; mode: rst -*-

.. _API-csum-partial-copy-to-xdr:

========================
csum_partial_copy_to_xdr
========================

*man csum_partial_copy_to_xdr(9)*

*4.6.0-rc5*

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

We have set things up such that we perform the checksum of the UDP
packet in parallel with the copies into the RPC client iovec. -DaveM


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
