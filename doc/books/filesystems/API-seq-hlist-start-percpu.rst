
.. _API-seq-hlist-start-percpu:

======================
seq_hlist_start_percpu
======================

*man seq_hlist_start_percpu(9)*

*4.6.0-rc1*

start an iteration of a percpu hlist array


Synopsis
========

.. c:function:: struct hlist_node ⋆ seq_hlist_start_percpu( struct hlist_head __percpu * head, int * cpu, loff_t pos )

Arguments
=========

``head``
    pointer to percpu array of struct hlist_heads

``cpu``
    pointer to cpu “cursor”

``pos``
    start position of sequence


Description
===========

Called at seq_file->op-> ``start``.
