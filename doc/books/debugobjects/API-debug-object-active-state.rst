
.. _API-debug-object-active-state:

=========================
debug_object_active_state
=========================

*man debug_object_active_state(9)*

*4.6.0-rc1*

debug checks object usage state machine


Synopsis
========

.. c:function:: void debug_object_active_state( void * addr, struct debug_obj_descr * descr, unsigned int expect, unsigned int next )

Arguments
=========

``addr``
    address of the object

``descr``
    pointer to an object specific debug description structure

``expect``
    expected state

``next``
    state to move to if expected state is found
