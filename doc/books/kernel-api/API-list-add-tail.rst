.. -*- coding: utf-8; mode: rst -*-

.. _API-list-add-tail:

=============
list_add_tail
=============

*man list_add_tail(9)*

*4.6.0-rc5*

add a new entry


Synopsis
========

.. c:function:: void list_add_tail( struct list_head * new, struct list_head * head )

Arguments
=========

``new``
    new entry to be added

``head``
    list head to add it before


Description
===========

Insert a new entry before the specified head. This is useful for
implementing queues.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
