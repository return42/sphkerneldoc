
.. _API-skb-zerocopy:

============
skb_zerocopy
============

*man skb_zerocopy(9)*

*4.6.0-rc1*

Zero copy skb to skb


Synopsis
========

.. c:function:: int skb_zerocopy( struct sk_buff * to, struct sk_buff * from, int len, int hlen )

Arguments
=========

``to``
    destination buffer

``from``
    source buffer

``len``
    number of bytes to copy from source buffer

``hlen``
    size of linear headroom in destination buffer


Description
===========

Copies up to `len` bytes from `from` to `to` by creating references to the frags in the source buffer.

The `hlen` as calculated by ``skb_zerocopy_headlen`` specifies the headroom in the `to` buffer.


0
=

everything is OK -ENOMEM: couldn't orphan frags of ``from`` due to lack of memory -EFAULT: ``skb_copy_bits`` found some problem with skb geometry
