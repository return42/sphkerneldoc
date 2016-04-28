.. -*- coding: utf-8; mode: rst -*-

.. _API-debug-object-active-state:

=========================
debug_object_active_state
=========================

*man debug_object_active_state(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
