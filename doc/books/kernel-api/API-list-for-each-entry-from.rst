.. -*- coding: utf-8; mode: rst -*-

.. _API-list-for-each-entry-from:

========================
list_for_each_entry_from
========================

*man list_for_each_entry_from(9)*

*4.6.0-rc5*

iterate over list of given type from the current point


Synopsis
========

.. c:function:: list_for_each_entry_from( pos, head, member )

Arguments
=========

``pos``
    the type * to use as a loop cursor.

``head``
    the head for your list.

``member``
    the name of the list_head within the struct.


Description
===========

Iterate over list of given type, continuing from current position.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
