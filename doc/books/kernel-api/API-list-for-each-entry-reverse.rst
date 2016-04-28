.. -*- coding: utf-8; mode: rst -*-

.. _API-list-for-each-entry-reverse:

===========================
list_for_each_entry_reverse
===========================

*man list_for_each_entry_reverse(9)*

*4.6.0-rc5*

iterate backwards over list of given type.


Synopsis
========

.. c:function:: list_for_each_entry_reverse( pos, head, member )

Arguments
=========

``pos``
    the type * to use as a loop cursor.

``head``
    the head for your list.

``member``
    the name of the list_head within the struct.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
