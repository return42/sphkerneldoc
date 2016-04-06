
.. _API-list-splice-init:

================
list_splice_init
================

*man list_splice_init(9)*

*4.6.0-rc1*

join two lists and reinitialise the emptied list.


Synopsis
========

.. c:function:: void list_splice_init( struct list_head * list, struct list_head * head )

Arguments
=========

``list``
    the new list to add.

``head``
    the place to add it in the first list.


Description
===========

The list at ``list`` is reinitialised
