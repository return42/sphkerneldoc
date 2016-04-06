
.. _API-list-move:

=========
list_move
=========

*man list_move(9)*

*4.6.0-rc1*

delete from one list and add as another's head


Synopsis
========

.. c:function:: void list_move( struct list_head * list, struct list_head * head )

Arguments
=========

``list``
    the entry to move

``head``
    the head that will precede our entry
