
.. _API-debug-object-init-on-stack:

==========================
debug_object_init_on_stack
==========================

*man debug_object_init_on_stack(9)*

*4.6.0-rc1*

debug checks when an object on stack is initialized


Synopsis
========

.. c:function:: void debug_object_init_on_stack( void * addr, struct debug_obj_descr * descr )

Arguments
=========

``addr``
    address of the object

``descr``
    pointer to an object specific debug description structure
