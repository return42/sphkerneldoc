.. -*- coding: utf-8; mode: rst -*-

.. _API-seq-hlist-next-rcu:

==================
seq_hlist_next_rcu
==================

*man seq_hlist_next_rcu(9)*

*4.6.0-rc5*

move to the next position of the hlist protected by RCU


Synopsis
========

.. c:function:: struct hlist_node * seq_hlist_next_rcu( void * v, struct hlist_head * head, loff_t * ppos )

Arguments
=========

``v``
    the current iterator

``head``
    the head of the hlist

``ppos``
    the current position


Description
===========

Called at seq_file->op-> ``next``.

This list-traversal primitive may safely run concurrently with the _rcu
list-mutation primitives such as ``hlist_add_head_rcu`` as long as the
traversal is guarded by ``rcu_read_lock``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
