.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-tid-ampdu-rx:

===================
struct tid_ampdu_rx
===================

*man struct tid_ampdu_rx(9)*

*4.6.0-rc5*

TID aggregation information (Rx).


Synopsis
========

.. code-block:: c

    struct tid_ampdu_rx {
      struct rcu_head rcu_head;
      spinlock_t reorder_lock;
      u64 reorder_buf_filtered;
      struct sk_buff_head * reorder_buf;
      unsigned long * reorder_time;
      struct timer_list session_timer;
      struct timer_list reorder_timer;
      unsigned long last_rx;
      u16 head_seq_num;
      u16 stored_mpdu_num;
      u16 ssn;
      u16 buf_size;
      u16 timeout;
      u8 dialog_token;
      bool auto_seq;
      bool removed;
    };


Members
=======

rcu_head
    RCU head used for freeing this struct

reorder_lock
    serializes access to reorder buffer, see below.

reorder_buf_filtered
    bitmap indicating where there are filtered frames in the reorder
    buffer that should be ignored when releasing frames

reorder_buf
    buffer to reorder incoming aggregated MPDUs. An MPDU may be an
    A-MSDU with individually reported subframes.

reorder_time
    jiffies when skb was added

session_timer
    check if peer keeps Tx-ing on the TID (by timeout value)

reorder_timer
    releases expired frames from the reorder buffer.

last_rx
    jiffies of last rx activity

head_seq_num
    head sequence number in reordering buffer.

stored_mpdu_num
    number of MPDUs in reordering buffer

ssn
    Starting Sequence Number expected to be aggregated.

buf_size
    buffer size for incoming A-MPDUs

timeout
    reset timer value (in TUs).

dialog_token
    dialog token for aggregation session

auto_seq
    used for offloaded BA sessions to automatically pick head_seq_and
    and ssn.

removed
    this session is removed (but might have been found due to RCU)


Description
===========

This structure's lifetime is managed by RCU, assignments to the array
holding it must hold the aggregation mutex.

The ``reorder_lock`` is used to protect the members of this struct,
except for ``timeout``, ``buf_size`` and ``dialog_token``, which are
constant across the lifetime of the struct (the dialog token being used
only for debugging).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
