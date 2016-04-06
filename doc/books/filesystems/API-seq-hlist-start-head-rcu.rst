
.. _API-seq-hlist-start-head-rcu:

========================
seq_hlist_start_head_rcu
========================

*man seq_hlist_start_head_rcu(9)*

*4.6.0-rc1*

start an iteration of a hlist protected by RCU


Synopsis
========

.. c:function:: struct hlist_node ⋆ seq_hlist_start_head_rcu( struct hlist_head * head, loff_t pos )

Arguments
=========

``head``
    the head of the hlist

``pos``
    the start position of the sequence


Description
===========

Called at seq_file->op-> ``start``. Call this function if you want to print a header at the top of the output.

This list-traversal primitive may safely run concurrently with the _rcu list-mutation primitives such as ``hlist_add_head_rcu`` as long as the traversal is guarded by
``rcu_read_lock``.
