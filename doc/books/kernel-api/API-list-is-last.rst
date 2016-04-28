.. -*- coding: utf-8; mode: rst -*-

.. _API-list-is-last:

============
list_is_last
============

*man list_is_last(9)*

*4.6.0-rc5*

tests whether ``list`` is the last entry in list ``head``


Synopsis
========

.. c:function:: int list_is_last( const struct list_head * list, const struct list_head * head )

Arguments
=========

``list``
    the entry to test

``head``
    the head of the list


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
