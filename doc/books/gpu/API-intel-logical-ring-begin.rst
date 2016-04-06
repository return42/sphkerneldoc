
.. _API-intel-logical-ring-begin:

========================
intel_logical_ring_begin
========================

*man intel_logical_ring_begin(9)*

*4.6.0-rc1*

prepare the logical ringbuffer to accept some commands


Synopsis
========

.. c:function:: int intel_logical_ring_begin( struct drm_i915_gem_request * req, int num_dwords )

Arguments
=========

``req``
    The request to start some new work for

``num_dwords``
    number of DWORDs that we plan to write to the ringbuffer.


Description
===========

The ringbuffer might not be ready to accept the commands right away (maybe it needs to be wrapped, or wait a bit for the tail to be updated). This function takes care of that and
also preallocates a request (every workload submission is still mediated through requests, same as it did with legacy ringbuffer submission).


Return
======

non-zero if the ringbuffer is not ready to be written to.
