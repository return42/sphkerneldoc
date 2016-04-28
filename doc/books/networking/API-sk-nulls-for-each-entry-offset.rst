.. -*- coding: utf-8; mode: rst -*-

.. _API-sk-nulls-for-each-entry-offset:

==============================
sk_nulls_for_each_entry_offset
==============================

*man sk_nulls_for_each_entry_offset(9)*

*4.6.0-rc5*

iterate over a list at a given struct offset


Synopsis
========

.. c:function:: sk_nulls_for_each_entry_offset( tpos, pos, head, offset )

Arguments
=========

``tpos``
    the type * to use as a loop cursor.

``pos``
    the ``struct hlist_node`` to use as a loop cursor.

``head``
    the head for your list.

``offset``
    offset of hlist_node within the struct.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
