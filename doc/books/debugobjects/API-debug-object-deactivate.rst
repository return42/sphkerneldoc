
.. _API-debug-object-deactivate:

=======================
debug_object_deactivate
=======================

*man debug_object_deactivate(9)*

*4.6.0-rc1*

debug checks when an object is deactivated


Synopsis
========

.. c:function:: void debug_object_deactivate( void * addr, struct debug_obj_descr * descr )

Arguments
=========

``addr``
    address of the object

``descr``
    pointer to an object specific debug description structure
