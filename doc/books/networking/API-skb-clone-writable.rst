.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-clone-writable:

==================
skb_clone_writable
==================

*man skb_clone_writable(9)*

*4.6.0-rc5*

is the header of a clone writable


Synopsis
========

.. c:function:: int skb_clone_writable( const struct sk_buff * skb, unsigned int len )

Arguments
=========

``skb``
    buffer to check

``len``
    length up to which to write


Description
===========

Returns true if modifying the header part of the cloned buffer does not
requires the data to be copied.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
