.. -*- coding: utf-8; mode: rst -*-

.. _API-list-move:

=========
list_move
=========

*man list_move(9)*

*4.6.0-rc5*

delete from one list and add as another's head


Synopsis
========

.. c:function:: void list_move( struct list_head * list, struct list_head * head )

Arguments
=========

``list``
    the entry to move

``head``
    the head that will precede our entry


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
