
.. _API-list-for-each-entry-from:

========================
list_for_each_entry_from
========================

*man list_for_each_entry_from(9)*

*4.6.0-rc1*

iterate over list of given type from the current point


Synopsis
========

.. c:function:: list_for_each_entry_from( pos, head, member )

Arguments
=========

``pos``
    the type ⋆ to use as a loop cursor.

``head``
    the head for your list.

``member``
    the name of the list_head within the struct.


Description
===========

Iterate over list of given type, continuing from current position.
