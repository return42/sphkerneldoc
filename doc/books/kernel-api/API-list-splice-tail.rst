
.. _API-list-splice-tail:

================
list_splice_tail
================

*man list_splice_tail(9)*

*4.6.0-rc1*

join two lists, each list being a queue


Synopsis
========

.. c:function:: void list_splice_tail( struct list_head * list, struct list_head * head )

Arguments
=========

``list``
    the new list to add.

``head``
    the place to add it in the first list.
