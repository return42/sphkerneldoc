.. -*- coding: utf-8; mode: rst -*-

.. _API-list-prepare-entry:

==================
list_prepare_entry
==================

*man list_prepare_entry(9)*

*4.6.0-rc5*

prepare a pos entry for use in ``list_for_each_entry_continue``


Synopsis
========

.. c:function:: list_prepare_entry( pos, head, member )

Arguments
=========

``pos``
    the type * to use as a start point

``head``
    the head of the list

``member``
    the name of the list_head within the struct.


Description
===========

Prepares a pos entry for use as a start point in
``list_for_each_entry_continue``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
