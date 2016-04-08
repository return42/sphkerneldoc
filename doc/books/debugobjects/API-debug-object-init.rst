
.. _API-debug-object-init:

=================
debug_object_init
=================

*man debug_object_init(9)*

*4.6.0-rc1*

debug checks when an object is initialized


Synopsis
========

.. c:function:: void debug_object_init( void * addr, struct debug_obj_descr * descr )

Arguments
=========

``addr``
    address of the object

``descr``
    pointer to an object specific debug description structure
