.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-copy-bits:

=============
skb_copy_bits
=============

*man skb_copy_bits(9)*

*4.6.0-rc5*

copy bits from skb to kernel buffer


Synopsis
========

.. c:function:: int skb_copy_bits( const struct sk_buff * skb, int offset, void * to, int len )

Arguments
=========

``skb``
    source skb

``offset``
    offset in source

``to``
    destination buffer

``len``
    number of bytes to copy


Description
===========

Copy the specified number of bytes from the source skb to the
destination buffer.

CAUTION ! : If its prototype is ever changed, check arch/{*}/net/{*}.S
files, since it is called from BPF assembly code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
