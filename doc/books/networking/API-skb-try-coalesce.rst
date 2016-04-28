.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-try-coalesce:

================
skb_try_coalesce
================

*man skb_try_coalesce(9)*

*4.6.0-rc5*

try to merge skb to prior one


Synopsis
========

.. c:function:: bool skb_try_coalesce( struct sk_buff * to, struct sk_buff * from, bool * fragstolen, int * delta_truesize )

Arguments
=========

``to``
    prior buffer

``from``
    buffer to add

``fragstolen``
    pointer to boolean

``delta_truesize``
    how much more was allocated than was requested


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
