
.. _API-list-for-each-entry-continue-reverse:

====================================
list_for_each_entry_continue_reverse
====================================

*man list_for_each_entry_continue_reverse(9)*

*4.6.0-rc1*

iterate backwards from the given point


Synopsis
========

.. c:function:: list_for_each_entry_continue_reverse( pos, head, member )

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

Start to iterate over list of given type backwards, continuing after the current position.
