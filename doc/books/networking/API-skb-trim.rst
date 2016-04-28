.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-trim:

========
skb_trim
========

*man skb_trim(9)*

*4.6.0-rc5*

remove end from a buffer


Synopsis
========

.. c:function:: void skb_trim( struct sk_buff * skb, unsigned int len )

Arguments
=========

``skb``
    buffer to alter

``len``
    new length


Description
===========

Cut the length of a buffer down by removing data from the tail. If the
buffer is already under the length specified it is not modified. The skb
must be linear.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
