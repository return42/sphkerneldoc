
.. _API-list-for-each-entry-reverse:

===========================
list_for_each_entry_reverse
===========================

*man list_for_each_entry_reverse(9)*

*4.6.0-rc1*

iterate backwards over list of given type.


Synopsis
========

.. c:function:: list_for_each_entry_reverse( pos, head, member )

Arguments
=========

``pos``
    the type ⋆ to use as a loop cursor.

``head``
    the head for your list.

``member``
    the name of the list_head within the struct.
