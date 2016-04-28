.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-availroom:

=============
skb_availroom
=============

*man skb_availroom(9)*

*4.6.0-rc5*

bytes at buffer end


Synopsis
========

.. c:function:: int skb_availroom( const struct sk_buff * skb )

Arguments
=========

``skb``
    buffer to check


Description
===========

Return the number of bytes of free space at the tail of an sk_buff
allocated by ``sk_stream_alloc``


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
