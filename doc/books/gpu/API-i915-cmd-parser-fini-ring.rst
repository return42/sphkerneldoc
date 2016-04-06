
.. _API-i915-cmd-parser-fini-ring:

=========================
i915_cmd_parser_fini_ring
=========================

*man i915_cmd_parser_fini_ring(9)*

*4.6.0-rc1*

clean up cmd parser related fields


Synopsis
========

.. c:function:: void i915_cmd_parser_fini_ring( struct intel_engine_cs * ring )

Arguments
=========

``ring``
    the ringbuffer to clean up


Description
===========

Releases any resources related to command parsing that may have been initialized for the specified ring.
