.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-shared:

==========
skb_shared
==========

*man skb_shared(9)*

*4.6.0-rc5*

is the buffer shared


Synopsis
========

.. c:function:: int skb_shared( const struct sk_buff * skb )

Arguments
=========

``skb``
    buffer to check


Description
===========

Returns true if more than one person has a reference to this buffer.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
