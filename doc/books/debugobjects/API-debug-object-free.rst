.. -*- coding: utf-8; mode: rst -*-

.. _API-debug-object-free:

=================
debug_object_free
=================

*man debug_object_free(9)*

*4.6.0-rc5*

debug checks when an object is freed


Synopsis
========

.. c:function:: void debug_object_free( void * addr, struct debug_obj_descr * descr )

Arguments
=========

``addr``
    address of the object

``descr``
    pointer to an object specific debug description structure


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
