
.. _API-list-for-each-entry-safe-from:

=============================
list_for_each_entry_safe_from
=============================

*man list_for_each_entry_safe_from(9)*

*4.6.0-rc1*

iterate over list from current point safe against removal


Synopsis
========

.. c:function:: list_for_each_entry_safe_from( pos, n, head, member )

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

Iterate over list of given type from current point, safe against removal of list entry.
