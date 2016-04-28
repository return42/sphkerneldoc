.. -*- coding: utf-8; mode: rst -*-

.. _API-hlist-for-each-entry-safe:

=========================
hlist_for_each_entry_safe
=========================

*man hlist_for_each_entry_safe(9)*

*4.6.0-rc5*

iterate over list of given type safe against removal of list entry


Synopsis
========

.. c:function:: hlist_for_each_entry_safe( pos, n, head, member )

Arguments
=========

``pos``
    the type * to use as a loop cursor.

``n``
    another ``struct hlist_node`` to use as temporary storage

``head``
    the head for your list.

``member``
    the name of the hlist_node within the struct.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
