.. -*- coding: utf-8; mode: rst -*-

.. _API-pskb-trim-unique:

================
pskb_trim_unique
================

*man pskb_trim_unique(9)*

*4.6.0-rc5*

remove end from a paged unique (not cloned) buffer


Synopsis
========

.. c:function:: void pskb_trim_unique( struct sk_buff * skb, unsigned int len )

Arguments
=========

``skb``
    buffer to alter

``len``
    new length


Description
===========

This is identical to pskb_trim except that the caller knows that the
skb is not cloned so we should never get an error due to out- of-memory.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
