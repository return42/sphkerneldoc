.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-header-cloned:

=================
skb_header_cloned
=================

*man skb_header_cloned(9)*

*4.6.0-rc5*

is the header a clone


Synopsis
========

.. c:function:: int skb_header_cloned( const struct sk_buff * skb )

Arguments
=========

``skb``
    buffer to check


Description
===========

Returns true if modifying the header part of the buffer requires the
data to be copied.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
