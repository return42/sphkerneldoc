.. -*- coding: utf-8; mode: rst -*-

.. _API-debug-object-activate:

=====================
debug_object_activate
=====================

*man debug_object_activate(9)*

*4.6.0-rc5*

debug checks when an object is activated


Synopsis
========

.. c:function:: int debug_object_activate( void * addr, struct debug_obj_descr * descr )

Arguments
=========

``addr``
    address of the object

``descr``
    pointer to an object specific debug description structure Returns 0
    for success, -EINVAL for check failed.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
