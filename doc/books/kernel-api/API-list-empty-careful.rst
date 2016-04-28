.. -*- coding: utf-8; mode: rst -*-

.. _API-list-empty-careful:

==================
list_empty_careful
==================

*man list_empty_careful(9)*

*4.6.0-rc5*

tests whether a list is empty and not being modified


Synopsis
========

.. c:function:: int list_empty_careful( const struct list_head * head )

Arguments
=========

``head``
    the list to test


Description
===========

tests whether a list is empty _and_ checks that no other CPU might be
in the process of modifying either member (next or prev)


NOTE
====

using ``list_empty_careful`` without synchronization can only be safe if
the only activity that can happen to the list entry is
``list_del_init``. Eg. it cannot be used if another CPU could
re-\ ``list_add`` it.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
