
.. _API-list-last-entry:

===============
list_last_entry
===============

*man list_last_entry(9)*

*4.6.0-rc1*

get the last element from a list


Synopsis
========

.. c:function:: list_last_entry( ptr, type, member )

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

Note, that list is expected to be not empty.
