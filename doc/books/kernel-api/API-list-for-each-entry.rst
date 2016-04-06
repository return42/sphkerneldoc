
.. _API-list-for-each-entry:

===================
list_for_each_entry
===================

*man list_for_each_entry(9)*

*4.6.0-rc1*

iterate over list of given type


Synopsis
========

.. c:function:: list_for_each_entry( pos, head, member )

Arguments
=========

``pos``
    the type ⋆ to use as a loop cursor.

``head``
    the head for your list.

``member``
    the name of the list_head within the struct.
