
.. _API-seq-hlist-next-percpu:

=====================
seq_hlist_next_percpu
=====================

*man seq_hlist_next_percpu(9)*

*4.6.0-rc1*

move to the next position of the percpu hlist array


Synopsis
========

.. c:function:: struct hlist_node ⋆ seq_hlist_next_percpu( void * v, struct hlist_head __percpu * head, int * cpu, loff_t * pos )

Arguments
=========

``v``
    pointer to current hlist_node

``head``
    pointer to percpu array of struct hlist_heads

``cpu``
    pointer to cpu “cursor”

``pos``
    start position of sequence


Description
===========

Called at seq_file->op-> ``next``.
