.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-get:

=======
skb_get
=======

*man skb_get(9)*

*4.6.0-rc5*

reference buffer


Synopsis
========

.. c:function:: struct sk_buff * skb_get( struct sk_buff * skb )

Arguments
=========

``skb``
    buffer to reference


Description
===========

Makes another reference to a socket buffer and returns a pointer to the
buffer.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
