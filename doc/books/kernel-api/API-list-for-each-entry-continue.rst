
.. _API-list-for-each-entry-continue:

============================
list_for_each_entry_continue
============================

*man list_for_each_entry_continue(9)*

*4.6.0-rc1*

continue iteration over list of given type


Synopsis
========

.. c:function:: list_for_each_entry_continue( pos, head, member )

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

Continue to iterate over list of given type, continuing after the current position.
