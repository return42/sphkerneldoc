.. -*- coding: utf-8; mode: rst -*-

.. _API-skb-prepare-seq-read:

====================
skb_prepare_seq_read
====================

*man skb_prepare_seq_read(9)*

*4.6.0-rc5*

Prepare a sequential read of skb data


Synopsis
========

.. c:function:: void skb_prepare_seq_read( struct sk_buff * skb, unsigned int from, unsigned int to, struct skb_seq_state * st )

Arguments
=========

``skb``
    the buffer to read

``from``
    lower offset of data to be read

``to``
    upper offset of data to be read

``st``
    state variable


Description
===========

Initializes the specified state variable. Must be called before invoking
``skb_seq_read`` for the first time.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
