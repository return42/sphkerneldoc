.. -*- coding: utf-8; mode: rst -*-

.. _API---pskb-pull-tail:

================
__pskb_pull_tail
================

*man __pskb_pull_tail(9)*

*4.6.0-rc5*

advance tail of skb header


Synopsis
========

.. c:function:: unsigned char * __pskb_pull_tail( struct sk_buff * skb, int delta )

Arguments
=========

``skb``
    buffer to reallocate

``delta``
    number of bytes to advance tail


Description
===========

The function makes a sense only on a fragmented ``sk_buff``, it expands
header moving its tail forward and copying necessary data from
fragmented part.

``sk_buff`` MUST have reference count of 1.

Returns ``NULL`` (and ``sk_buff`` does not change) if pull failed or
value of new tail of skb in the case of success.

All the pointers pointing into skb header may change and must be
reloaded after call to this function.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
