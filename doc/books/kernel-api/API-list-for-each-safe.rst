
.. _API-list-for-each-safe:

==================
list_for_each_safe
==================

*man list_for_each_safe(9)*

*4.6.0-rc1*

iterate over a list safe against removal of list entry


Synopsis
========

.. c:function:: list_for_each_safe( pos, n, head )

Arguments
=========

``pos``
    the ``struct list_head`` to use as a loop cursor.

``n``
    another ``struct list_head`` to use as temporary storage

``head``
    the head for your list.
