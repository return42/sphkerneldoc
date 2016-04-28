.. -*- coding: utf-8; mode: rst -*-

.. _API-v4l2-ctrl-handler-init-class:

============================
v4l2_ctrl_handler_init_class
============================

*man v4l2_ctrl_handler_init_class(9)*

*4.6.0-rc5*

Initialize the control handler.


Synopsis
========

.. c:function:: int v4l2_ctrl_handler_init_class( struct v4l2_ctrl_handler * hdl, unsigned nr_of_controls_hint, struct lock_class_key * key, const char * name )

Arguments
=========

``hdl``
    The control handler.

``nr_of_controls_hint``
    A hint of how many controls this handler is expected to refer to.
    This is the total number, so including any inherited controls. It
    doesn't have to be precise, but if it is way off, then you either
    waste memory (too many buckets are allocated) or the control lookup
    becomes slower (not enough buckets are allocated, so there are more
    slow list lookups). It will always work, though.

``key``
    Used by the lock validator if CONFIG_LOCKDEP is set.

``name``
    Used by the lock validator if CONFIG_LOCKDEP is set.


Description
===========

Returns an error if the buckets could not be allocated. This error will
also be stored in ``hdl``->error.

Never use this call directly, always use the v4l2_ctrl_handler_init
macro that hides the ``key`` and ``name`` arguments.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
