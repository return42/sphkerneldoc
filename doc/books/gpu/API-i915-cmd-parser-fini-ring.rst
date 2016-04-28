.. -*- coding: utf-8; mode: rst -*-

.. _API-i915-cmd-parser-fini-ring:

=========================
i915_cmd_parser_fini_ring
=========================

*man i915_cmd_parser_fini_ring(9)*

*4.6.0-rc5*

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

Releases any resources related to command parsing that may have been
initialized for the specified ring.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
