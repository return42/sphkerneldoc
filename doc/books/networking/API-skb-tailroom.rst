.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-tailroom:

============
skb_tailroom
============

*man skb_tailroom(9)*

*4.6.0-rc5*

bytes at buffer end


Synopsis
========

.. c:function:: int skb_tailroom( const struct sk_buff * skb )

Arguments
=========

``skb``
    buffer to check


Description
===========

Return the number of bytes of free space at the tail of an sk_buff


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
