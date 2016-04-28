.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-header-release:

==================
skb_header_release
==================

*man skb_header_release(9)*

*4.6.0-rc5*

release reference to header


Synopsis
========

.. c:function:: void skb_header_release( struct sk_buff * skb )

Arguments
=========

``skb``
    buffer to operate on


Description
===========

Drop a reference to the header part of the buffer. This is done by
acquiring a payload reference. You must not read from the header part of
skb->data after this.


Note
====

Check if you can use ``__skb_header_release`` instead.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
