.. -*- coding: utf-8; mode: rst -*-

.. _API-debug-object-assert-init:

========================
debug_object_assert_init
========================

*man debug_object_assert_init(9)*

*4.6.0-rc5*

debug checks when object should be init-ed


Synopsis
========

.. c:function:: void debug_object_assert_init( void * addr, struct debug_obj_descr * descr )

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
