.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-execlists-submission:

==========================
intel_execlists_submission
==========================

*man intel_execlists_submission(9)*

*4.6.0-rc5*

submit a batchbuffer for execution, Execlists style


Synopsis
========

.. c:function:: int intel_execlists_submission( struct i915_execbuffer_params * params, struct drm_i915_gem_execbuffer2 * args, struct list_head * vmas )

Arguments
=========

``params``
    -- undescribed --

``args``
    execbuffer call arguments.

``vmas``
    list of vmas.


Description
===========

This is the evil twin version of i915_gem_ringbuffer_submission. It
abstracts away the submission details of the execbuffer ioctl call.


Return
======

non-zero if the submission fails.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
