.. -*- coding: utf-8; mode: rst -*-

.. _API-list-splice-init:

================
list_splice_init
================

*man list_splice_init(9)*

*4.6.0-rc5*

join two lists and reinitialise the emptied list.


Synopsis
========

.. c:function:: void list_splice_init( struct list_head * list, struct list_head * head )

Arguments
=========

``list``
    the new list to add.

``head``
    the place to add it in the first list.


Description
===========

The list at ``list`` is reinitialised


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
