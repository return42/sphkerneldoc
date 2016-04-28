.. -*- coding: utf-8; mode: rst -*-

.. _API-i915-cmd-parser-init-ring:

=========================
i915_cmd_parser_init_ring
=========================

*man i915_cmd_parser_init_ring(9)*

*4.6.0-rc5*

set cmd parser related fields for a ringbuffer


Synopsis
========

.. c:function:: int i915_cmd_parser_init_ring( struct intel_engine_cs * ring )

Arguments
=========

``ring``
    the ringbuffer to initialize


Description
===========

Optionally initializes fields related to batch buffer command parsing in
the struct intel_engine_cs based on whether the platform requires
software command parsing.


Return
======

non-zero if initialization fails


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
