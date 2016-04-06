
.. _API-list-splice-tail-init:

=====================
list_splice_tail_init
=====================

*man list_splice_tail_init(9)*

*4.6.0-rc1*

join two lists and reinitialise the emptied list


Synopsis
========

.. c:function:: void list_splice_tail_init( struct list_head * list, struct list_head * head )

Arguments
=========

``list``
    the new list to add.

``head``
    the place to add it in the first list.


Description
===========

Each of the lists is a queue. The list at ``list`` is reinitialised
