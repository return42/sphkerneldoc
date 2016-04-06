
.. _API-list-entry:

==========
list_entry
==========

*man list_entry(9)*

*4.6.0-rc1*

get the struct for this entry


Synopsis
========

.. c:function:: list_entry( ptr, type, member )

Arguments
=========

``ptr``
    the ``struct list_head`` pointer.

``type``
    the type of the struct this is embedded in.

``member``
    the name of the list_head within the struct.
