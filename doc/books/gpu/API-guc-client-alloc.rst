.. -*- coding: utf-8; mode: rst -*-

.. _API-guc-client-alloc:

================
guc_client_alloc
================

*man guc_client_alloc(9)*

*4.6.0-rc5*

Allocate an i915_guc_client


Synopsis
========

.. c:function:: struct i915_guc_client * guc_client_alloc( struct drm_device * dev, uint32_t priority, struct intel_context * ctx )

Arguments
=========

``dev``
    drm device

``priority``
    four levels priority _CRITICAL, _HIGH, _NORMAL and _LOW The
    kernel client to replace ExecList submission is created with NORMAL
    priority. Priority of a client for scheduler can be HIGH, while a
    preemption context can use CRITICAL.

``ctx``
    the context that owns the client (we use the default render context)


Return
======

An i915_guc_client object if success.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
