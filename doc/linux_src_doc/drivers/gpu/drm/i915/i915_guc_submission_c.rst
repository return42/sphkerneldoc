.. -*- coding: utf-8; mode: rst -*-

=====================
i915_guc_submission.c
=====================



.. _xref_i915_guc_submit:

i915_guc_submit
===============

.. c:function:: int i915_guc_submit (struct i915_guc_client * client, struct drm_i915_gem_request * rq)

    Submit commands through GuC

    :param struct i915_guc_client * client:
        the guc client where commands will go through

    :param struct drm_i915_gem_request * rq:
        request associated with the commands



Return
------

0 if succeed




.. _xref_gem_allocate_guc_obj:

gem_allocate_guc_obj
====================

.. c:function:: struct drm_i915_gem_object * gem_allocate_guc_obj (struct drm_device * dev, u32 size)

    Allocate gem object for GuC usage

    :param struct drm_device * dev:
        drm device

    :param u32 size:
        size of object



Description
-----------

This is a wrapper to create a gem obj. In order to use it inside GuC, the
object needs to be pinned lifetime. Also we must pin it to gtt space other
than [0, GUC_WOPCM_TOP) because this range is reserved inside GuC.



Return
------

A drm_i915_gem_object if successful, otherwise NULL.




.. _xref_gem_release_guc_obj:

gem_release_guc_obj
===================

.. c:function:: void gem_release_guc_obj (struct drm_i915_gem_object * obj)

    Release gem object allocated for GuC usage

    :param struct drm_i915_gem_object * obj:
        gem obj to be released




.. _xref_guc_client_alloc:

guc_client_alloc
================

.. c:function:: struct i915_guc_client * guc_client_alloc (struct drm_device * dev, uint32_t priority, struct intel_context * ctx)

    Allocate an i915_guc_client

    :param struct drm_device * dev:
        drm device

    :param uint32_t priority:
        four levels priority _CRITICAL, _HIGH, _NORMAL and _LOW
        		The kernel client to replace ExecList submission is created with
        		NORMAL priority. Priority of a client for scheduler can be HIGH,
        		while a preemption context can use CRITICAL.

    :param struct intel_context * ctx:
        the context that owns the client (we use the default render
        		context)



Return
------

An i915_guc_client object if success.




.. _xref_intel_guc_suspend:

intel_guc_suspend
=================

.. c:function:: int intel_guc_suspend (struct drm_device * dev)

    notify GuC entering suspend state

    :param struct drm_device * dev:
        drm device




.. _xref_intel_guc_resume:

intel_guc_resume
================

.. c:function:: int intel_guc_resume (struct drm_device * dev)

    notify GuC resuming from suspend state

    :param struct drm_device * dev:
        drm device


