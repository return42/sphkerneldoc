
.. _API---list-del-entry:

================
__list_del_entry
================

*man __list_del_entry(9)*

*4.6.0-rc1*

deletes entry from list.


Synopsis
========

.. c:function:: void __list_del_entry( struct list_head * entry )

Arguments
=========

``entry``
    the element to delete from the list.


Note
====

``list_empty`` on entry does not return true after this, the entry is in an undefined state.
