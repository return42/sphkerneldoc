
.. _API-i915-guc-submit:

===============
i915_guc_submit
===============

*man i915_guc_submit(9)*

*4.6.0-rc1*

Submit commands through GuC


Synopsis
========

.. c:function:: int i915_guc_submit( struct i915_guc_client * client, struct drm_i915_gem_request * rq )

Arguments
=========

``client``
    the guc client where commands will go through

``rq``
    request associated with the commands


Return
======

0 if succeed
