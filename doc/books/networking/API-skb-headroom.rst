.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-headroom:

============
skb_headroom
============

*man skb_headroom(9)*

*4.6.0-rc5*

bytes at buffer head


Synopsis
========

.. c:function:: unsigned int skb_headroom( const struct sk_buff * skb )

Arguments
=========

``skb``
    buffer to check


Description
===========

Return the number of bytes of free space at the head of an ``sk_buff``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
