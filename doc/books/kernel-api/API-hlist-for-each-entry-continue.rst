.. -*- coding: utf-8; mode: rst -*-

.. _API-hlist-for-each-entry-continue:

=============================
hlist_for_each_entry_continue
=============================

*man hlist_for_each_entry_continue(9)*

*4.6.0-rc5*

iterate over a hlist continuing after current point


Synopsis
========

.. c:function:: hlist_for_each_entry_continue( pos, member )

Arguments
=========

``pos``
    the type * to use as a loop cursor.

``member``
    the name of the hlist_node within the struct.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
