
.. _API-skb-seq-read:

============
skb_seq_read
============

*man skb_seq_read(9)*

*4.6.0-rc1*

Sequentially read skb data


Synopsis
========

.. c:function:: unsigned int skb_seq_read( unsigned int consumed, const u8 ** data, struct skb_seq_state * st )

Arguments
=========

``consumed``
    number of bytes consumed by the caller so far

``data``
    destination pointer for data to be returned

``st``
    state variable


Description
===========

Reads a block of skb data at ``consumed`` relative to the lower offset specified to ``skb_prepare_seq_read``. Assigns the head of the data block to ``data`` and returns the length
of the block or 0 if the end of the skb data or the upper offset has been reached.

The caller is not required to consume all of the data returned, i.e. ``consumed`` is typically set to the number of bytes already consumed and the next call to ``skb_seq_read``
will return the remaining part of the block.


Note 1
======

The size of each block of data returned can be arbitrary, this limitation is the cost for zerocopy sequential reads of potentially non linear data.


Note 2
======

Fragment lists within fragments are not implemented at the moment, state->root_skb could be replaced with a stack for this purpose.
