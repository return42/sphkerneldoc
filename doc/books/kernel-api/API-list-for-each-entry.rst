.. -*- coding: utf-8; mode: rst -*-

.. _API-list-for-each-entry:

===================
list_for_each_entry
===================

*man list_for_each_entry(9)*

*4.6.0-rc5*

iterate over list of given type


Synopsis
========

.. c:function:: list_for_each_entry( pos, head, member )

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
