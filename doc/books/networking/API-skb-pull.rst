.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-pull:

========
skb_pull
========

*man skb_pull(9)*

*4.6.0-rc5*

remove data from the start of a buffer


Synopsis
========

.. c:function:: unsigned char * skb_pull( struct sk_buff * skb, unsigned int len )

Arguments
=========

``skb``
    buffer to use

``len``
    amount of data to remove


Description
===========

This function removes data from the start of a buffer, returning the
memory to the headroom. A pointer to the next data in the buffer is
returned. Once the data has been pulled future pushes will overwrite the
old data.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
