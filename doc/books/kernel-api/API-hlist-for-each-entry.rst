
.. _API-hlist-for-each-entry:

====================
hlist_for_each_entry
====================

*man hlist_for_each_entry(9)*

*4.6.0-rc1*

iterate over list of given type


Synopsis
========

.. c:function:: hlist_for_each_entry( pos, head, member )

Arguments
=========

``pos``
    the type ⋆ to use as a loop cursor.

``head``
    the head for your list.

``member``
    the name of the hlist_node within the struct.
