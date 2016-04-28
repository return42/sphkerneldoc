.. -*- coding: utf-8; mode: rst -*-

.. _API-list-first-entry:

================
list_first_entry
================

*man list_first_entry(9)*

*4.6.0-rc5*

get the first element from a list


Synopsis
========

.. c:function:: list_first_entry( ptr, type, member )

Arguments
=========

``ptr``
    the list head to take the element from.

``type``
    the type of the struct this is embedded in.

``member``
    the name of the list_head within the struct.


Description
===========

Note, that list is expected to be not empty.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
