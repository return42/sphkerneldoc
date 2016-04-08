
.. _API-skb-copy-bits:

=============
skb_copy_bits
=============

*man skb_copy_bits(9)*

*4.6.0-rc1*

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

Copy the specified number of bytes from the source skb to the destination buffer.

CAUTION ! : If its prototype is ever changed, check arch/{⋆}/net/{⋆}.S files, since it is called from BPF assembly code.
