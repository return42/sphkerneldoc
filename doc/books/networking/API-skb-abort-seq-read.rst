
.. _API-skb-abort-seq-read:

==================
skb_abort_seq_read
==================

*man skb_abort_seq_read(9)*

*4.6.0-rc1*

Abort a sequential read of skb data


Synopsis
========

.. c:function:: void skb_abort_seq_read( struct skb_seq_state * st )

Arguments
=========

``st``
    state variable


Description
===========

Must be called if ``skb_seq_read`` was not called until it returned 0.
