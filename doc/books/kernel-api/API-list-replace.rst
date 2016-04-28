.. -*- coding: utf-8; mode: rst -*-

.. _API-list-replace:

============
list_replace
============

*man list_replace(9)*

*4.6.0-rc5*

replace old entry by new one


Synopsis
========

.. c:function:: void list_replace( struct list_head * old, struct list_head * new )

Arguments
=========

``old``
    the element to be replaced

``new``
    the new element to insert


Description
===========

If ``old`` was empty, it will be overwritten.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
