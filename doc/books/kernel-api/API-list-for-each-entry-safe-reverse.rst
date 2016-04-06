
.. _API-list-for-each-entry-safe-reverse:

================================
list_for_each_entry_safe_reverse
================================

*man list_for_each_entry_safe_reverse(9)*

*4.6.0-rc1*

iterate backwards over list safe against removal


Synopsis
========

.. c:function:: list_for_each_entry_safe_reverse( pos, n, head, member )

Arguments
=========

``pos``
    the type ⋆ to use as a loop cursor.

``n``
    another type ⋆ to use as temporary storage

``head``
    the head for your list.

``member``
    the name of the list_head within the struct.


Description
===========

Iterate backwards over list of given type, safe against removal of list entry.
