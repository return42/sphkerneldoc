
.. _API-debug-object-free:

=================
debug_object_free
=================

*man debug_object_free(9)*

*4.6.0-rc1*

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
