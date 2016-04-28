.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-morph:

=========
skb_morph
=========

*man skb_morph(9)*

*4.6.0-rc5*

morph one skb into another


Synopsis
========

.. c:function:: struct sk_buff * skb_morph( struct sk_buff * dst, struct sk_buff * src )

Arguments
=========

``dst``
    the skb to receive the contents

``src``
    the skb to supply the contents


Description
===========

This is identical to skb_clone except that the target skb is supplied
by the user.

The target skb is returned upon exit.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
