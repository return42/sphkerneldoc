
.. _API-sk-nulls-for-each-entry-offset:

==============================
sk_nulls_for_each_entry_offset
==============================

*man sk_nulls_for_each_entry_offset(9)*

*4.6.0-rc1*

iterate over a list at a given struct offset


Synopsis
========

.. c:function:: sk_nulls_for_each_entry_offset( tpos, pos, head, offset )

Arguments
=========

``tpos``
    the type ⋆ to use as a loop cursor.

``pos``
    the ``struct hlist_node`` to use as a loop cursor.

``head``
    the head for your list.

``offset``
    offset of hlist_node within the struct.
