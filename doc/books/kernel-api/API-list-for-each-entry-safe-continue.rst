.. -*- coding: utf-8; mode: rst -*-

.. _API-list-for-each-entry-safe-continue:

=================================
list_for_each_entry_safe_continue
=================================

*man list_for_each_entry_safe_continue(9)*

*4.6.0-rc5*

continue list iteration safe against removal


Synopsis
========

.. c:function:: list_for_each_entry_safe_continue( pos, n, head, member )

Arguments
=========

``pos``
    the type * to use as a loop cursor.

``n``
    another type * to use as temporary storage

``head``
    the head for your list.

``member``
    the name of the list_head within the struct.


Description
===========

Iterate over list of given type, continuing after current point, safe
against removal of list entry.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
