
.. _API-seq-hlist-start-head:

====================
seq_hlist_start_head
====================

*man seq_hlist_start_head(9)*

*4.6.0-rc1*

start an iteration of a hlist


Synopsis
========

.. c:function:: struct hlist_node ⋆ seq_hlist_start_head( struct hlist_head * head, loff_t pos )

Arguments
=========

``head``
    the head of the hlist

``pos``
    the start position of the sequence


Description
===========

Called at seq_file->op-> ``start``. Call this function if you want to print a header at the top of the output.
