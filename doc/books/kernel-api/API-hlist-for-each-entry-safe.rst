
.. _API-hlist-for-each-entry-safe:

=========================
hlist_for_each_entry_safe
=========================

*man hlist_for_each_entry_safe(9)*

*4.6.0-rc1*

iterate over list of given type safe against removal of list entry


Synopsis
========

.. c:function:: hlist_for_each_entry_safe( pos, n, head, member )

Arguments
=========

``pos``
    the type ⋆ to use as a loop cursor.

``n``
    another ``struct hlist_node`` to use as temporary storage

``head``
    the head for your list.

``member``
    the name of the hlist_node within the struct.
