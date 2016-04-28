.. -*- coding: utf-8; mode: rst -*-

.. _API-list-splice:

===========
list_splice
===========

*man list_splice(9)*

*4.6.0-rc5*

join two lists, this is designed for stacks


Synopsis
========

.. c:function:: void list_splice( const struct list_head * list, struct list_head * head )

Arguments
=========

``list``
    the new list to add.

``head``
    the place to add it in the first list.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
