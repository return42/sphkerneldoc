
.. _API-list-del-init:

=============
list_del_init
=============

*man list_del_init(9)*

*4.6.0-rc1*

deletes entry from list and reinitialize it.


Synopsis
========

.. c:function:: void list_del_init( struct list_head * entry )

Arguments
=========

``entry``
    the element to delete from the list.
