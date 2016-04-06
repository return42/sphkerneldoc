
.. _API-list-splice:

===========
list_splice
===========

*man list_splice(9)*

*4.6.0-rc1*

join two lists, this is designed for stacks


Synopsis
========

.. c:function:: void list_splice( const struct list_head * list, struct list_head * head )

Arguments
=========

``list``
    the new list to add.

``head``
    the place to add it in the first list.
