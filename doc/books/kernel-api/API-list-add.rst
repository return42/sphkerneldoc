.. -*- coding: utf-8; mode: rst -*-

.. _API-list-add:

========
list_add
========

*man list_add(9)*

*4.6.0-rc5*

add a new entry


Synopsis
========

.. c:function:: void list_add( struct list_head * new, struct list_head * head )

Arguments
=========

``new``
    new entry to be added

``head``
    list head to add it after


Description
===========

Insert a new entry after the specified head. This is good for
implementing stacks.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
