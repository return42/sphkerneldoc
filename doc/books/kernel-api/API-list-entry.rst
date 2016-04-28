.. -*- coding: utf-8; mode: rst -*-

.. _API-list-entry:

==========
list_entry
==========

*man list_entry(9)*

*4.6.0-rc5*

get the struct for this entry


Synopsis
========

.. c:function:: list_entry( ptr, type, member )

Arguments
=========

``ptr``
    the ``struct list_head`` pointer.

``type``
    the type of the struct this is embedded in.

``member``
    the name of the list_head within the struct.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
