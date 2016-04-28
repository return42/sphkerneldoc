.. -*- coding: utf-8; mode: rst -*-

.. _API-pskb-expand-head:

================
pskb_expand_head
================

*man pskb_expand_head(9)*

*4.6.0-rc5*

reallocate header of ``sk_buff``


Synopsis
========

.. c:function:: int pskb_expand_head( struct sk_buff * skb, int nhead, int ntail, gfp_t gfp_mask )

Arguments
=========

``skb``
    buffer to reallocate

``nhead``
    room to add at head

``ntail``
    room to add at tail

``gfp_mask``
    allocation priority


Description
===========

Expands (or creates identical copy, if ``nhead`` and ``ntail`` are zero)
header of ``skb``. ``sk_buff`` itself is not changed. ``sk_buff`` MUST
have reference count of 1. Returns zero in the case of success or error,
if expansion failed. In the last case, ``sk_buff`` is not changed.

All the pointers pointing into skb header may change and must be
reloaded after call to this function.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
