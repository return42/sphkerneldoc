
.. _API-list-first-entry-or-null:

========================
list_first_entry_or_null
========================

*man list_first_entry_or_null(9)*

*4.6.0-rc1*

get the first element from a list


Synopsis
========

.. c:function:: list_first_entry_or_null( ptr, type, member )

Arguments
=========

``ptr``
    the list head to take the element from.

``type``
    the type of the struct this is embedded in.

``member``
    the name of the list_head within the struct.


Description
===========

Note that if the list is empty, it returns NULL.
