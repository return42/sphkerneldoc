
.. _API-debug-object-destroy:

====================
debug_object_destroy
====================

*man debug_object_destroy(9)*

*4.6.0-rc1*

debug checks when an object is destroyed


Synopsis
========

.. c:function:: void debug_object_destroy( void * addr, struct debug_obj_descr * descr )

Arguments
=========

``addr``
    address of the object

``descr``
    pointer to an object specific debug description structure
