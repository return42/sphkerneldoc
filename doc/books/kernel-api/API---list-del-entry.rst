.. -*- coding: utf-8; mode: rst -*-

.. _API---list-del-entry:

================
__list_del_entry
================

*man __list_del_entry(9)*

*4.6.0-rc5*

deletes entry from list.


Synopsis
========

.. c:function:: void __list_del_entry( struct list_head * entry )

Arguments
=========

``entry``
    the element to delete from the list.


Note
====

``list_empty`` on entry does not return true after this, the entry is in
an undefined state.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
