.. -*- coding: utf-8; mode: rst -*-

.. _API-list-for-each-prev-safe:

=======================
list_for_each_prev_safe
=======================

*man list_for_each_prev_safe(9)*

*4.6.0-rc5*

iterate over a list backwards safe against removal of list entry


Synopsis
========

.. c:function:: list_for_each_prev_safe( pos, n, head )

Arguments
=========

``pos``
    the ``struct list_head`` to use as a loop cursor.

``n``
    another ``struct list_head`` to use as temporary storage

``head``
    the head for your list.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
