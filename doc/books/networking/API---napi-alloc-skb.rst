
.. _API---napi-alloc-skb:

================
__napi_alloc_skb
================

*man __napi_alloc_skb(9)*

*4.6.0-rc1*

allocate skbuff for rx in a specific NAPI instance


Synopsis
========

.. c:function:: struct sk_buff ⋆ __napi_alloc_skb( struct napi_struct * napi, unsigned int len, gfp_t gfp_mask )

Arguments
=========

``napi``
    napi instance this buffer was allocated for

``len``
    length to allocate

``gfp_mask``
    get_free_pages mask, passed to alloc_skb and alloc_pages


Description
===========

Allocate a new sk_buff for use in NAPI receive. This buffer will attempt to allocate the head from a special reserved region used only for NAPI Rx allocation. By doing this we can
save several CPU cycles by avoiding having to disable and re-enable IRQs.

``NULL`` is returned if there is no free memory.
