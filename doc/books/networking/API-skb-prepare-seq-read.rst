
.. _API-skb-prepare-seq-read:

====================
skb_prepare_seq_read
====================

*man skb_prepare_seq_read(9)*

*4.6.0-rc1*

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

Initializes the specified state variable. Must be called before invoking ``skb_seq_read`` for the first time.
