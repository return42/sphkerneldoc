
.. _API---alloc-skb:

===========
__alloc_skb
===========

*man __alloc_skb(9)*

*4.6.0-rc1*

allocate a network buffer


Synopsis
========

.. c:function:: struct sk_buff ⋆ __alloc_skb( unsigned int size, gfp_t gfp_mask, int flags, int node )

Arguments
=========

``size``
    size to allocate

``gfp_mask``
    allocation mask

``flags``
    If SKB_ALLOC_FCLONE is set, allocate from fclone cache instead of head cache and allocate a cloned (child) skb. If SKB_ALLOC_RX is set, __GFP_MEMALLOC will be used for
    allocations in case the data is required for writeback

``node``
    numa node to allocate memory on


Description
===========

Allocate a new ``sk_buff``. The returned buffer has no headroom and a tail room of at least size bytes. The object has a reference count of one. The return is the buffer. On a
failure the return is ``NULL``.

Buffers may only be allocated from interrupts using a ``gfp_mask`` of ``GFP_ATOMIC``.
