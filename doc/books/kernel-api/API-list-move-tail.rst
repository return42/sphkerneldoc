
.. _API-list-move-tail:

==============
list_move_tail
==============

*man list_move_tail(9)*

*4.6.0-rc1*

delete from one list and add as another's tail


Synopsis
========

.. c:function:: void list_move_tail( struct list_head * list, struct list_head * head )

Arguments
=========

``list``
    the entry to move

``head``
    the head that will follow our entry
