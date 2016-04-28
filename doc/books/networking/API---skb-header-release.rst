.. -*- coding: utf-8; mode: rst -*-

.. _API---skb-header-release:

====================
__skb_header_release
====================

*man __skb_header_release(9)*

*4.6.0-rc5*

release reference to header


Synopsis
========

.. c:function:: void __skb_header_release( struct sk_buff * skb )

Arguments
=========

``skb``
    buffer to operate on


Description
===========

Variant of ``skb_header_release`` assuming skb is private to caller. We
can avoid one atomic operation.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
