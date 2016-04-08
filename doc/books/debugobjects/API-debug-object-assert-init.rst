
.. _API-debug-object-assert-init:

========================
debug_object_assert_init
========================

*man debug_object_assert_init(9)*

*4.6.0-rc1*

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
