.. -*- coding: utf-8; mode: rst -*-

.. _API-list-move-tail:

==============
list_move_tail
==============

*man list_move_tail(9)*

*4.6.0-rc5*

delete from one list and add as another's tail


Synopsis
========

.. c:function:: void list_move_tail( struct list_head * list, struct list_head * head )

Arguments
=========

``list``
    the entry to move

``head``
    the head that will follow our entry


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
