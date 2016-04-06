
.. _API-seq-hlist-next:

==============
seq_hlist_next
==============

*man seq_hlist_next(9)*

*4.6.0-rc1*

move to the next position of the hlist


Synopsis
========

.. c:function:: struct hlist_node ⋆ seq_hlist_next( void * v, struct hlist_head * head, loff_t * ppos )

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
